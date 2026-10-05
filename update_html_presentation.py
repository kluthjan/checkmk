import re

path = r"C:\Users\erolt\Desktop\monitor\Nutzwertanalyse_Praesentation.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Header Buttons
old_header_btn = '''      <button onclick="toggleOverview()" title="Folienübersicht (O)" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700/60 transition flex items-center gap-1.5">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
        <span class="hidden sm:inline">Übersicht (O)</span>
      </button>'''

new_header_btn = '''      <button onclick="toggleNotes()" title="Sprechernotizen / Gesprächsleitfaden (N)" class="px-2.5 py-1.5 rounded-lg bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-400 border border-emerald-500/40 transition flex items-center gap-1.5 font-semibold">
        <span>🎙️ Notizen (N)</span>
      </button>

      <button onclick="window.print()" title="Als PDF exportieren / Drucken" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700/60 transition hidden sm:flex items-center gap-1.5">
        <span>🖨️ PDF</span>
      </button>

      <button onclick="toggleOverview()" title="Folienübersicht (O)" class="px-2.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 border border-slate-700/60 transition flex items-center gap-1.5">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
        <span class="hidden sm:inline">Übersicht (O)</span>
      </button>'''

if old_header_btn in content:
    content = content.replace(old_header_btn, new_header_btn)
    print("Header buttons replaced.")
else:
    print("Warning: old_header_btn not found directly, trying normalized whitespace...")
    content = re.sub(r'<button onclick="toggleOverview\(\)".*?<\/button>', new_header_btn, content, count=1, flags=re.DOTALL)

# 2. Add Floating Speaker Notes Drawer before </main>
notes_drawer_html = '''
    <!-- FLOATING SPEAKER NOTES DRAWER -->
    <div id="speaker-notes-drawer" class="fixed bottom-14 left-4 right-4 max-w-4xl mx-auto glass-card rounded-2xl p-5 border border-emerald-500/40 shadow-2xl z-40 hidden transition-all duration-300">
      <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800 text-xs font-semibold">
        <div class="flex items-center gap-2 text-emerald-400">
          <span>🎙️ Gesprächsleitfaden &amp; Sprechernotizen</span>
          <span id="notes-timer-badge" class="px-2 py-0.5 rounded bg-emerald-500/10 text-[10px] font-mono border border-emerald-500/20">0:00 - 0:45 Min.</span>
        </div>
        <button onclick="toggleNotes()" class="text-slate-400 hover:text-white text-xs">✕ Schließen (N)</button>
      </div>
      <div id="notes-content" class="text-xs text-slate-200 leading-relaxed max-h-40 overflow-y-auto whitespace-pre-line font-sans">
      </div>
    </div>
'''

if '<!-- FLOATING SPEAKER NOTES DRAWER -->' not in content:
    content = content.replace('</main>', notes_drawer_html + '\n  </main>')
    print("Speaker notes drawer added.")

# 3. Add Notes Data and JS logic
js_additions = '''
    // ==========================================
    // SPEAKER NOTES DATA (10–15 MIN. LEITFADEN)
    // ==========================================
    const speakerNotes = [
      {
        timer: "0:00 - 0:45 Min. | Sprecher 1",
        text: "Guten Tag zusammen und herzlich willkommen zu unserer Projektpräsentation. Mein Name ist [Name] und zusammen mit meinem Team stellen wir Ihnen heute unser Abschlussprojekt vor: Die Einführung eines zentralen IT-Monitorings für die Müller & Partner GmbH.\\n\\nZiel unseres 3-tägigen PoC war es, nachzuweisen, dass eine moderne Open-Source-Monitoringlösung Ausfälle proaktiv verhindern kann. Wir haben alle 11 Muss-Kriterien zu 100% erfüllt und als Testsieger die Checkmk Raw Edition erfolgreich implementiert."
      },
      {
        timer: "0:45 - 2:00 Min. | Sprecher 1",
        text: "Schauen wir auf die Ausgangslage: Müller & Partner betreibt mehrere Server für Web, Dateiverwaltung und DNS/DHCP. Die Überwachung lief bisher rein manuell. Man erfuhr von Ausfällen erst, wenn verärgerte Mitarbeiter anriefen. Es gab unbemerkte DNS-Ausfälle und Festplatten liefen fast voll.\\n\\nDie Geschäftsführung forderte daher: Weg vom reaktiven Brandlöschen hin zu einem proaktiven Monitoring, das Störungen im Keim meldet, BEVOR der Anwender beeinträchtigt wird."
      },
      {
        timer: "2:00 - 3:15 Min. | Sprecher 1",
        text: "Vor der Umsetzung haben wir einen detaillierten Pflichtenkatalog aufgestellt: 11 verbindliche Muss-Kriterien (M01–M11) – von der Einrichtung des zentralen Servers über Multi-System-Monitoring bis hin zu Dienst-Überwachung und Störungstests.\\n\\nAlle 11 Kriterien haben wir zu 100% grün abgenommen. Zusätzlich konnten wir drei Kann-Anforderungen realisieren: Vorbereitete E-Mail-Alarmierung, erweiterte Dashboards und detaillierte Metriken im Custom Check."
      },
      {
        timer: "3:15 - 4:30 Min. | Sprecher 2",
        text: "Welche Software nimmt man für so ein Projekt? Wir haben uns auf die drei bekanntesten Open-Source-Lösungen konzentriert: Checkmk Raw, Zabbix und Nagios Core.\\n\\nAlle drei kosten null Euro Lizenzgebühr. Nagios ist extrem ressourcensparend, aber veraltet und rein textbasiert. Zabbix ist sehr mächtig, verlangt aber eine externe SQL-Datenbank und tagelange Einarbeitung. Checkmk punktet sofort mit seiner intuitiven WATO-Weboberfläche, automatischer Service-Erkennung und fertigen Dashboards."
      },
      {
        timer: "4:30 - 5:45 Min. | Sprecher 2",
        text: "Um die Entscheidung nachvollziehbar zu belegen, haben wir eine klassische Nutzwertanalyse nach DIN durchgeführt. Wir haben sieben Kriterien gewichtet. Das wichtigste Kriterium mit 20% war die Bedienbarkeit, gefolgt von Visualisierung, Alarmierung und Netzwerkdiensten mit je 15%.\\n\\nDas Gesamtergebnis ist eindeutig: Checkmk holt mit 4,40 Punkten den 1. Platz. Zabbix folgt mit 4,20 Punkten auf Platz 2, und Nagios fällt mit 3,30 Punkten deutlich zurück."
      },
      {
        timer: "5:45 - 6:45 Min. | Sprecher 2",
        text: "Warum hat Checkmk trotz der Stärken von Zabbix gewonnen? Zabbix holte in 3 Kriterien insgesamt +0,35 Punkte auf. ABER: Checkmk dominierte bei den beiden Kriterien mit dem höchsten Praxisnutzen: Bei der Bedienbarkeit holte Checkmk eine 5 und Zabbix nur eine 3 – das macht allein +0,40 Punkte Vorsprung! Und bei den Dashboards kamen nochmal +0,15 Punkte dazu.\\n\\n+0,55 Vorsprung minus +0,35 Aufholjagd = Ein klarer Gesamtsieg von +0,20 Punkten für Checkmk!"
      },
      {
        timer: "6:45 - 8:00 Min. | Sprecher 2",
        text: "Kommen wir zur Praxis: Wir haben in VirtualBox ein isoliertes Host-Only-Netzwerk im Subnetz 192.168.56.0/24 aufgebaut. Der Verbund besteht aus drei Systemen:\\n1. mon-srv01 (.101): Checkmk im Docker-Container, port-gemappt auf 8080.\\n2. web-srv01 (.102): Unser überwachter Webserver mit Apache2, MariaDB und OpenSSH.\\n3. win-client01 (.1): Der Windows-Host-PC mit dem nativen Windows-Agenten.\\n\\nDas Prinzip: Der Server pollt minütlich Port 6556 der Clients und holt alle Sensordaten ab."
      },
      {
        timer: "8:00 - 9:30 Min. | Sprecher 3",
        text: "Eine besondere Prüfungsanforderung war M09: Die Eigenentwicklung eines Messwert-Skripts. Wir haben in Python 3 ein Plugin geschrieben: active_tcp_connections.py. Es liest über 'ss' alle aktiven TCP-Verbindungen im Zustand ESTABLISHED aus.\\n\\nDas Geniale an Checkmk ist das Local-Check-Format: Das Skript gibt den Statuscode (0=OK, 1=WARN, 2=CRIT), den Namen, die Metrik und Text aus. Ab 100 Verbindungen gibt es eine Warnung, ab 200 wird es kritisch. Checkmk generiert daraus automatisch historische RRD-Graphen im Dashboard!"
      },
      {
        timer: "9:30 - 11:00 Min. | Sprecher 3",
        text: "Ein Monitoring ist nur so gut, wie es im Ernstfall reagiert. Wir haben vier reale Störungen provoziert:\\n1. Apache gestoppt: Nach 47 Sekunden meldete das Dashboard CRIT – Connection refused.\\n2. CPU-Stresstest auf 4 Kernen: Nach 62s Warnung, nach 75s CRIT bei 98% Last.\\n3. Festplatte vollgeschrieben: Nach 60 Sekunden Alarm bei über 95% Füllstand.\\n4. Host-Crash (VM aus): Nach 127 Sekunden meldete Checkmk 'Host DOWN, PING failed'.\\n\\n100% Erkennung in unter zwei Minuten, und nach Behebung sprangen alle Checks ohne manuellen Eingriff wieder auf Grün!"
      },
      {
        timer: "11:00 - 12:30 Min. | Alle Sprecher",
        text: "Unser Fazit: Der Proof of Concept hat alle Anforderungen zu 100% erfüllt. Checkmk Raw Edition sollte fest in den Produktivbetrieb übernommen werden.\\n\\nWir empfehlen einen 3-Phasen-Rollout: Phase 1: Pilotbetrieb der 10 Kernserver; Phase 2: Vollständiger Rollout auf Clients & E-Mail-Alarmierung; Phase 3: SNMP-Switche und historische Kapazitätsplanung.\\n\\nDie Instanz läuft aktuell live – wir können Ihnen das Dashboard jetzt vorführen. Vielen Dank!"
      }
    ];

    let notesVisible = false;
    function toggleNotes() {
      notesVisible = !notesVisible;
      const drawer = document.getElementById('speaker-notes-drawer');
      if (drawer) {
        drawer.classList.toggle('hidden', !notesVisible);
      }
      updateNotesContent();
    }

    function updateNotesContent() {
      const idx = currentSlide - 1;
      const note = speakerNotes[idx] || { timer: "", text: "" };
      const tb = document.getElementById('notes-timer-badge');
      const tc = document.getElementById('notes-content');
      if (tb) tb.textContent = note.timer;
      if (tc) tc.textContent = note.text;
    }
'''

# Update updatePresentation to refresh notes
content = content.replace("updatePresentation();", "updateNotesContent(); updatePresentation();")

# Add N and P keyboard handler
old_keys = "if (e.key === 'f' || e.key === 'F') {"
new_keys = """if (e.key === 'n' || e.key === 'N') {
        toggleNotes();
      } else if (e.key === 'p' || e.key === 'P') {
        window.print();
      } else if (e.key === 'f' || e.key === 'F') {"""

content = content.replace(old_keys, new_keys)

# Insert the JS additions before </script>
content = content.replace("</script>", js_additions + "\n  </script>")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

# Also copy to uw2
with open(r"C:\Users\erolt\Desktop\uw2\Nutzwertanalyse_Praesentation.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Nutzwertanalyse_Praesentation.html updated with interactive speaker notes drawer!")
