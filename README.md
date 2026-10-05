# Einführung eines zentralen IT-Monitorings
**Proof of Concept (PoC) – Müller & Partner GmbH**  
*Auftragnehmer: Grone Umschulungsteam | September/Oktober 2026 | Version 1.0*

---

## 📌 Projektübersicht
Evaluation, Planung und prototypische Implementierung eines zentralen Open-Source-Monitoringsystems (Checkmk Raw Edition 2.3) zur proaktiven Störungserkennung von Servern, Netzwerkdiensten und Clients vor Beeinträchtigung der Endanwender.

Alle **11 MUSS-Anforderungen (M01–M11)** und 3 KANN-Anforderungen wurden vollständig umgesetzt und abgenommen.

---

## 📂 Dateien & Projektstruktur

| Datei / Verzeichnis | Beschreibung |
|---|---|
| 📄 [`Projektdokumentation_IT-Monitoring.md`](Projektdokumentation_IT-Monitoring.md) | **Hauptdokumentation** (60+ Seiten) mit allen Abgabeprodukten A bis K |
| 📕 `Projektdokumentation IT-Monitoring.pdf` | Druckfertige PDF-Version der Projektdokumentation |
| 📊 [`Abschlusspraesentation.md`](Abschlusspraesentation.md) | Leitfaden & Folientexte für die Abschlusspräsentation / das Fachgespräch |
| 📽️ `Abschlusspraesentation.pptx` / `Einführung...pptx` | PowerPoint-Präsentationsfolien |
| 🌐 [`Nutzwertanalyse_Praesentation.html`](Nutzwertanalyse_Praesentation.html) | Interaktive Web-Präsentation zur Nutzwertanalyse (direkt im Browser klickbar) |
| 📑 `Nutzwertanalyse IT-Monitoring.pdf` | Detaillierte Nutzwertmatrix als PDF |
| 🐍 [`custom_check_tcp_connections.py`](custom_check_tcp_connections.py) | Eigenentwicklung: Checkmk Local Check für aktive TCP-Verbindungen (M09) |
| ⚡ [`start_monitoring.ps1`](start_monitoring.ps1) | 1-Klick-Startskript: Fährt alle VMs hoch und öffnet das Dashboard |
| 🛠️ `stoerungssimulation/` | Testskripte für die 4 Störungsszenarien (Apache, CPU, Disk) |

---

## 🚀 Schnellstart: Monitoring starten

1. **PowerShell** im Projektordner öffnen.
2. Das Startskript ausführen:
   ```powershell
   .\start_monitoring.ps1
   ```
3. Das Skript startet automatisch beide VirtualBox-VMs und öffnet das Dashboard im Browser:  
   👉 **URL:** [http://localhost:8080/cmk/](http://localhost:8080/cmk/)  
   👉 **Benutzer:** `cmkadmin`  
   👉 **Passwort:** `cmkadmin`  

---

## 🌐 Testnetz-Architektur & Topologie

Das Testnetz ist als VirtualBox Host-Only-Netzwerk (`192.168.56.0/24`) aufgebaut:

```
                      ┌───────────────────────────────────────────┐
                      │    Windows Host-PC (win-client01)         │
                      │    IP: 192.168.56.1 | Checkmk Win-Agent   │
                      │    Web-Dashboard: http://localhost:8080   │
                      └─────────────────────┬─────────────────────┘
                                            │
                                ┌───────────┴───────────┐
                                │ VirtualBox Host-Only  │
                                │ Subnetz 192.168.56/24 │
                                └─────┬───────────┬─────┘
                                      │           │
            ┌─────────────────────────┴─┐       ┌─┴─────────────────────────┐
            │ mon-srv01 (Ubuntu VM)     │       │ web-srv01 (Geklonte VM)   │
            │ IP: 192.168.56.101        │       │ IP: 192.168.56.102        │
            │ Checkmk Server 2.3 (Docker)│       │ Apache2, MySQL, SSH       │
            │ Port 80 (HTTP) -> 8080    │       │ Checkmk Agent (Port 6556) │
            │ Port 22 (SSH)  -> 2222    │       │ Port 80 -> 8081 | 22->2223│
            └───────────────────────────┘       └───────────────────────────┘
```

---

## 🔍 Überwachte Dienste auf `web-srv01` (M05, M06, M09)

* **HTTP_Apache:** Antwortzeit auf Port 80 (Schwellwerte: WARN >2,0 s / CRIT >5,0 s)
* **MySQL_Database:** TCP-Verfügbarkeit von MariaDB auf Port 3306
* **SSH_Service:** Erreichbarkeit von OpenSSH auf Port 22
* **Active_TCP_Connections:** Eigener Checkmk-Local-Check (Schwellwerte: WARN: 100 / CRIT: 200)
* **Systemmetriken:** CPU-Auslastung, RAM, Festplattenbelegung (`/`), Netzwerk-Interfaces, Uptime

---

## 🧪 Störungssimulation (M10)

| # | Störung | Befehl auf `web-srv01` | Erkennung in Checkmk | Reaktionszeit |
|---|---|---|---|---|
| 1 | **Apache-Ausfall** | `sudo systemctl stop apache2` | `HTTP_Apache` ➔ **CRIT (Connection refused)** | 47 Sek. |
| 2 | **CPU-Volllast** | `stress --cpu 4 --timeout 180` | `CPU utilization` ➔ **WARN / CRIT** | 62 Sek. |
| 3 | **Festplatte voll** | `sudo dd if=/dev/zero of=/tmp/file bs=1M count=20000` | `Filesystem /` ➔ **CRIT (>95%)** | 60 Sek. |
| 4 | **Host-Ausfall** | VM in VirtualBox ausschalten | Host-Status ➔ **DOWN (Ping Fail)** | 127 Sek. |
