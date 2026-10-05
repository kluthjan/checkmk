#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erweiterter Custom Monitoring Check: Aktive Netzwerkverbindungen (K04)
======================================================================

Projekt:      Zentrales IT-Monitoring – Müller & Partner GmbH
Auftragnehmer: Grone Umschulungsteam
Datum:        September 2026

Beschreibung:
    Erweiterte Version des TCP-Verbindungschecks mit zusätzlichen Funktionen:
    - Verbindungen pro Port zählen
    - Top-5 Verbindungsziele anzeigen
    - Detaillierte Performancedaten (je Status eine Metrik)
    - Kommandozeilenargumente für Schwellwerte (argparse)

    Erfüllt die KANN-Anforderung K04 (Erweiterte Eigenentwicklung).

Verwendung:
    ./custom_check_tcp_connections_extended.py
    ./custom_check_tcp_connections_extended.py --warn 150 --crit 250
    ./custom_check_tcp_connections_extended.py --verbose
"""

import subprocess
import sys
import argparse
from collections import Counter


def parse_arguments():
    """
    Verarbeitet Kommandozeilenargumente für flexible Konfiguration.

    Returns:
        argparse.Namespace: Geparste Argumente mit Schwellwerten.
    """
    parser = argparse.ArgumentParser(
        description='Checkmk Local Check: Aktive TCP-Verbindungen (erweitert)'
    )
    parser.add_argument(
        '--warn', '-w',
        type=int,
        default=100,
        help='Warnschwelle für Verbindungsanzahl (Standard: 100)'
    )
    parser.add_argument(
        '--crit', '-c',
        type=int,
        default=200,
        help='Kritische Schwelle für Verbindungsanzahl (Standard: 200)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Ausführliche Ausgabe auf stderr (für Debugging)'
    )
    return parser.parse_args()


def run_ss_command(args_list):
    """
    Führt einen ss-Befehl aus und gibt die Ausgabe zurück.

    Args:
        args_list (list): Argumente für den ss-Befehl.

    Returns:
        str: Ausgabe des Befehls oder leerer String bei Fehler.
    """
    try:
        result = subprocess.run(
            ['ss'] + args_list,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except Exception as e:
        print(f'Fehler bei ss-Befehl: {e}', file=sys.stderr)
        return ''


def get_established_count():
    """
    Ermittelt die Anzahl hergestellter TCP-Verbindungen.

    Returns:
        int: Anzahl der ESTABLISHED-Verbindungen.
    """
    output = run_ss_command(['-t', '-n', 'state', 'established'])
    if not output:
        return 0
    lines = output.split('\n')
    return max(0, len(lines) - 1)


def get_all_connections():
    """
    Liest alle TCP-Verbindungen mit Details aus.

    Returns:
        list[dict]: Liste von Verbindungs-Dictionaries mit Keys:
                    state, local_addr, local_port, remote_addr, remote_port
    """
    output = run_ss_command(['-t', '-n', '-a'])
    if not output:
        return []

    connections = []
    for line in output.split('\n')[1:]:  # Header überspringen
        parts = line.split()
        if len(parts) >= 5:
            state = parts[0]
            local = parts[3]
            remote = parts[4]

            # Adresse und Port trennen (letzter ':' ist Trenner)
            local_parts = local.rsplit(':', 1)
            remote_parts = remote.rsplit(':', 1)

            connections.append({
                'state': state,
                'local_addr': local_parts[0] if len(local_parts) > 1 else local,
                'local_port': local_parts[1] if len(local_parts) > 1 else '0',
                'remote_addr': remote_parts[0] if len(remote_parts) > 1 else remote,
                'remote_port': remote_parts[1] if len(remote_parts) > 1 else '0',
            })

    return connections


def count_by_state(connections):
    """
    Zählt Verbindungen nach Status.

    Args:
        connections (list[dict]): Liste der Verbindungen.

    Returns:
        Counter: Zuordnung Status → Anzahl.
    """
    return Counter(conn['state'] for conn in connections)


def count_by_local_port(connections):
    """
    Zählt Verbindungen nach lokalem Port (Server-Sicht).

    Args:
        connections (list[dict]): Liste der Verbindungen.

    Returns:
        Counter: Zuordnung Port → Anzahl.
    """
    return Counter(conn['local_port'] for conn in connections
                   if conn['state'] == 'ESTAB')


def get_top_destinations(connections, top_n=5):
    """
    Ermittelt die Top-N Verbindungsziele.

    Args:
        connections (list[dict]): Liste der Verbindungen.
        top_n (int): Anzahl der Top-Ziele.

    Returns:
        list[tuple]: Liste von (Adresse, Anzahl) Tupeln.
    """
    destinations = Counter(conn['remote_addr'] for conn in connections
                           if conn['state'] == 'ESTAB' and
                           conn['remote_addr'] not in ('*', '0.0.0.0', '::'))
    return destinations.most_common(top_n)


def determine_status(count, warn, crit):
    """
    Bestimmt den Monitoring-Status anhand der Schwellwerte.

    Args:
        count (int): Aktuelle Verbindungsanzahl.
        warn (int): Warnschwelle.
        crit (int): Kritische Schwelle.

    Returns:
        tuple: (status_code, status_text)
    """
    if count >= crit:
        return 2, 'CRIT'
    elif count >= warn:
        return 1, 'WARN'
    else:
        return 0, 'OK'


def main():
    """
    Hauptfunktion des erweiterten Custom Monitoring Checks.

    Führt eine umfassende Analyse der TCP-Verbindungen durch und
    gibt das Ergebnis mit detaillierten Performancedaten aus.
    """
    # Argumente verarbeiten
    args = parse_arguments()
    warn = args.warn
    crit = args.crit

    # Daten sammeln
    established_count = get_established_count()
    all_connections = get_all_connections()
    state_counts = count_by_state(all_connections)
    port_counts = count_by_local_port(all_connections)
    top_destinations = get_top_destinations(all_connections)

    # Status bestimmen
    status, status_text = determine_status(established_count, warn, crit)

    # --- Performancedaten zusammenstellen ---
    # Hauptmetrik
    perf_parts = [f'connections={established_count};{warn};{crit}']

    # Metriken pro Verbindungsstatus
    for state_name in ['ESTAB', 'TIME-WAIT', 'CLOSE-WAIT', 'FIN-WAIT-1',
                       'FIN-WAIT-2', 'SYN-SENT', 'SYN-RECV', 'LISTEN']:
        count_val = state_counts.get(state_name, 0)
        perf_parts.append(f'{state_name.replace("-", "_").lower()}={count_val}')

    perf_data = '|'.join([perf_parts[0]] + perf_parts[1:])
    # Checkmk Local Check: Mehrere Metriken durch | getrennt im Metrik-Feld
    # Format: metric1=val;warn;crit|metric2=val|metric3=val

    # --- Statustext zusammenstellen ---
    # Hauptinfo
    info_parts = [f'{status_text} - {established_count} aktive TCP-Verbindungen']

    # Status-Details
    state_str = ', '.join(f'{k}:{v}' for k, v in sorted(state_counts.items()))
    if state_str:
        info_parts.append(f'Status: {state_str}')

    # Top-Ports
    if port_counts:
        top_ports = port_counts.most_common(5)
        port_str = ', '.join(f'Port {p}:{c}' for p, c in top_ports)
        info_parts.append(f'Top-Ports: {port_str}')

    # Top-Ziele
    if top_destinations:
        dest_str = ', '.join(f'{addr}:{cnt}' for addr, cnt in top_destinations)
        info_parts.append(f'Top-Ziele: {dest_str}')

    info_text = ' | '.join(info_parts)

    # --- Ausgabe im Checkmk Local Check Format ---
    print(f'{status} "{args.__class__.__name__ if False else "Active_TCP_Connections_Extended"}" '
          f'{perf_data} {info_text}')

    # Verbose-Ausgabe für Debugging
    if args.verbose:
        print(f'\n--- Debug-Informationen ---', file=sys.stderr)
        print(f'Schwellwerte: WARN={warn}, CRIT={crit}', file=sys.stderr)
        print(f'Established: {established_count}', file=sys.stderr)
        print(f'Alle Verbindungen: {len(all_connections)}', file=sys.stderr)
        print(f'Status-Verteilung: {dict(state_counts)}', file=sys.stderr)
        print(f'Port-Verteilung: {dict(port_counts)}', file=sys.stderr)
        print(f'Top-5 Ziele: {top_destinations}', file=sys.stderr)


if __name__ == '__main__':
    main()
