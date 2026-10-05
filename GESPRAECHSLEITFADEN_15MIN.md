# 🎙️ Gesprächsleitfaden: 10–15 Minuten Projektpräsentation
## Einführung eines zentralen IT-Monitorings
**Auftraggeber:** Müller & Partner GmbH | **Auftragnehmer:** Grone Umschulungsteam  
**Präsentationsdauer:** 10 bis 15 Minuten  
**Projektteam:** Jan Kluth, Marion Ballcke, Mathias Vorrau, Marco Schmidt, Robert Ortmann  
**Stil:** Natürlich, souverän, praxisnah („in eigener Sprache“ – kein trockenes Vorlesen)

---

## ⏱️ Zeit- und Rollenübersicht für das 5er-Team (15 Minuten)

| Zeitfenster | Folie | Thema | Sprecher/in |
|---|---|---|---|
| **0:00 – 0:45 min** | **Folie 1** | Begrüßung, Projektrahmen (PoC, 3 Tage) & Teamvorstellung | **Jan Kluth** |
| **0:45 – 1:15 min** | **Folie 2** | Agenda der 15 Minuten | **Jan Kluth** |
| **1:15 – 2:30 min** | **Folie 3** | Ausgangslage bei Müller & Partner & das Problem | **Jan Kluth** |
| **2:30 – 3:45 min** | **Folie 4** | Anforderungskatalog: 11 MUSS-Kriterien (M01–M11) & KANN | **Marion Ballcke** |
| **3:45 – 5:00 min** | **Folie 5** | Marktanalyse: Die 3 Kandidaten (Checkmk, Zabbix, Nagios) | **Marion Ballcke** |
| **5:00 – 6:15 min** | **Folie 6** | Nutzwertanalyse Matrix nach gewichteten DIN-Kriterien | **Mathias Vorrau** |
| **6:15 – 7:30 min** | **Folie 7** | Warum Checkmk? Der Gamechanger (+0,55 Punkte Vorsprung) | **Mathias Vorrau** |
| **7:30 – 8:45 min** | **Folie 8** | Testnetz-Architektur & Topologie (192.168.56.0/24) | **Marco Schmidt** |
| **8:45 – 9:45 min** | **Folie 9** | Umgesetzte Dienstüberwachung (HTTP, MySQL, SSH) & Schwellen | **Marco Schmidt** |
| **9:45 – 11:00 min** | **Folie 10** | Eigenentwicklung: Custom Python Local Check (`active_tcp_connections.py`) | **Marco Schmidt** |
| **11:00 – 12:15 min** | **Folie 11** | Störungssimulation: Die 4 Ausfalltests mit Reaktionszeiten | **Robert Ortmann** |
| **12:15 – 13:00 min** | **Folie 12** | Datenanalyse & Schwellwertvalidierung (CPU, Disk, HTTP) | **Robert Ortmann** |
| **13:00 – 13:45 min** | **Folie 13** | Herausforderungen & Lessons Learned (Docker, Bind-Address) | **Robert Ortmann** |
| **13:45 – 14:15 min** | **Folie 14** | Gesamtergebnis des PoC: 100 % Zielerreichung | **Jan Kluth** |
| **14:15 – 14:45 min** | **Folie 15** | Handlungsempfehlung & 3-Phasen-Rollout-Fahrplan | **Jan Kluth** |
| **14:45 – 15:00 min** | **Folie 16** | Abschluss, Danksagung & Einladung zur Live-Demonstration | **Alle gemeinsam** |

---

## 🗣️ Folie für Folie: Sprechtext für jeden Einzelnen

### Folie 1: Titelfolie (Minute 0:00 – 0:45)
* **Sprecher:** **Jan Kluth**
* **Worauf du zeigst:** Auf den Titel, den 3-Tage-PoC-Hinweis und das Kärtchen mit allen fünf Namen unseres Teams.
* **Was du sagst:**
  > „Guten Tag zusammen und herzlich willkommen zu unserer Projektpräsentation!
  > Mein Name ist Jan Kluth und ich präsentiere Ihnen heute gemeinsam mit meinen Teamkollegen Marion Ballcke, Mathias Vorrau, Marco Schmidt und Robert Ortmann unser Abschlussprojekt: Die Einführung eines zentralen IT-Monitorings für die Müller & Partner GmbH.
  > Unser Auftrag war es, innerhalb von drei Projekttagen eine praxistaugliche Open-Source-Monitoringlösung auszuwählen, in einem virtuellen Testnetzwerk aufzubauen und anhand realer Störungen zu validieren. 
  > Wir haben alle elf Muss-Anforderungen zu einhundert Prozent erfüllt – und wie wir das im Team umgesetzt haben, stellen wir Ihnen jetzt vor.“

---

### Folie 2: Agenda (Minute 0:45 – 1:15)
* **Sprecher:** **Jan Kluth**
* **Worauf du zeigst:** Auf die 4 Abschnitte und erwähnst kurz die Namen, wer was übernimmt.
* **Was du sagst:**
  > „Wir haben unseren 15-minütigen Vortrag in vier Abschnitte gegliedert und fair im Team aufgeteilt: 
  > Zuerst beleuchte ich die Ausgangslage bei Müller & Partner, bevor Marion gleich die konkreten Anforderungen und die Marktanalyse übernimmt. 
  > Danach zeigt Mathias anhand unserer Nutzwertanalyse, warum Checkmk mit klarem Vorsprung gewonnen hat. 
  > Im dritten Teil führt Marco durch die technische Umsetzung im Testnetzwerk, die Dienst-Checks und unseren eigenen Python-Check. 
  > Zum Schluss präsentieren Robert und ich die Störungstests, die Datenanalyse und unsere Empfehlung an die Geschäftsführung.“

---

### Folie 3: Ausgangslage & Problemstellung (Minute 1:15 – 2:30)
* **Sprecher:** **Jan Kluth**
* **Worauf du zeigst:** Auf die Punkte der linken Box („Manuelle Überwachung“) und die typischen Vorfälle.
* **Was du sagst:**
  > „Schauen wir auf die Ausgangslage: Müller & Partner ist in den letzten Jahren gewachsen. Zahlreiche Arbeitsplätze, mehrere Server für Webanwendungen, interne Dateiablage und zentrale Dienste wie DNS und DHCP.
  > Das Problem dabei: Die Überwachung lief bisher komplett manuell!
  > Im Klartext: Ein Admin loggte sich sporadisch ein, oder man erfuhr erst von einem Ausfall, wenn verärgerte Mitarbeiter am Telefon waren. 
  > Typische Vorfälle waren: DNS fiel aus, keiner bemerkte es sofort. Festplatten liefen fast voll – was beinahe zu Datenverlust geführt hätte. Und interne Webdienste reagierten quälend langsam. 
  > Die Geschäftsführung hat völlig zu Recht gesagt: Das ist reines Brandlöschen! Wir brauchen ein proaktives Monitoring, das Störungen im Keim meldet, BEVOR der Mitarbeiter überhaupt merkt, dass etwas hakt. 
  > Ich übergebe nun an Marion für die Anforderungen und den Systemvergleich.“

---

### Folie 4: Anforderungsanalyse (Minute 2:30 – 3:45)
* **Sprecherin:** **Marion Ballcke**
* **Worauf du zeigst:** Auf die drei übersichtlichen Spalten (Infrastruktur, Dienste, Alarmierung & Qualität) und unten auf die KANN-Features.
* **Was du sagst:**
  > „Vielen Dank, Jan! Um das Projekt strukturiert abzuarbeiten, haben wir vorab einen Pflichtenkatalog aufgestellt. Die elf verbindlichen Muss-Kriterien sehen Sie hier in drei klaren Säulen:
  > Erstens: Die Infrastruktur – ein zentraler Server und mindestens zwei überwachte Systeme mit CPU-, RAM- und Festplatten-Sensoren.
  > Zweitens: Die Netzwerkdienste – aktive Checks für Apache-Webserver, MySQL-Datenbank und SSH sowie unser eigenes Python-Skript.
  > Drittens: Alarmierung und Qualität – automatische Benachrichtigung, ein übersichtliches Dashboard und die Validierung durch reale Störungstests.
  > Wie Sie sehen: Alle elf Muss-Kriterien haben wir zu 100 % grün abgenommen! Zusätzlich konnten wir drei Kann-Anforderungen umsetzen – darunter vorbereitete E-Mail-Alarmierung und erweiterte Performance-Matrizen.“

---

### Folie 5: Die 3 Kandidaten im Systemvergleich (Minute 3:45 – 5:00)
* **Sprecherin:** **Marion Ballcke**
* **Worauf du zeigst:** Auf die drei Produktkarten (Checkmk, Zabbix, Nagios Core).
* **Was du sagst:**
  > „Welche Software nimmt man für so ein Vorhaben? Wir haben den Open-Source-Markt sondiert und uns auf die drei führenden Lösungen fokussiert: Checkmk Raw Edition, Zabbix und Nagios Core.
  > Alle drei kosten keine Lizenzgebühren, unterscheiden sich aber dramatisch in der Philosophie: 
  > Nagios ist der Urvater – extrem ressourcensparend, aber veraltet und rein textbasiert. Für moderne Admins nicht mehr zeitgemäß. 
  > Zabbix ist mächtig und hochgradig skalierbar, verlangt aber eine externe relationale Datenbank und hat eine extrem steile Lernkurve, was den Rahmen von drei Projekttagen sprengen würde. 
  > Und Checkmk punktet sofort mit seiner intuitiven WATO-Weboberfläche, fertigen Dashboards und der automatischen Service-Erkennung. 
  > Wie sich das in Zahlen ausdrückt, zeigt Ihnen jetzt Mathias.“

---

### Folie 6: Die Nutzwertanalyse (Entscheidungsmatrix) (Minute 5:00 – 6:15)
* **Sprecher:** **Mathias Vorrau**
* **Worauf du zeigst:** Auf die Spalte Gewichtung, besonders auf die Zeile „Bedienbarkeit & GUI (20%)“ und unten auf das Gesamtergebnis.
* **Was du sagst:**
  > „Danke Marion! Um die Entscheidung mathematisch fundiert zu belegen, haben wir eine klassische Nutzwertanalyse nach DIN-Kriterien aufgesetzt. Wir haben sieben Kriterien gewichtet:
  > Das wichtigste Kriterium mit 20 % war die Bedienbarkeit im Alltag. Visualisierung, Alarmierung und Netzwerkdienste wurden mit je 15 % gewichtet. 
  > Auf einer Skala von 1 bis 5 haben wir jedes System objektiv bewertet und mit dem Gewicht multipliziert. 
  > Das Gesamtergebnis ist eindeutig: Checkmk erreicht 4,40 Punkte und belegt Platz 1. Zabbix landet mit 4,20 knapp dahinter auf Platz 2, und Nagios Core fällt mit 3,30 Punkten deutlich ab.“

---

### Folie 7: Warum Checkmk gewonnen hat – Der Gamechanger (Minute 6:15 – 7:30)
* **Sprecher:** **Mathias Vorrau**
* **Worauf du zeigst:** Auf die linke Box (+0,55 Punkte Vorsprung) und die Differenzrechnung unten rechts.
* **Was du sagst:**
  > „Man könnte sich fragen: Zabbix war bei Netzwerkdiensten und Erweiterbarkeit doch sehr stark – warum hat Checkmk trotzdem gewonnen? 
  > Genau das belegt diese Folie: Zabbix war in drei Kriterien besser und holte dort insgesamt +0,35 Punkte auf. 
  > ABER: Checkmk dominierte bei den beiden Kriterien mit dem höchsten Praxisnutzen für unser Team: 
  > Bei der Bedienbarkeit holte Checkmk eine glatte 5 und Zabbix nur eine 3 – das macht allein +0,40 Punkte Vorsprung! Und bei den fertigen Dashboards kamen nochmal +0,15 Punkte dazu. 
  > Differenzrechnung: +0,55 Punkte Vorsprung minus +0,35 Punkte Aufholjagd = Ein klarer Gesamtsieg von +0,20 Punkten für Checkmk! 
  > Ich übergebe nun an Marco für die technische Umsetzung im Testnetz.“

---

### Folie 8: Testnetz-Architektur & Topologie (Minute 7:30 – 8:45)
* **Sprecher:** **Marco Schmidt**
* **Worauf du zeigst:** Auf die drei Systemkarten und den Kommunikationsfluss unten.
* **Was du sagst:**
  > „Danke Mathias! Schauen wir auf die Praxis: Wir haben in VirtualBox ein isoliertes Host-Only-Netzwerk im Subnetz 192.168.56.0/24 aufgebaut. 
  > Drei Systeme arbeiten hier zusammen: 
  > Erstens: Unser Monitoring-Server mon-srv01 auf IP .101. Hier läuft Checkmk im Docker-Container, port-gemappt auf 8080 für den Browser. 
  > Zweitens: Unser überwachter Webserver web-srv01 auf IP .102 mit Apache2, MariaDB und OpenSSH. 
  > Drittens: Der Windows-Host-PC auf IP .1, auf dem der native Checkmk-Windows-Agent läuft. 
  > Die Kommunikation erfolgt nach dem Pull-Prinzip: Der Server kontaktiert jede Minute Port 6556 der Clients und holt alle Messwerte ab.“

---

### Folie 9: Umgesetzte Dienst-Überwachung (M05 & M06) (Minute 8:45 – 9:45)
* **Sprecher:** **Marco Schmidt**
* **Worauf du zeigst:** Auf die Tabelle der Services und die Schwellwerte (Warn/Crit).
* **Was du sagst:**
  > „Auf unserem Webserver web-srv01 haben wir alle geforderten Anwendungsdienste aktiv eingebunden: 
  > Den Apache-Webserver prüfen wir auf Port 80. Die Reaktionszeit ist gemäß Anforderung M06 belegt: Ab 2 Sekunden gibt es eine Warnung, ab 5 Sekunden oder bei Ausfall ist es kritisch. 
  > Die MariaDB-Datenbank überwachen wir auf Port 3306, den SSH-Dienst auf Port 22. 
  > Und zusätzlich erfasst der Agent im Hintergrund kontinuierlich alle Systemressourcen: CPU-Auslastung, RAM, Festplattenbelegung und Netzwerkinterfaces – alles läuft aktuell im optimalen grünen Bereich.“

---

### Folie 10: Eigenentwicklung – Custom Local Check (M09) (Minute 9:45 – 11:00)
* **Sprecher:** **Marco Schmidt**
* **Worauf du zeigst:** Auf den Python-Codeausschnitt und die Protokollerklärung rechts.
* **Was du sagst:**
  > „Eine besondere Anforderung war M09: Die Eigenentwicklung eines Messwert-Skripts. 
  > Wir haben in Python 3 ein eigenes Plugin geschrieben: active_tcp_connections.py. Es liegt direkt im Agenten-Verzeichnis auf dem Webserver und liest über das Tool 'ss' alle aktiven TCP-Verbindungen im Zustand ESTABLISHED aus. 
  > Das Geniale an Checkmk ist das Local-Check-Format: Das Skript gibt einfach den Statuscode – 0 für OK, 1 für Warnung, 2 für Kritisch –, den Servicenamen, die Metrik und einen Klartext aus. 
  > Liegen mehr als 100 Verbindungen an, geht der Status auf Warnung. Bei über 200 – was auf eine DoS-Attacke hindeuten könnte – springt er auf CRIT. Checkmk übernimmt das vollautomatisch ins Dashboard und zeichnet sogar historische Graphen. 
  > Ich übergebe nun an Robert für die Störungssimulationen.“

---

### Folie 11: Störungssimulation & Testergebnisse (M10) (Minute 11:00 – 12:15)
* **Sprecher:** **Robert Ortmann**
* **Worauf du zeigst:** Auf die vier Zeilen der Tabelle und die gemessenen Sekunden in der rechten Spalte.
* **Was du sagst:**
  > „Danke Marco! Ein Monitoring ist nur so gut, wie es im Ernstfall reagiert. Deshalb haben wir vier reale Störungen provoziert: 
  > Test 1: Wir haben den Apache gestoppt. Nach genau 47 Sekunden meldete das Dashboard CRIT – Connection refused. 
  > Test 2: Ein CPU-Stresstest auf 4 Kernen. Nach 62 Sekunden Warnung, nach 75 Sekunden CRIT bei 98 % Last. 
  > Test 3: Die Festplatte künstlich vollgeschrieben. Nach genau 60 Sekunden schlug der Alarm bei über 95 % Füllstand an. 
  > Und Test 4: Der harte Host-Crash – wir haben die VM ausgeschaltet. Nach 127 Sekunden meldete Checkmk 'Host DOWN, PING failed'. 
  > Fazit: 100 % Trefferquote in unter zwei Minuten, und nach Behebung sprangen alle Checks ohne manuellen Eingriff wieder auf Grün.“

---

### Folie 12: Datenanalyse & Schwellwert-Validierung (Minute 12:15 – 13:00)
* **Sprecher:** **Robert Ortmann**
* **Worauf du zeigst:** Auf die drei Messgrößen (CPU, Festplatte, HTTP).
* **Was du sagst:**
  > „In Abgabeprodukt I haben wir die Datenverläufe analysiert. Warum sind unsere Schwellwerte genau so gewählt? 
  > Bei der CPU brauchen wir ein 5-Minuten-Zeitfenster bei 80 %, damit ein kurzer Update-Prozess keinen Fehlalarm auslöst. 
  > Bei der Festplatte lässt eine Warnschwelle bei 85 % den Admins noch mehrere Tage Zeit, Logdateien zu bereinigen, bevor das System kollabiert. 
  > Und bei HTTP ist die Sache binär: Liefert der Webserver einen Fehler oder reagiert er länger als 5 Sekunden, können Kunden nicht arbeiten – hier ist sofortiges Handeln Pflicht. Unsere Grenzwerte haben sich als absolut praxistauglich erwiesen.“

---

### Folie 13: Herausforderungen & Lessons Learned (Minute 13:00 – 13:45)
* **Sprecher:** **Robert Ortmann**
* **Worauf du zeigst:** Auf die drei Problem- und Lösungsblöcke.
* **Was du sagst:**
  > „Natürlich lief in den drei Tagen nicht alles auf Knopfdruck. Zwei echte Herausforderungen: 
  > Erstens: Paketkonflikte auf Ubuntu 26.04. Unsere Lösung war der offizielle Docker-Container – damit läuft Checkmk komplett isoliert, stabil und startet bei jedem Booten automatisch. 
  > Zweitens: MariaDB lauschte standardmäßig nur auf 127.0.0.1. Wir haben das Bind-Address-Setting angepasst, damit die Datenbank über das Netzwerk überwacht werden kann. 
  > Unsere wichtigste Lesson Learned: Eine saubere Netzwerkplanung vorab spart hintenraus Stunden an Fehlersuche. 
  > Ich übergebe zurück an Jan für das Gesamtergebnis und den Rollout-Plan.“

---

### Folie 14: Projektergebnis & Zielerreichung (Minute 13:45 – 14:15)
* **Sprecher:** **Jan Kluth**
* **Worauf du zeigst:** Auf die KPI-Kacheln: 11/11 MUSS, 13/13 Abnahmetests bestanden.
* **Was du sagst:**
  > „Fassen wir das Gesamtergebnis zusammen: 
  > Alle 11 Muss-Anforderungen sind zu 100 % erfüllt. 
  > Drei zusätzliche Kann-Anforderungen wurden implementiert. 
  > Alle vier Störungstests wurden erfolgreich bestanden. 
  > Und im strukturierten Abnahmetest haben wir 13 von 13 Testfällen auf 'PASSED' gesetzt. 
  > Mit 41,5 Arbeitsstunden lagen wir nur knapp 6 % über dem Plan – der Proof of Concept ist damit auf ganzer Linie gelungen.“

---

### Folie 15: Empfehlung & Rollout-Fahrplan (Minute 14:15 – 14:45)
* **Sprecher:** **Jan Kluth**
* **Worauf du zeigst:** Auf die drei Phasen (Pilotbetrieb, Rollout, SNMP).
* **Was du sagst:**
  > „Unsere klare Handlungsempfehlung an die Geschäftsführung der Müller & Partner GmbH lautet daher: Checkmk Raw Edition sollte fest in den Produktivbetrieb übernommen werden. 
  > Wir empfehlen einen 3-Phasen-Rollout: 
  > Phase 1 in den ersten zwei Wochen: Ein dedizierter Server für Checkmk und die Anbindung der 10 kritischsten Kernserver. 
  > Phase 2 im ersten Monat: Kompletter Rollout auf alle Clients und NAS-Systeme plus E-Mail-Alarmierungsketten. 
  > Phase 3: SNMP-Überwachung der Switche und historische Kapazitätsplanung.“

---

### Folie 16: Abschluss & Übergang zur Live-Demo (Minute 14:45 – 15:00)
* **Sprecher:** **Alle gemeinsam**
* **Worauf du zeigst:** Auf die Live-Zugangsdaten in der Mitte der Folie.
* **Was du sagst:**
  > „Damit sind wir am Ende unseres Vortrags angekommen. Die Monitoring-Instanz läuft aktuell live auf unserem System – wir können Ihnen das Dashboard, die Host-Zustände und auf Wunsch auch gerne einen Live-Störungstest direkt vorführen. 
  > Vielen Dank für Ihre Aufmerksamkeit – wir freuen uns auf Ihre Fragen!“

---

## 💡 Typische Prüfungsfragen & Souveräne Antworten

1. **Frage: „Warum haben Sie Checkmk als Docker-Container und nicht direkt auf dem Host installiert?“**  
   *Antwort (Jan / Marco):* „Ubuntu 26.04 nutzt bereits neuere Bibliotheken wie Perl 5.40, für die ältere Checkmk-Pakete Abhängigkeitskonflikte hatten. Durch den offiziellen Docker-Container von Checkmk ist die gesamte OMD-Laufzeitumgebung vollkommen isoliert, reproduzierbar und unabhängig vom Host-Betriebssystem. Zudem startet der Container dank `--restart always` automatisch mit der VM.“

2. **Frage: „Wie skaliert Checkmk, wenn Müller & Partner auf 500 Systeme wächst?“**  
   *Antwort (Mathias / Marion):* „Checkmk Raw nutzt den extrem schnellen Livestatus-Kern und ein ressourcenschonendes Pull-Verfahren über TCP-Port 6556. Selbst auf Standardhardware verwaltet Checkmk tausende Services problemlos. Sollte die Firma weiter wachsen, gibt es einen nahtlosen Upgrade-Pfad auf die Checkmk Enterprise Edition mit dem hauseigenen Micro Core (CMC).“

3. **Frage: „Warum haben Sie für den TCP-Check ein eigenes Python-Skript geschrieben?“**  
   *Antwort (Marco / Robert):* „Gemäß Muss-Kriterium M09 sollte die Erweiterbarkeit bewiesen werden. Mit Python und dem Checkmk-Local-Check-Format konnten wir in unter 25 Zeilen Code ein performantes Tool bauen, das die Metriken direkt an die RRD-Graph-Engine übergibt – ganz ohne komplexe Compiler oder Plugins.“
