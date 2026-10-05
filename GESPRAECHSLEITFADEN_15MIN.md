# 🎙️ Gesprächsleitfaden: 10–15 Minuten Projektpräsentation
## Einführung eines zentralen IT-Monitorings
**Auftraggeber:** Müller & Partner GmbH | **Auftragnehmer:** Grone Umschulungsteam  
**Stil:** Natürlich, souverän, praxisnah („in eigener Sprache“ – kein trockenes Vorlesen)

---

## ⏱️ Zeit- und Rollenübersicht (15 Minuten)

| Zeit | Folie | Thema | Sprecher (Vorschlag) |
|---|---|---|---|
| **0:00 – 1:15** | Folie 1 & 2 | Begrüßung, Projektrahmen & Agenda | **Sprecher 1** |
| **1:15 – 3:30** | Folie 3 & 4 | Ausgangslage, Problem & 11 MUSS-Anforderungen | **Sprecher 1** |
| **3:30 – 5:45** | Folie 5 & 6 | Marktanalyse (3 Kandidaten) & Nutzwertmatrix | **Sprecher 2** |
| **5:45 – 8:00** | Folie 7 & 8 | Warum Checkmk? (Entscheidung) & Testnetz-Architektur | **Sprecher 2** |
| **8:00 – 10:15** | Folie 9 & 10 | Umgesetzte Überwachung & Eigenentwicklung (Custom Check) | **Sprecher 3** |
| **10:15 – 12:30** | Folie 11 & 12 | 4 Störungssimulationen & Datenanalyse der Grenzwerte | **Sprecher 3** |
| **12:30 – 14:00** | Folie 13 & 14 | Herausforderungen, Lessons Learned & Projektergebnis | **Sprecher 1** |
| **14:00 – 15:00** | Folie 15 & 16 | Rollout-Fahrplan, Fazit & Übergang zur Live-Demo | **Alle** |

*(Hinweis: Trägt eine Person alleine vor, dienen die Sprecherangaben einfach als Strukturierung der Themenblöcke).*

---

## 🗣️ Folie für Folie: Was du sagst & worauf du zeigst

### Folie 1: Titelfolie (Minute 0:00 – 0:45)
* **Worauf du zeigst:** Auf den Titel, den 3-Tage-PoC-Hinweis und die Kernmetadaten.
* **Was du sagst:**
  > „Guten Tag zusammen und herzlich willkommen zu unserer Präsentation. Mein Name ist [Name] und zusammen mit meinem Team stellen wir Ihnen heute unser Abschlussprojekt vor: Die Einführung eines zentralen IT-Monitorings für die Müller & Partner GmbH.
  > Ziel war es, innerhalb von drei Projekttagen einen vollständigen Proof of Concept aufzusetzen, um zu beweisen, dass eine moderne Open-Source-Monitoring-Lösung Ausfälle verhindern und die IT-Abteilung massiv entlasten kann. Wir haben alle elf Muss-Anforderungen zu einhundert Prozent erfüllt – und wie wir das geschafft haben, zeigen wir Ihnen jetzt.“

---

### Folie 2: Agenda (Minute 0:45 – 1:15)
* **Worauf du zeigst:** Kurz die 4 großen Blöcke mit der Hand abfahren.
* **Was du sagst:**
  > „Wir haben unseren Vortrag in vier logische Abschnitte unterteilt: 
  > Zuerst schauen wir uns kurz an, warum Müller & Partner dringend handeln musste. 
  > Danach gehen wir in die Systemauswahl und erklären anhand unserer Nutzwertanalyse, warum Checkmk das beste Tool für den Job ist. 
  > Im dritten Teil zeigen wir die konkrete technische Umsetzung im Testnetz inklusive unserer eigenen Python-Entwicklung und den Störungstests. 
  > Am Ende ziehen wir ein klares Fazit und geben der Geschäftsführung eine fundierte Handlungsempfehlung.“

---

### Folie 3: Ausgangslage & Problemstellung (Minute 1:15 – 2:30)
* **Worauf du zeigst:** Auf die Punkte der linken Box („Manuelle Überwachung“) und die typischen Vorfälle.
* **Was du sagst:**
  > „Schauen wir auf die Ausgangslage: Müller & Partner ist in den letzten Jahren gewachsen. Immer mehr Server, Linux-Maschinen, Webdienste, Dateiserver und zentrale Dienste wie DNS und DHCP kamen dazu. 
  > Das Problem dabei: Die Überwachung lief bisher komplett manuell. Das heißt im Klartext: Ein Admin loggte sich sporadisch ein, oder – und das war der Regelfall – man erfuhr erst von einem Ausfall, wenn verärgerte Mitarbeiter am Telefon waren. 
  > Typische Vorfälle waren: DNS fiel aus, keiner merkte es sofort. Festplatten liefen unbemerkt voll, was fast zu Datenverlust geführt hätte. Und Webanwendungen reagierten quälend langsam. 
  > Die Geschäftsführung hat völlig zu Recht gesagt: Das ist reines Brandlöschen, wir brauchen eine proaktive Überwachung, die Alarm schlägt, BEVOR der Mitarbeiter überhaupt merkt, dass etwas hakt.“

---

### Folie 4: Anforderungen – Der Projektkatalog (Minute 2:30 – 3:30)
* **Worauf du zeigst:** Auf die grüne Spalte „Erfüllt ✓“ bei M01 bis M11 und kurz die 3 Kann-Punkte erwähnen.
* **Was du sagst:**
  > „Um das strukturiert anzugehen, haben wir vorab einen klaren Anforderungskatalog definiert. 
  > Es gab elf verbindliche Muss-Kriterien – von der Einrichtung des zentralen Servers, über ein Multi-System-Setup mit mindestens zwei überwachten Maschinen, aktiven Dienst-Checks für HTTP, MySQL und SSH, bis hin zu eigenen Grenzwerten, einem zentralen Dashboard und realen Störungssimulationen. 
  > Wie Sie hier in der Übersicht sehen: Alle elf Muss-Kriterien haben wir zu 100 % grün abgenommen. Zusätzlich konnten wir drei Kann-Anforderungen umsetzen – darunter ein erweitertes Skript und vorbereitete E-Mail-Alarmierung.“

---

### Folie 5: Die 3 Kandidaten im Systemvergleich (Minute 3:30 – 4:30)
* **Worauf du zeigst:** Auf die drei Produktkarten (Checkmk, Zabbix, Nagios Core).
* **Was du sagst:**
  > „Welche Software nimmt man für so ein Vorhaben? Wir haben den Open-Source-Markt sondiert und uns auf die drei bekanntesten Platzhirsche fokussiert: Checkmk Raw Edition, Zabbix und Nagios Core.
  > Alle drei kosten keine Lizenzgebühren. Aber sie unterscheiden sich dramatisch in der Philosophie: 
  > Nagios ist der Urvater – extrem ressourcenschonend, aber veraltete Oberfläche und man muss jede Textdatei per Hand editieren. Für 2026 nicht mehr zeitgemäß. 
  > Zabbix ist mächtig und hochgradig skalierbar, verlangt aber eine externe relationale Datenbank und hat eine extrem steile Lernkurve. 
  > Und Checkmk punktet sofort mit seiner intuitiven Web-Oberfläche, fertigen Dashboards und der genialen Auto-Discovery.“

---

### Folie 6: Die Nutzwertanalyse (Entscheidungsmatrix) (Minute 4:30 – 5:45)
* **Worauf du zeigst:** Auf die Spalte Gewichtung, besonders auf die Zeile „Bedienbarkeit & GUI (20%)“ und unten auf das Gesamtergebnis.
* **Was du sagst:**
  > „Um die Entscheidung nicht aus dem Bauch heraus zu treffen, haben wir eine klassische Nutzwertanalyse nach DIN-Kriterien aufgesetzt. Wir haben sieben Kriterien gewichtet – insgesamt 100 %. 
  > Das wichtigste Kriterium mit 20 % war die Bedienbarkeit und GUI, gefolgt von Dashboards, Alarmierung und Netzwerkdiensten mit jeweils 15 %. 
  > Auf einer Skala von 1 bis 5 haben wir jedes System bewertet und mit dem Gewicht multipliziert. 
  > Das Gesamtergebnis ist eindeutig: Checkmk erreicht 4,40 Punkte und belegt Platz 1. Zabbix landet mit 4,20 knapp dahinter auf Platz 2, und Nagios fällt mit 3,30 Punkten deutlich ab.“

---

### Folie 7: Warum Checkmk gewonnen hat – Der Gamechanger (Minute 5:45 – 6:45)
* **Worauf du zeigst:** Auf die linke Box (+0,55 Punkte Vorsprung) und die Differenzrechnung.
* **Was du sagst:**
  > „Man könnte sich fragen: Zabbix war bei Netzwerkdiensten und Schnittstellen doch sehr stark – warum hat Checkmk trotzdem gewonnen? 
  > Genau das zeigt diese Folie: Zabbix hat in drei Kriterien insgesamt +0,35 Punkte gutgemacht. ABER: Checkmk hat in den beiden Kriterien mit dem höchsten Praxisnutzen voll abgeräumt: Bei der Bedienbarkeit holte Checkmk eine glatte 5 und Zabbix nur eine 3 – das macht allein +0,40 Punkte Vorsprung! Und bei den fertigen Dashboards kamen nochmal +0,15 Punkte dazu. 
  > Bei einem 3-Tage-Projekt und einem schlanken IT-Team zählt jeder Tag Einarbeitungszeit. Checkmk installiert man, startet die Auto-Discovery, und das Dashboard steht. Das hat den Ausschlag gegeben.“

---

### Folie 8: Testnetz-Architektur & Topologie (Minute 6:45 – 8:00)
* **Worauf du zeigst:** Auf das 3-Knoten-Diagramm mit IP-Adressen und Ports.
* **Was du sagst:**
  > „Kommen wir zur Praxis. Wir haben in VirtualBox ein isoliertes Host-Only-Netzwerk im Subnetz 192.168.56.0/24 aufgebaut. 
  > Unser Verbund besteht aus drei Systemen: 
  > Erstens: Unser Monitoring-Server mon-srv01 auf IP .101. Hier läuft Checkmk Raw 2.3 im Docker-Container, port-gemappt auf 8080 für den Browser. 
  > Zweitens: Unser überwachter Webserver web-srv01 auf IP .102. Darauf laufen Apache2, MariaDB und SSH. 
  > Drittens: Der Windows-Host-PC auf IP .1, auf dem der native Checkmk-Windows-Agent läuft. 
  > Die Kommunikation läuft nach dem Pull-Prinzip: Der Server kontaktiert jede Minute Port 6556 auf den Zielsystemen und holt die Sensordaten ab.“

---

### Folie 9: Umgesetzte Dienst-Überwachung (M05 & M06) (Minute 8:00 – 9:00)
* **Worauf du zeigst:** Auf die Tabelle der Services und die Schwellwerte.
* **Was du sagst:**
  > „Auf web-srv01 haben wir alle geforderten Anwendungsdienste scharf geschaltet. 
  > Für den Apache-Webserver prüfen wir Port 80 aktiv auf Status 200 OK. Die Reaktionszeit haben wir gemäß Anforderung M06 belegt: Ab 2 Sekunden gibt es eine Warnung, ab 5 Sekunden wird es kritisch. 
  > Die MariaDB-Datenbank überwachen wir auf Port 3306, den SSH-Dienst auf Port 22. 
  > Und zusätzlich erfasst der Agent im Hintergrund natürlich alle Kernressourcen: CPU-Last, RAM, Festplattenbelegung und Netzwerktraffic.“

---

### Folie 10: Eigenentwicklung – Custom Local Check (M09) (Minute 9:00 – 10:15)
* **Worauf du zeigst:** Auf den Python-Codeausschnitt und das Ausgabeformat.
* **Was du sagst:**
  > „Eine besondere Prüfungsanforderung war M09: Die Eigenentwicklung eines Messwert-Skripts. 
  > Wir haben in Python 3 ein Plugin geschrieben, das auf dem Webserver liegt: active_tcp_connections.py. 
  > Was macht das Skript? Es liest über das Systemtool 'ss' alle aktiven TCP-Verbindungen im Zustand ESTABLISHED aus. 
  > Das Geniale an Checkmk ist das Local-Check-Format: Das Skript gibt einfach den Statuscode – 0 für OK, 1 für Warnung, 2 für Kritisch –, den Servicenamen, die Metrik und einen Klartext aus. 
  > Liegen mehr als 100 Verbindungen an, geht der Status auf Warnung. Bei über 200 – was auf eine DoS-Attacke hindeuten könnte – springt er auf CRIT. Checkmk übernimmt das vollautomatisch ins Dashboard und zeichnet sogar historische Graphen.“

---

### Folie 11: Störungssimulation & Testergebnisse (M10) (Minute 10:15 – 11:30)
* **Worauf du zeigst:** Auf die vier Zeilen der Tabelle und die gemessenen Sekunden.
* **Was du sagst:**
  > „Ein Monitoring ist nur so gut, wie es im Ernstfall reagiert. Deshalb haben wir vier reale Störungen provoziert: 
  > Test 1: Wir haben den Apache gestoppt. Nach 47 Sekunden sprang das Dashboard auf CRIT – 'Connection refused'. 
  > Test 2: Ein CPU-Stresstest mit dem Tool 'stress' auf 4 Kernen. Nach 62 Sekunden Warnung, nach 75 Sekunden CRIT bei 98 % Last. 
  > Test 3: Die Festplatte mit 'dd' künstlich vollgeschrieben. Nach genau 60 Sekunden schlug der Alarm bei über 95 % Füllstand an. 
  > Und Test 4: Der harte Totalausfall – wir haben die VM ausgeschaltet. Nach 127 Sekunden meldete Checkmk 'Host DOWN, PING failed'. 
  > Fazit aller Tests: 100 % Trefferquote in unter zwei Minuten, und nach Behebung sprangen alle Checks ohne manuellen Eingriff wieder auf Grün.“

---

### Folie 12: Datenanalyse & Schwellwert-Validierung (Minute 11:30 – 12:30)
* **Worauf du zeigst:** Auf die Analyse der drei Messgrößen (CPU, Festplatte, HTTP).
* **Was du sagst:**
  > „In Abgabeprodukt I haben wir die Datenverläufe analysiert. Warum sind unsere Grenzwerte genau so gewählt? 
  > Bei der CPU brauchen wir ein 5-Minuten-Zeitfenster bei 80 %, damit ein kurzer Update-Vorgang keinen Fehlalarm auslöst. 
  > Bei der Festplatte lässt eine Warnschwelle bei 85 % den Admins noch mehrere Tage Zeit, Logdateien zu bereinigen, bevor das System kollabiert. 
  > Und bei HTTP ist die Sache binär: Liefert der Webserver einen Fehler oder reagiert er länger als 5 Sekunden, können Kunden nicht arbeiten – hier ist sofortiges Handeln Pflicht. Unsere Grenzwerte haben sich als absolut praxistauglich erwiesen.“

---

### Folie 13: Herausforderungen & Lessons Learned (Minute 12:30 – 13:15)
* **Worauf du zeigst:** Auf die Tabelle der Probleme und Lösungen.
* **Was du sagst:**
  > „Natürlich lief in den drei Tagen nicht alles auf Knopfdruck. Zwei echte Herausforderungen: 
  > Erstens: Die Paketabhängigkeiten auf Ubuntu 26.04. Neuere Perl-Versionen blockierten das native .deb-Paket von Checkmk. Unsere saubere Lösung war der offizielle Docker-Container – damit läuft Checkmk komplett isoliert, stabil und startet bei jedem Booten automatisch. 
  > Zweitens: MariaDB lauschte standardmäßig nur auf 127.0.0.1. Wir haben das Bind-Address-Setting angepasst, damit die Datenbank über das Host-Only-Netzwerk sauber überwacht werden kann. 
  > Unsere wichtigste Lesson Learned: Eine saubere Netzwerkplanung vorab spart hintenraus Stunden an Fehlersuche.“

---

### Folie 14: Projektergebnis & Zielerreichung (Minute 13:15 – 14:00)
* **Worauf du zeigst:** Auf die Erfolgs-Kennzahlen: 11/11 MUSS, 13/13 Abnahmetests bestanden.
* **Was du sagst:**
  > „Fassen wir das Gesamtergebnis zusammen: 
  > Alle 11 Muss-Anforderungen sind zu 100 % erfüllt. 
  > Drei zusätzliche Kann-Anforderungen wurden implementiert. 
  > Alle vier Störungstests wurden erfolgreich bestanden. 
  > Und im strukturierten Abnahmetest nach Kapitel 11 haben wir 13 von 13 Testfällen auf 'PASSED' gesetzt. 
  > Mit 41,5 Arbeitsstunden lagen wir nur knapp 6 % über dem Plan – der Proof of Concept ist damit auf ganzer Linie gelungen.“

---

### Folie 15: Empfehlung & Rollout-Fahrplan (Minute 14:00 – 14:45)
* **Worauf du zeigst:** Auf die drei Phasen (Pilotbetrieb, Rollout, SNMP).
* **Was du sagst:**
  > „Unsere klare Handlungsempfehlung an die Geschäftsführung der Müller & Partner GmbH lautet daher: Checkmk Raw Edition sollte fest in den Produktivbetrieb übernommen werden. 
  > Wir empfehlen einen 3-Phasen-Rollout: 
  > Phase 1 in den ersten zwei Wochen: Ein dedizierter Server für Checkmk und die Anbindung der 10 kritischsten Kernserver. 
  > Phase 2 im ersten Monat: Kompletter Rollout auf alle Clients und NAS-Systeme plus E-Mail-Alarmierungsketten. 
  > Phase 3: SNMP-Überwachung der Switche und historische Kapazitätsplanung.“

---

### Folie 16: Abschluss & Übergang zur Live-Demo (Minute 14:45 – 15:00)
* **Worauf du zeigst:** Auf den Button/Link zum Dashboard.
* **Was du sagst:**
  > „Damit sind wir am Ende unseres Vortrags angekommen. Die Monitoring-Instanz läuft aktuell live auf unserem System – wir können Ihnen das Dashboard, die Host-Zustände und auf Wunsch auch gerne einen Live-Störungstest direkt vorführen. 
  > Vielen Dank für Ihre Aufmerksamkeit – wir freuen uns auf Ihre Fragen!“

---

## 💡 Typische Prüfungsfragen & Souveräne Antworten

1. **Frage: „Warum haben Sie Checkmk als Docker-Container und nicht direkt auf dem Host installiert?“**  
   *Antwort:* „Ubuntu 26.04 nutzt bereits neuere Bibliotheken wie Perl 5.40, für die ältere Checkmk-Pakete Abhängigkeitskonflikte hatten. Durch den offiziellen Docker-Container von Checkmk ist die gesamte OMD-Laufzeitumgebung vollkommen isoliert, reproduzierbar und unabhängig vom Host-Betriebssystem. Zudem startet der Container dank `--restart always` automatisch mit der VM.“

2. **Frage: „Wie skaliert Checkmk, wenn Müller & Partner auf 500 Systeme wächst?“**  
   *Antwort:* „Checkmk Raw nutzt den extrem schnellen Livestatus-Kern und ein ressourcenschonendes Pull-Verfahren über TCP-Port 6556. Selbst auf Standardhardware verwaltet Checkmk tausende Services problemlos. Sollte die Firma weiter wachsen, gibt es einen nahtlosen Upgrade-Pfad auf die Checkmk Enterprise Edition mit dem hauseigenen Micro Core (CMC).“

3. **Frage: „Warum haben Sie für den TCP-Check ein eigenes Python-Skript geschrieben?“**  
   *Antwort:* „Gemäß Muss-Kriterium M09 sollte die Erweiterbarkeit bewiesen werden. Mit Python und dem Checkmk-Local-Check-Format konnten wir in unter 25 Zeilen Code ein performantes Tool bauen, das die Metriken direkt an die RRD-Graph-Engine übergibt – ganz ohne komplexe Compiler oder Plugins.“
