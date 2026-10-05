# Abschlusspräsentation
## Einführung eines zentralen IT-Monitorings
### Müller & Partner GmbH | Grone Umschulungsteam | September 2026

---

## Folie 1: Titelfolie

# Einführung eines zentralen IT-Monitorings

**Proof of Concept – Prototypische Implementierung**

| | |
|---|---|
| **Auftraggeber:** | Müller & Partner GmbH |
| **Auftragnehmer:** | Grone Umschulungsteam |
| **Projektlaufzeit:** | 3 Projekttage |
| **Datum:** | September 2026 |

---

## Folie 2: Agenda

1. Ausgangssituation
2. Anforderungen
3. Untersuchte Monitoring-Produkte
4. Begründung der Produktauswahl
5. Testumgebung & Netzwerkplan
6. Umgesetzte Überwachung
7. Eigenentwicklung
8. Störungssimulation
9. Datenanalyse
10. Projektergebnis & Empfehlung
11. **Live-Demonstration**

---

## Folie 3: Ausgangssituation

### Das Problem

- 📈 Wachsende IT-Infrastruktur (mehrere Server, zahlreiche Clients)
- 🔧 **Manuelle Überwachung** – keine automatische Erkennung
- ⏰ Störungen werden **zu spät** erkannt (erst bei Mitarbeiter-Meldung)

### Typische Vorfälle

| Problem | Auswirkung |
|---------|------------|
| Server nicht erreichbar | Arbeit blockiert |
| Netzwerkdienst ausgefallen | Verbindungsprobleme |
| Festplatte voll | Datenverlust-Risiko |
| Hohe CPU-Auslastung | Langsame Systeme |
| Speichermangel | System-Instabilität |

> **Geschäftsführung: „Diese Situation ist nicht mehr ausreichend."**

---

## Folie 4: Anforderungen

### MUSS-Anforderungen (M01–M11)

| ID | Anforderung | Status |
|----|-------------|--------|
| M01 | Zentraler Monitoring-Server | ✅ |
| M02 | Mindestens 2 überwachte Systeme | ✅ |
| M03 | Erreichbarkeitsprüfung | ✅ |
| M04 | CPU, RAM, Festplatte überwachen | ✅ |
| M05 | Netzwerkdienst überwachen | ✅ |
| M06 | Grenzwerte definiert & begründet | ✅ |
| M07 | Automatische Alarmierung | ✅ |
| M08 | Zentrales Dashboard | ✅ |
| M09 | Eigener Messwert (Skript) | ✅ |
| M10 | 3+ Störungen simuliert | ✅ |
| M11 | Abnahmetest durchgeführt | ✅ |

> **11 von 11 MUSS-Anforderungen erfüllt ✅**

### KANN-Anforderungen: 3 von 5 umgesetzt
- ✅ K01 – E-Mail-Alarmierung
- ✅ K02 – Erweiterte Dashboards
- ✅ K04 – Erweiterte Eigenentwicklung

---

## Folie 5: Untersuchte Monitoring-Produkte

### Drei Lösungen im Vergleich

| Kriterium | Checkmk Raw | Zabbix | Nagios Core |
|-----------|:-----------:|:------:|:-----------:|
| **Typ** | Open Source | Open Source | Open Source |
| **Web-GUI** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Auto-Discovery** | ✅ Ja | ✅ Ja | ❌ Nein |
| **Agent** | Linux + Windows | Linux + Windows | Plugin-basiert |
| **Dashboards** | Integriert | Integriert | Extern nötig |
| **Konfiguration** | GUI-basiert | GUI-basiert | Textdateien |
| **Einrichtung** | Einfach | Mittel | Komplex |

---

## Folie 6: Nutzwertanalyse – Ergebnis

### Bewertung (Skala 1–5, gewichtet)

| Kriterium | Gewicht | Checkmk | Zabbix | Nagios |
|-----------|---------|---------|--------|--------|
| Bedienbarkeit | 20 % | **5** | 3 | 2 |
| Visualisierung | 15 % | **5** | 4 | 2 |
| Alarmierung | 15 % | 4 | 4 | 3 |
| Netzwerkdienste | 15 % | 4 | **5** | 4 |
| OS-Support | 10 % | 4 | **5** | 4 |
| Kosten | 10 % | 5 | 5 | 5 |

### Gesamtergebnis

| Rang | Produkt | Punktzahl |
|:----:|---------|:---------:|
| 🥇 | **Checkmk Raw Edition** | **4,40 / 5,00** |
| 🥈 | Zabbix | 4,20 / 5,00 |
| 🥉 | Nagios Core | 3,30 / 5,00 |

---

## Folie 7: Begründung der Produktauswahl

### Warum Checkmk Raw Edition?

- ✅ **Intuitivste Web-Oberfläche** – einfache Bedienung ohne Schulungsaufwand
- ✅ **Automatische Service-Erkennung** – spart enormen Konfigurationsaufwand
- ✅ **Agent-basiert** – vorgefertigte Agenten für Linux und Windows
- ✅ **Integrierte Dashboards** – keine zusätzlichen Tools nötig
- ✅ **Kostenlos** – Open Source (GNU GPL v2)
- ✅ **Professionelle Dokumentation** – umfangreiche offizielle Docs
- ✅ **Upgrade-Pfad** – späterer Wechsel auf Enterprise Edition möglich

> Beste Kombination aus **Bedienbarkeit** und **Funktionsumfang**  
> für die Anforderungen der Müller & Partner GmbH.

---

## Folie 8: Testumgebung & Netzwerkplan

### Virtuelle Testumgebung (VirtualBox)

```
┌──────────────────────────────────────────────┐
│         Netzwerk: 192.168.100.0/24           │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │mon-srv01 │  │web-srv01 │  │win-client│   │
│  │Ubuntu    │  │Debian 12 │  │Windows 10│   │
│  │22.04 LTS │  │          │  │          │   │
│  │.100.10   │  │.100.20   │  │.100.30   │   │
│  │          │  │          │  │          │   │
│  │ Checkmk  │  │ Apache2  │  │   RDP    │   │
│  │ Server   │  │ MySQL    │  │  Agent   │   │
│  │          │  │ SSH      │  │          │   │
│  │          │  │ Agent    │  │          │   │
│  └──────────┘  └──────────┘  └──────────┘   │
│       │              │              │        │
│       └──────────────┼──────────────┘        │
│              Agent Port 6556                 │
└──────────────────────────────────────────────┘
```

| System | OS | IP | Rolle |
|--------|----|----|-------|
| mon-srv01 | Ubuntu 22.04 | .100.10 | Monitoring-Server |
| web-srv01 | Debian 12 | .100.20 | Überwachter Server |
| win-client01 | Windows 10 | .100.30 | Überwachter Client |

---

## Folie 9: Umgesetzte Überwachung

### Konfigurierte Überwachung

**Überwachte Metriken:**
- 🖥️ CPU-Auslastung (CPU load, CPU utilization)
- 💾 Arbeitsspeicher (Memory)
- 💿 Festplattenbelegung (Filesystem)
- 🌐 Netzwerkinterfaces (Traffic, Errors)
- 🔌 Dienste (Apache, MySQL, SSH)
- 📡 Erreichbarkeit (ICMP Ping)
- 🔧 Custom Check (TCP-Verbindungen)

### Definierte Grenzwerte

| Messwert | ⚠️ WARN | 🔴 CRIT |
|----------|---------|---------|
| CPU | > 80 % (5 Min) | > 95 % (5 Min) |
| RAM | > 85 % | > 95 % |
| Festplatte | > 85 % belegt | > 95 % belegt |
| HTTP | > 2s Antwortzeit | > 5s / nicht erreichbar |

---

## Folie 10: Eigenentwicklung

### Custom Monitoring Check: Aktive TCP-Verbindungen

**Sprache:** Python 3  
**Integration:** Checkmk Local Check  
**Messwert:** Anzahl aktiver TCP-Verbindungen

```python
# Kernfunktion (Auszug)
def get_tcp_connections():
    result = subprocess.run(
        ['ss', '-t', '-n', 'state', 'established'],
        capture_output=True, text=True, timeout=10
    )
    lines = result.stdout.strip().split('\n')
    return max(0, len(lines) - 1)
```

**Schwellwerte:** WARN > 100 | CRIT > 200

**Beispielausgabe:**
```
0 "Active_TCP_Connections" connections=42;100;200 
  OK - 42 aktive TCP-Verbindungen (ESTAB:38, TIME-WAIT:4)
```

**Erweiterte Version (K04):** Zusätzlich Port-Analyse, Top-5 Ziele, Argparse

---

## Folie 11: Störungssimulation

### 4 Störungen simuliert und erkannt

| Nr. | Störung | Methode | Erkannt | Alarm | Zeit |
|-----|---------|---------|:-------:|:-----:|-----:|
| 1 | Apache-Ausfall | `systemctl stop apache2` | ✅ | ✅ | 47s |
| 2 | Hohe CPU-Last | `stress --cpu 4` | ✅ | ✅ | 62s |
| 3 | Festplatte voll | `dd if=/dev/zero ...` | ✅ | ✅ | 60s |
| 4 | VM-Totalausfall | VM herunterfahren | ✅ | ✅ | 127s |

> **Alle 4 Störungen wurden automatisch erkannt und alarmiert.**  
> **Alle Systeme wurden nach den Tests wiederhergestellt. ✅**

---

## Folie 12: Datenanalyse

### 3 Messgrößen untersucht

| Messgröße | Normal | Störung | Erkennbar? | Grenzwerte |
|-----------|--------|---------|:----------:|:----------:|
| **CPU** | 5–15 % | 98–100 % | ✅ Sofort | Sinnvoll ✅ |
| **Festplatte** | 35–45 % | 85–100 % | ✅ Klar | Sinnvoll ✅ |
| **HTTP** | OK (<100ms) | Connection refused | ✅ Eindeutig | Sinnvoll ✅ |

### Erkenntnisse
- Alle Grenzwerte sind **praxistauglich**
- **Fehlalarm-Risiko:** Gering bis mittel
- **Verbesserungsvorschläge:**
  - Trendanalyse für Kapazitätsplanung
  - Content-Check für HTTP (nicht nur Erreichbarkeit)
  - Prognose „Festplatte voll in X Tagen"

---

## Folie 13: Aufgetretene Probleme

### Herausforderungen und Lösungen

| Problem | Lösung |
|---------|--------|
| Netzwerkkonfiguration der VMs war zeitaufwändig | Systematische Planung, statische IPs |
| Windows-Firewall blockierte Checkmk Agent | Manuelle Firewall-Regel für Port 6556 |
| Dokumentation parallel zur Umsetzung herausfordernd | Projektbegleitende Notizen |
| Service Discovery auf Windows weniger umfangreich | Manuelle Checks konfiguriert |

### Lessons Learned
- ⏱️ Mehr Pufferzeit für Infrastruktur einplanen
- 📝 Dokumentation **projektbegleitend** erstellen
- 🔄 Regelmäßig testen statt am Ende
- 🤝 Gute Team-Kommunikation ist entscheidend

---

## Folie 14: Projektergebnis

### Alle Ziele erreicht ✅

| Kennzahl | Ergebnis |
|----------|----------|
| MUSS-Anforderungen | **11 / 11 erfüllt (100 %)** |
| KANN-Anforderungen | **3 / 5 umgesetzt (60 %)** |
| Störungssimulation | **4 / 3 erkannt (133 %)** |
| Abnahmetest | **13 / 13 bestanden (100 %)** |
| Projektzeit | Geplant: 39h → Tatsächlich: 41,5h (+6,4 %) |

### Proof of Concept: **ERFOLGREICH** ✅

> Checkmk Raw Edition ist als zentrale Monitoring-Lösung  
> für die Müller & Partner GmbH **geeignet**.

---

## Folie 15: Empfehlung

### Empfohlene nächste Schritte

**Phase 1 – Pilotbetrieb** (1–2 Wochen)
- Checkmk auf dediziertem Server installieren
- 5–10 produktive Systeme anbinden
- IT-Mitarbeiter einarbeiten

**Phase 2 – Rollout** (2–4 Wochen)
- Alle Server und kritische Clients migrieren
- E-Mail-Benachrichtigungen an IT-Team
- Produktive Schwellwerte definieren

**Phase 3 – Erweiterung** (fortlaufend)
- SNMP-Monitoring für Netzwerkgeräte
- Log-Monitoring-Integration
- Kapazitätsplanung mit historischen Daten
- Evaluierung: Upgrade auf Enterprise Edition

---

## Folie 16: Live-Demonstration

### Demonstration der Monitoring-Lösung

**Ablauf der Live-Demo:**

1. 🖥️ **Checkmk Web-GUI** aufrufen
2. 📊 **Dashboard** mit Gesamtübersicht zeigen
3. ✅ **Host-Status** aller Systeme prüfen
4. 🔍 **Service-Details** eines Hosts anzeigen
5. 📈 **Performance-Graphen** demonstrieren
6. 🔧 **Custom Check** (TCP-Verbindungen) zeigen

**Live-Störungssimulation:**

7. 🔴 Apache-Dienst **stoppen** (`systemctl stop apache2`)
8. ⚠️ Alarm-Erkennung im Dashboard **live beobachten**
9. 📧 Benachrichtigung prüfen
10. 🟢 Dienst **wiederherstellen** und Rückkehr zu OK zeigen

---

## Folie 17: Vielen Dank!

# Vielen Dank für Ihre Aufmerksamkeit!

### Haben Sie Fragen?

---

**Projekt:** Einführung eines zentralen IT-Monitorings  
**Auftraggeber:** Müller & Partner GmbH  
**Projektteam:** Grone Umschulungsteam  
**Datum:** September 2026  

---

*Müller & Partner GmbH – IT · Prozesse · Lösungen*
