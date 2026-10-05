#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom Monitoring Check: Aktive Netzwerkverbindungen
=====================================================

Projekt:      Zentrales IT-Monitoring – Müller & Partner GmbH
Auftragnehmer: Grone Umschulungsteam
Datum:        September 2026

Beschreibung:
    Dieses Skript ermittelt die Anzahl aktiver TCP-Verbindungen auf einem
    Linux-System und gibt das Ergebnis im Checkmk Local Check Format aus.
    Es wird als eigenständiger Messwert (MUSS-Anforderung M09) in das
    Monitoring-System integriert.

Funktionsweise:
    1. Auslesen aktiver TCP-Verbindungen über den 'ss'-Befehl
    2. Klassifizierung nach Verbindungsstatus (ESTABLISHED, TIME_WAIT, etc.)
    3. Bewertung anhand definierter Schwellwerte
    4. Ausgabe im Checkmk Local Check Format

Installation:
    1. Skript kopieren nach: /usr/lib/check_mk_agent/local/
    2. Ausführbar machen: chmod +x custom_check_tcp_connections.py
    3. In Checkmk: Service Discovery für den Host durchführen

Schwellwerte:
    - WARN (Warnung):  > 100 aktive Verbindungen
    - CRIT (Kritisch): > 200 aktive Verbindungen

Ausgabeformat (Checkmk Local Check):
    <status> "<service_name>" <metrik>=<wert>;<warn>;<crit> <statustext>

Beispiel:
    0 "Active_TCP_Connections" connections=42;100;200 OK - 42 aktive
    TCP-Verbindungen (ESTABLISHED:38, TIME_WAIT:4)
"""

import subprocess
import sys

# =============================================================================
# Konfiguration: Schwellwerte
# =============================================================================

# Warnung ab dieser Anzahl aktiver TCP-Verbindungen
WARN_THRESHOLD = 100

# Kritischer Zustand ab dieser Anzahl aktiver TCP-Verbindungen
CRIT_THRESHOLD = 200

# Name des Services in Checkmk
SERVICE_NAME = "Active_TCP_Connections"


# =============================================================================
# Funktionen
# =============================================================================

def get_tcp_connections():
    """
    Ermittelt die Anzahl aktiver TCP-Verbindungen über den 'ss'-Befehl.

    Verwendet 'ss -t -n state established' um nur hergestellte
    TCP-Verbindungen zu zählen.

    Returns:
        int: Anzahl der aktiven TCP-Verbindungen.
             Bei Fehler wird 0 zurückgegeben und eine Fehlermeldung ausgegeben.
    """
    try:
        # ss-Befehl ausführen: TCP-Verbindungen im Status 'established'
        result = subprocess.run(
            ['ss', '-t', '-n', 'state', 'established'],
            capture_output=True,
            text=True,
            timeout=10
        )

        # Ausgabe in Zeilen aufteilen
        lines = result.stdout.strip().split('\n')

        # Erste Zeile ist der Header, daher Anzahl = Zeilen - 1
        count = max(0, len(lines) - 1)
        return count

    except subprocess.TimeoutExpired:
        # Timeout: ss-Befehl hat zu lange gedauert
        print(f'3 "{SERVICE_NAME}" connections=0;{WARN_THRESHOLD};'
              f'{CRIT_THRESHOLD} UNKNOWN - Timeout bei Abfrage der '
              f'Netzwerkverbindungen')
        sys.exit(0)

    except FileNotFoundError:
        # ss-Befehl nicht gefunden
        print(f'3 "{SERVICE_NAME}" connections=0;{WARN_THRESHOLD};'
              f'{CRIT_THRESHOLD} UNKNOWN - Befehl "ss" nicht gefunden')
        sys.exit(0)

    except Exception as e:
        # Allgemeiner Fehler
        print(f'3 "{SERVICE_NAME}" connections=0;{WARN_THRESHOLD};'
              f'{CRIT_THRESHOLD} UNKNOWN - Fehler: {e}')
        sys.exit(0)


def get_connection_details():
    """
    Ermittelt detaillierte Informationen zu TCP-Verbindungsstatus.

    Liest alle TCP-Verbindungen (alle Status) aus und zählt die
    Verbindungen pro Status (ESTABLISHED, TIME_WAIT, CLOSE_WAIT, etc.).

    Returns:
        dict: Zuordnung von Status zu Anzahl, z.B.:
              {'ESTAB': 38, 'TIME-WAIT': 4, 'CLOSE-WAIT': 1}
    """
    try:
        # Alle TCP-Verbindungen abfragen (alle Status)
        result = subprocess.run(
            ['ss', '-t', '-n', '-a'],
            capture_output=True,
            text=True,
            timeout=10
        )

        # Verbindungen nach Status zählen
        states = {}
        for line in result.stdout.strip().split('\n')[1:]:  # Header überspringen
            parts = line.split()
            if parts:
                state = parts[0]
                states[state] = states.get(state, 0) + 1

        return states

    except Exception:
        # Bei Fehler leeres Dictionary zurückgeben
        return {}


def determine_status(count):
    """
    Bestimmt den Monitoring-Status basierend auf der Verbindungsanzahl.

    Checkmk Statuswerte:
        0 = OK       (alles in Ordnung)
        1 = WARNING  (Warnschwelle überschritten)
        2 = CRITICAL (Kritische Schwelle überschritten)
        3 = UNKNOWN  (Status nicht ermittelbar)

    Args:
        count (int): Anzahl der aktiven TCP-Verbindungen.

    Returns:
        tuple: (status_code, status_text) z.B. (0, 'OK')
    """
    if count >= CRIT_THRESHOLD:
        return 2, 'CRIT'
    elif count >= WARN_THRESHOLD:
        return 1, 'WARN'
    else:
        return 0, 'OK'


def format_output(status, status_text, count, details):
    """
    Formatiert die Ausgabe im Checkmk Local Check Format.

    Format: <status> "<service_name>" <metrik>=<wert>;<warn>;<crit> <text>

    Args:
        status (int): Checkmk Statuscode (0-3).
        status_text (str): Statustext (OK, WARN, CRIT).
        count (int): Anzahl aktiver Verbindungen.
        details (dict): Verbindungsdetails nach Status.

    Returns:
        str: Formatierte Ausgabezeile für Checkmk.
    """
    # Detail-String aus den Verbindungsstatus erstellen
    if details:
        detail_str = ', '.join(
            f'{key}:{value}' for key, value in sorted(details.items())
        )
        detail_info = f' ({detail_str})'
    else:
        detail_info = ''

    # Checkmk Local Check Ausgabe zusammensetzen
    output = (
        f'{status} "{SERVICE_NAME}" '
        f'connections={count};{WARN_THRESHOLD};{CRIT_THRESHOLD} '
        f'{status_text} - {count} aktive TCP-Verbindungen{detail_info}'
    )

    return output


# =============================================================================
# Hauptprogramm
# =============================================================================

def main():
    """
    Hauptfunktion des Custom Monitoring Checks.

    Ablauf:
        1. Anzahl aktiver TCP-Verbindungen ermitteln
        2. Detailinformationen zu Verbindungsstatus abrufen
        3. Status anhand der Schwellwerte bestimmen
        4. Ergebnis im Checkmk-Format ausgeben
    """
    # Schritt 1: Anzahl aktiver Verbindungen ermitteln
    count = get_tcp_connections()

    # Schritt 2: Detailinformationen abrufen
    details = get_connection_details()

    # Schritt 3: Status bestimmen
    status, status_text = determine_status(count)

    # Schritt 4: Ergebnis ausgeben
    output = format_output(status, status_text, count, details)
    print(output)


# Skript ausführen
if __name__ == '__main__':
    main()
