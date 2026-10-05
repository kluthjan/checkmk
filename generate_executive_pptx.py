import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6] # Blank slide

    # Color Palette
    BG_COLOR = RGBColor(11, 17, 32)       # Slate 950
    CARD_BG = RGBColor(30, 41, 59)        # Slate 800
    CARD_BORDER = RGBColor(51, 65, 85)    # Slate 700
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)  # Slate 400
    ACCENT_GREEN = RGBColor(16, 185, 129) # Emerald 500
    ACCENT_BLUE = RGBColor(59, 130, 246)  # Blue 500
    ACCENT_ROSE = RGBColor(244, 63, 94)   # Rose 500
    ACCENT_AMBER = RGBColor(245, 158, 11) # Amber 500

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, chapter_tag, title_text, subtitle_text):
        # Chapter badge
        tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.3))
        p_tag = tb_tag.text_frame.paragraphs[0]
        p_tag.text = chapter_tag.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_GREEN

        # Title
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.65), Inches(11.7), Inches(0.6))
        p_title = tb_title.text_frame.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

        # Subtitle
        if subtitle_text:
            tb_sub = slide.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(11.7), Inches(0.4))
            p_sub = tb_sub.text_frame.paragraphs[0]
            p_sub.text = subtitle_text
            p_sub.font.size = Pt(12)
            p_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    def set_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # ==========================================
    # SLIDE 1: TITELFOLIE
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    add_background(s1)

    # Pill badge
    badge = add_card(s1, Inches(0.8), Inches(1.2), Inches(3.2), Inches(0.4), RGBColor(16, 185, 129), RGBColor(16, 185, 129))
    badge.fill.transparency = 0.8
    p = badge.text_frame.paragraphs[0]
    p.text = "PROOF OF CONCEPT • 3 PROJEKTTAGE"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_main = s1.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(1.8))
    tf_main = tb_main.text_frame
    tf_main.word_wrap = True
    p1 = tf_main.paragraphs[0]
    p1.text = "Einführung eines zentralen"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p2 = tf_main.add_paragraph()
    p2.text = "IT-Monitorings mit Checkmk"
    p2.font.size = Pt(40)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_GREEN

    # Subtitle
    tb_sub = s1.shapes.add_textbox(Inches(0.8), Inches(3.7), Inches(11.7), Inches(0.6))
    p_sub = tb_sub.text_frame.paragraphs[0]
    p_sub.text = "Systematische Evaluation, Nutzwertanalyse und prototypische Implementierung für die Müller & Partner GmbH"
    p_sub.font.size = Pt(15)
    p_sub.font.color.rgb = TEXT_MUTED

    # 4 Metadata Cards
    cards_data = [
        ("Auftraggeber", "Müller & Partner GmbH", "Wachsende IT-Infrastruktur"),
        ("Auftragnehmer", "Grone Umschulungsteam", "Fachinformatiker SI"),
        ("Zielerreichung", "11/11 MUSS erfüllt", "100 % Erfolgsquote"),
        ("Systemauswahl", "Checkmk Raw Edition 2.3", "Rang 1 (4,40 Punkte)")
    ]
    for i, (title, val, desc) in enumerate(cards_data):
        c = add_card(s1, Inches(0.8 + i * 2.95), Inches(4.8), Inches(2.8), Inches(1.8))
        tf = c.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title.upper()
        p_t.font.size = Pt(10)
        p_t.font.color.rgb = TEXT_MUTED
        p_v = tf.add_paragraph()
        p_v.text = val
        p_v.font.size = Pt(13)
        p_v.font.bold = True
        p_v.font.color.rgb = ACCENT_GREEN if i >= 2 else TEXT_WHITE
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_MUTED

    set_notes(s1, """[ZEIT: 0:00 - 0:45 Min. | SPRECHER 1]
Guten Tag zusammen und herzlich willkommen zu unserer Präsentation. 
Mein Name ist [Name] und zusammen mit meinem Team stellen wir Ihnen heute unser Abschlussprojekt vor: Die Einführung eines zentralen IT-Monitorings für die Müller & Partner GmbH.

Ziel unseres Projekts war es, innerhalb einer 3-tägigen PoC-Phase nachzuweisen, dass eine moderne Open-Source-Monitoringlösung unbemerkte Server- und Dienstausfälle proaktiv verhindern kann. 

Wir haben alle 11 Muss-Kriterien zu 100% erfüllt und als Testsieger die Checkmk Raw Edition in einem 3-System-Testnetz erfolgreich implementiert.""")

    # ==========================================
    # SLIDE 2: AGENDA
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_background(s2)
    add_header(s2, "Übersicht", "Agenda der Präsentation", "Strukturierter Ablauf in 4 Kernabschnitten (15 Minuten)")

    agenda_items = [
        ("01", "Ausgangslage & Anforderungen", "Manuelle Überwachung, typische Vorfälle & der verbindliche MUSS-Katalog (M01–M11)"),
        ("02", "Evaluation & Nutzwertanalyse", "Vergleich von Checkmk, Zabbix und Nagios Core nach gewichteter DIN-Matrix"),
        ("03", "Technische Implementierung", "VirtualBox Testnetz, Checkmk Server, Dienst-Checks & Custom Python Check"),
        ("04", "Validierung & Rollout-Empfehlung", "4 Störungssimulationen, Datenanalyse der Schwellwerte & 3-Phasen-Fahrplan")
    ]
    for i, (num, title, desc) in enumerate(agenda_items):
        c = add_card(s2, Inches(0.8), Inches(1.8 + i * 1.3), Inches(11.7), Inches(1.15))
        tf = c.text_frame
        tf.word_wrap = True
        p_n = tf.paragraphs[0]
        p_n.text = f"{num}   {title}"
        p_n.font.size = Pt(16)
        p_n.font.bold = True
        p_n.font.color.rgb = ACCENT_GREEN
        p_d = tf.add_paragraph()
        p_d.text = f"      {desc}"
        p_d.font.size = Pt(11)
        p_d.font.color.rgb = TEXT_MUTED

    set_notes(s2, """[ZEIT: 0:45 - 1:15 Min. | SPRECHER 1]
Wir haben unseren Vortrag in vier logische Blöcke aufgeteilt:
Zuerst zeigen wir kurz die Ausgangslage bei Müller & Partner und die definierten Anforderungen.
Danach erläutern wir die Systemauswahl anhand unserer Nutzwertanalyse.
Im dritten Teil steigen wir direkt in die Technik ein: Testnetzwerk, Dienst-Überwachung und unser eigenes Python-Plugin.
Und zum Schluss präsentieren wir die Ergebnisse der 4 Störungstests sowie die Empfehlung an die Geschäftsführung.""")

    # ==========================================
    # SLIDE 3: AUSGANGSSITUATION
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_background(s3)
    add_header(s3, "Kapitel 01", "Ausgangslage & Problemstellung", "Warum die manuelle Überwachung ein untragbares Risiko für das Unternehmen war")

    c_prob = add_card(s3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0), CARD_BG, ACCENT_ROSE)
    tf_p = c_prob.text_frame
    tf_p.word_wrap = True
    p = tf_p.paragraphs[0]
    p.text = "⚠️ Das bisherige Problem: Manuelle Kontrolle"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_ROSE

    prob_bullets = [
        "Wachsende IT-Infrastruktur: Mehrere Linux-Server für Web, Dateiverwaltung und DNS/DHCP.",
        "Reaktives Handeln: Admins erfuhren von Ausfällen erst, wenn verärgerte Anwender anriefen.",
        "Unbemerkte DNS/DHCP-Ausfälle: Verbindungsprobleme legten Arbeitsplätze lahm.",
        "Drohender Datenverlust: Unbemerkte Festplattenengpässe brachten Systeme an den Rand des Crashs.",
        "Performance-Verluste: Quälend langsame Antwortzeiten blieben undokumentiert."
    ]
    for b in prob_bullets:
        pb = tf_p.add_paragraph()
        pb.text = "• " + b
        pb.font.size = Pt(11)
        pb.font.color.rgb = TEXT_WHITE

    c_sol = add_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), CARD_BG, ACCENT_GREEN)
    tf_s = c_sol.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "🎯 Das Projektziel: Proaktives Monitoring"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    sol_bullets = [
        "Proaktive Erkennung: Störungen erkennen und beheben, BEVOR Endanwender betroffen sind.",
        "Zentrales Web-Dashboard: Gesamter Zustand aller Hosts und Dienste auf einen Blick.",
        "Automatisierte Alarmierung: Sofortige Benachrichtigung bei Schwellwert-Überschreitung.",
        "100 % Open Source: Vermeidung teurer Lizenzkosten durch etablierte Enterprise-Standards.",
        "Proof of Concept in 3 Tagen: Voll funktionsfähige Testumgebung zum Praxisnachweis."
    ]
    for b in sol_bullets:
        pb = tf_s.add_paragraph()
        pb.text = "✓ " + b
        pb.font.size = Pt(11)
        pb.font.color.rgb = TEXT_WHITE

    set_notes(s3, """[ZEIT: 1:15 - 2:30 Min. | SPRECHER 1]
Schauen wir auf die Ausgangslage: Müller & Partner ist kontinuierlich gewachsen. Mehrere Server, Linux-Maschinen für Webdienste, Dateiserver und DNS/DHCP.
Das Problem: Die Überwachung erfolgte rein manuell. 
Im Klartext hieß das: Man erfuhr von Ausfällen erst, wenn Mitarbeiter anriefen. Es gab unbemerkte DNS-Ausfälle und Festplatten liefen fast voll. 
Die Geschäftsführung hat daher völlig zu Recht gefordert: Wir müssen weg vom reaktiven Brandlöschen hin zu einem proaktiven Monitoring, das Störungen im Keim meldet.""")

    # ==========================================
    # SLIDE 4: ANFORDERUNGSANALYSE
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_background(s4)
    add_header(s4, "Kapitel 02", "Anforderungsanalyse (Abgabeprodukt A)", "11 verbindliche MUSS-Anforderungen zu 100 % erfüllt + 3 KANN-Features umgesetzt")

    muss_items = [
        ("M01", "Zentrales Monitoring", "Einrichtung einer zentralen Überwachungsinstanz"),
        ("M02", "Multi-System-Setup", "Einbindung von mind. 2 Testsystemen (Linux & Windows)"),
        ("M03", "Erreichbarkeit", "Erkennung der Erreichbarkeit via ICMP-Ping"),
        ("M04", "Systemressourcen", "Überwachung von CPU, RAM und Festplattenbelegung"),
        ("M05", "Netzwerkdienste", "Aktive Überwachung von HTTP, SSH und MySQL"),
        ("M06", "Schwellwerte", "Definition fundierter Warn- und Fehlergrenzen"),
        ("M07", "Alarmierung", "Automatische Erkennung & Visualisierung kritischer Zustände"),
        ("M08", "Dashboard", "Zentrale Übersicht des Gesamtzustands der Infrastruktur"),
        ("M09", "Custom Check", "Entwicklung und Integration eines eigenen Messwert-Skripts"),
        ("M10", "Störungssimulation", "Gezielte Auslösung & Validierung von 4 Störungen"),
        ("M11", "Abnahmetest", "Strukturierter Durchlauf & Protokoll aller Testfälle (13/13)")
    ]

    for idx, (mid, mtitle, mdesc) in enumerate(muss_items):
        col = idx % 2
        row = idx // 2
        c = add_card(s4, Inches(0.8 + col * 5.95), Inches(1.8 + row * 0.85), Inches(5.8), Inches(0.75))
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{mid}: {mtitle}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p2 = tf.add_paragraph()
        p2.text = f"{mdesc}  [STATUS: ERFÜLLT ✓]"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED

    # KANN Box
    c_kann = add_card(s4, Inches(0.8 + 1 * 5.95), Inches(1.8 + 5 * 0.85), Inches(5.8), Inches(0.75), CARD_BG, ACCENT_BLUE)
    tf_k = c_kann.text_frame
    tf_k.word_wrap = True
    p = tf_k.paragraphs[0]
    p.text = "K01, K02, K04: KANN-Anforderungen (3 von 5 umgesetzt)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p2 = tf_k.add_paragraph()
    p2.text = "E-Mail-Alarmierung vorbereitet, erweiterte Dashboards & Custom Check [ERFÜLLT ✓]"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED

    set_notes(s4, """[ZEIT: 2:30 - 3:30 Min. | SPRECHER 1]
Vor der Umsetzung haben wir einen detaillierten Pflichtenkatalog aufgestellt.
Es gab 11 verbindliche Muss-Kriterien – von der Einrichtung des zentralen Servers über Multi-System-Monitoring bis hin zu Dienst-Überwachung und Störungstests.
Wie Sie in der Übersicht sehen: Wir haben alle 11 Kriterien zu 100% grün abgenommen.
Zusätzlich konnten wir drei Kann-Anforderungen realisieren: Vorbereitete E-Mail-Alarmierung, erweiterte Dashboards und detaillierte Metriken im Custom Check.""")

    # ==========================================
    # SLIDE 5: DIE 3 KANDIDATEN
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_background(s5)
    add_header(s5, "Kapitel 03", "Die 3 Kandidaten im Systemvergleich", "Marktanalyse führender Open-Source-Monitoring-Lösungen für den 3-Tage-PoC")

    tools = [
        ("Checkmk Raw Edition 2.3", "TESTSIEGER 🏆", ACCENT_GREEN, [
            "Typ: Open Source (GPLv2)",
            "Web-GUI: Sehr intuitiv & modern (WATO)",
            "Discovery: Automatische Service-Erkennung",
            "Agent: Schlanker nativer Agent (Linux/Win)",
            "Dashboards: Fertig out-of-the-box",
            "Setup: Schnellster Time-to-Value",
            "Keine externe Datenbank nötig"
        ]),
        ("Zabbix 7.0 LTS", "RANG 2 (SEHR LEISTUNGSFÄHIG)", ACCENT_BLUE, [
            "Typ: Open Source (GPLv2)",
            "Web-GUI: Leistungsstark, aber komplex",
            "Flexibilität: Sehr mächtige Template-Engine",
            "Skalierbarkeit: Exzellent für Großkonzerne",
            "Nachteil: Externe SQL-DB zwingend nötig",
            "Nachteil: Hohe Einarbeitungszeit",
            "Zu komplex für 3 Projekttage"
        ]),
        ("Nagios Core 4.5", "RANG 3 (KLASSISCHER STANDARD)", TEXT_MUTED, [
            "Typ: Open Source (GPLv2)",
            "Ressourcen: Extrem sparsam",
            "Historisch: Bewährter Industriestandard",
            "Nachteil: Veraltete Weboberfläche",
            "Nachteil: Rein dateibasierte Konfiguration",
            "Nachteil: Keine integrierten Dashboards",
            "Für moderne Admins nicht mehr zeitgemäß"
        ])
    ]

    for i, (name, badge, color, points) in enumerate(tools):
        c = add_card(s5, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(5.0), CARD_BG, color)
        tf = c.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = name
        p_t.font.size = Pt(14)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_b = tf.add_paragraph()
        p_b.text = badge
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = color
        for pt in points:
            p_p = tf.add_paragraph()
            p_p.text = "• " + pt
            p_p.font.size = Pt(10.5)
            p_p.font.color.rgb = TEXT_MUTED

    set_notes(s5, """[ZEIT: 3:30 - 4:30 Min. | SPRECHER 2]
Welche Software nimmt man für so ein Projekt? Wir haben uns auf die drei bekanntesten Open-Source-Lösungen konzentriert: Checkmk Raw, Zabbix und Nagios Core.
Alle drei kosten null Euro Lizenzgebühr, aber sie unterscheiden sich massiv in der Philosophie:
Nagios ist der Urvater – extrem sparsam, aber rein textbasiert und ohne moderne Dashboards.
Zabbix ist extrem mächtig und skalierbar, erfordert aber eine externe SQL-Datenbank und tagelange Einarbeitung.
Checkmk punktet sofort mit seiner intuitiven WATO-Weboberfläche, der automatischen Service-Erkennung und fertigen Dashboards.""")

    # ==========================================
    # SLIDE 6: NUTZWERTANALYSE MATRIX
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_background(s6)
    add_header(s6, "Kapitel 04", "Nutzwertanalyse & Entscheidungsmatrix", "Strukturierte Bewertung nach gewichteten Kriterien (Skala 1 bis 5)")

    # Table Card
    c_tbl = add_card(s6, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf_tbl = c_tbl.text_frame
    tf_tbl.word_wrap = True

    matrix_lines = [
        ("Kriterium", "Gewicht", "Checkmk Raw", "Zabbix", "Nagios Core"),
        ("1. Kosten / Lizenz", "10 %", "5 / 0,50", "5 / 0,50", "5 / 0,50"),
        ("2. Bedienbarkeit & GUI (Ausschlaggebend)", "20 %", "5 / 1,00  🏆", "3 / 0,60", "2 / 0,40"),
        ("3. OS-Unterstützung", "10 %", "4 / 0,40", "5 / 0,50", "4 / 0,40"),
        ("4. Netzwerkdienste", "15 %", "4 / 0,60", "5 / 0,75", "4 / 0,60"),
        ("5. Alarmierung", "15 %", "4 / 0,60", "4 / 0,60", "3 / 0,45"),
        ("6. Visualisierung / Dashboards (Ausschlaggebend)", "15 %", "5 / 0,75  🏆", "4 / 0,60", "2 / 0,30"),
        ("7. Erweiterbarkeit & Doku", "15 %", "4 / 0,55", "5 / 0,65", "4 / 0,60"),
        ("GESAMTERGEBNIS (PUNKTE / RANG)", "100 %", "4,40 (RANG 1) 🏆", "4,20 (RANG 2)", "3,30 (RANG 3)")
    ]

    p_header = tf_tbl.paragraphs[0]
    p_header.text = f"{matrix_lines[0][0]:<45} {matrix_lines[0][1]:<10} {matrix_lines[0][2]:<18} {matrix_lines[0][3]:<15} {matrix_lines[0][4]}"
    p_header.font.size = Pt(11)
    p_header.font.bold = True
    p_header.font.color.rgb = ACCENT_GREEN

    for row in matrix_lines[1:]:
        p_r = tf_tbl.add_paragraph()
        p_r.text = f"{row[0]:<45} {row[1]:<10} {row[2]:<18} {row[3]:<15} {row[4]}"
        p_r.font.size = Pt(10.5)
        if "GESAMTERGEBNIS" in row[0]:
            p_r.font.bold = True
            p_r.font.size = Pt(12)
            p_r.font.color.rgb = TEXT_WHITE
        elif "Ausschlaggebend" in row[0]:
            p_r.font.bold = True
            p_r.font.color.rgb = ACCENT_GREEN
        else:
            p_r.font.color.rgb = TEXT_MUTED

    set_notes(s6, """[ZEIT: 4:30 - 5:45 Min. | SPRECHER 2]
Um die Entscheidung nachvollziehbar zu belegen, haben wir eine klassische Nutzwertanalyse durchgeführt.
Wir haben sieben Kriterien gewichtet. 
Das wichtigste Kriterium mit 20% war die Bedienbarkeit, gefolgt von Visualisierung, Alarmierung und Netzwerkdiensten mit je 15%.
Jedes System wurde von 1 bis 5 bewertet und mit der Gewichtung multipliziert.
Das Gesamtergebnis ist eindeutig:
Checkmk holt mit 4,40 Punkten den 1. Platz.
Zabbix folgt mit 4,20 Punkten auf Platz 2.
Nagios fällt mit 3,30 Punkten deutlich zurück.""")

    # ==========================================
    # SLIDE 7: WARUM CHECKMK?
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_background(s7)
    add_header(s7, "Kapitel 05", "Warum Checkmk gewonnen hat: Der Gamechanger", "Detailanalyse des Punkteabstands zwischen Checkmk (4,40) und Zabbix (4,20)")

    c_left = add_card(s7, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0), CARD_BG, ACCENT_GREEN)
    tf_l = c_left.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "🏆 Wo Checkmk siegte: +0,55 Punkte Vorsprung"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    pts_l = [
        "Bedienbarkeit & GUI (20 % Gewicht):",
        "  • Checkmk holte die Bestnote 5 / 5 (1,00 Nutzwert)",
        "  • Zabbix erhielt nur 3 / 5 (0,60 Nutzwert)",
        "  ➔ Allein hier: +0,40 Punkte Vorsprung für Checkmk!",
        "",
        "Visualisierung & Dashboards (15 % Gewicht):",
        "  • Checkmk: 5 / 5 (0,75 Nutzwert) durch fertige Dashboards",
        "  • Zabbix: 4 / 5 (0,60 Nutzwert)",
        "  ➔ Weitere +0,15 Punkte Vorsprung für Checkmk!",
        "",
        "Fazit: In den beiden Kriterien mit dem höchsten Praxisnutzen für das Team war Checkmk unschlagbar."
    ]
    for pt in pts_l:
        p_pt = tf_l.add_paragraph()
        p_pt.text = pt
        p_pt.font.size = Pt(10.5)
        p_pt.font.color.rgb = TEXT_WHITE if "Vorsprung" in pt or "Fazit" in pt else TEXT_MUTED

    c_right = add_card(s7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), CARD_BG, ACCENT_BLUE)
    tf_r = c_right.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "⚖️ Wo Zabbix punktete: +0,35 Punkte Aufholjagd"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE

    pts_r = [
        "Zabbix war in 3 Kriterien überlegen:",
        "  • Netzwerkdienste (15 %): Zabbix 5 vs. Checkmk 4 ➔ +0,15",
        "  • Erweiterbarkeit (15 %): Zabbix 5 vs. Checkmk 4 ➔ +0,10",
        "  • OS-Support (10 %): Zabbix 5 vs. Checkmk 4 ➔ +0,10",
        "",
        "Warum es trotzdem nicht für den Sieg reichte:",
        "  • Zabbix sammelte in diesen 3 Kriterien insgesamt +0,35 Punkte.",
        "  • Checkmk holte aber allein bei Usability & Dashboards +0,55 Punkte!",
        "",
        "Differenz-Rechnung:",
        "  +0,55 (Checkmk) minus +0,35 (Zabbix) = +0,20 Punkte Gesamtsieg!"
    ]
    for pt in pts_r:
        p_pt = tf_r.add_paragraph()
        p_pt.text = pt
        p_pt.font.size = Pt(10.5)
        p_pt.font.color.rgb = TEXT_WHITE if "Gesamtsieg" in pt or "Differenz" in pt else TEXT_MUTED

    set_notes(s7, """[ZEIT: 5:45 - 6:45 Min. | SPRECHER 2]
Man könnte sich fragen: Zabbix war doch bei Netzwerkdiensten und Erweiterbarkeit extrem stark – warum hat Checkmk trotzdem gewonnen?
Genau das belegt diese Folie:
Zabbix punktete in 3 Kriterien und holte dort +0,35 Punkte auf.
ABER: Checkmk dominierte bei den beiden Kriterien mit dem höchsten Praxisnutzen:
Bei der Bedienbarkeit holte Checkmk eine 5 und Zabbix nur eine 3 – das macht allein +0,40 Punkte Vorsprung!
Bei den Dashboards kamen nochmal +0,15 Punkte dazu.
Macht zusammen +0,55 Punkte Vorsprung gegen +0,35 Punkte Aufholjagd von Zabbix = Ein klarer Gesamtsieg von +0,20 Punkten für Checkmk.""")

    # ==========================================
    # SLIDE 8: TESTNETZ & TOPOLOGIE
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_background(s8)
    add_header(s8, "Kapitel 06", "Testnetz-Architektur & Topologie", "Strukturiertes 3-System-Testnetz (VirtualBox Host-Only Subnetz 192.168.56.0/24)")

    topo_cards = [
        ("mon-srv01 (SERVER)", "192.168.56.101", ACCENT_GREEN, [
            "OS: Ubuntu 26.04 LTS VM",
            "Rolle: Checkmk Raw 2.3 Server",
            "Betrieb: Docker-Container (restart: always)",
            "Web-GUI: Port 80 (gemappt auf Host: 8080)",
            "Status: 24 Services aktiv überwacht"
        ]),
        ("web-srv01 (CLIENT LINUX)", "192.168.56.102", ACCENT_BLUE, [
            "OS: Geklonte Ubuntu VM (4 GB RAM)",
            "Dienste: Apache2 (HTTP 80), MariaDB (SQL 3306), SSH (22)",
            "Checkmk Agent: Port 6556 TCP aktiv",
            "Custom Check: Python TCP-Verbindungsüberwachung",
            "Ports: SSH 2223 / HTTP 8081"
        ]),
        ("win-client01 (CLIENT WIN)", "192.168.56.1", RGBColor(168, 85, 247), [
            "OS: Windows 10/11 Host-PC",
            "Agent: Checkmk Windows Agent (MSI)",
            "Dienst: Checkmk Service aktiv",
            "Firewall: Port 6556 freigegeben",
            "Überwacht: CPU, RAM, Festplatte C:"
        ])
    ]

    for i, (title, ip, color, details) in enumerate(topo_cards):
        c = add_card(s8, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(4.2), CARD_BG, color)
        tf = c.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = TEXT_WHITE
        p_ip = tf.add_paragraph()
        p_ip.text = f"IP: {ip}"
        p_ip.font.size = Pt(11)
        p_ip.font.bold = True
        p_ip.font.color.rgb = color
        for d in details:
            p_d = tf.add_paragraph()
            p_d.text = "• " + d
            p_d.font.size = Pt(10)
            p_d.font.color.rgb = TEXT_MUTED

    # Bottom Protocol Bar
    c_bot = add_card(s8, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.85))
    tf_b = c_bot.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "Kommunikationsprinzip (Pull-Monitoring):"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p2 = tf_b.add_paragraph()
    p2.text = "Checkmk Server pollt minütlich Port 6556 aller Zielsysteme ➔ Agent liefert Sensordaten ➔ Livestatus Core bewertet Schwellwerte ➔ Live-Dashboard aktualisiert."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = TEXT_MUTED

    set_notes(s8, """[ZEIT: 6:45 - 8:00 Min. | SPRECHER 2]
Kommen wir zur Praxis: Wir haben in VirtualBox ein isoliertes Host-Only-Netzwerk im Subnetz 192.168.56.0/24 aufgebaut.
Der Verbund besteht aus drei Systemen:
Erstens: Unser Monitoring-Server mon-srv01 auf IP .101. Hier läuft Checkmk im Docker-Container, port-gemappt auf Port 8080 für den Browser.
Zweitens: Unser überwachter Webserver web-srv01 auf IP .102 mit Apache2, MariaDB und OpenSSH.
Drittens: Der Windows-Host-PC auf IP .1 mit dem nativen Windows-Agenten.
Das Prinzip: Der Server pollt minütlich Port 6556 der Clients, holt alle Metriken ab und visualisiert sie im Dashboard.""")

    # ==========================================
    # SLIDE 9: UMGESETZTE ÜBERWACHUNG
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_background(s9)
    add_header(s9, "Kapitel 07", "Umgesetzte Dienst-Überwachung & Schwellwerte", "Aktive Überwachung von Anwendungsdiensten (M05) & definierte Grenzwerte (M06)")

    c_svc = add_card(s9, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf_s = c_svc.text_frame
    tf_s.word_wrap = True

    svc_rows = [
        ("Dienst / Ressource", "Überwachter Service", "Port", "Warnung (WARN)", "Kritisch (CRIT)", "Status"),
        ("Apache Webserver", "HTTP_Apache", "Port 80", "> 2,0 Sekunden", "> 5,0 s / Ausfall", "OK (200 OK) 🟢"),
        ("MariaDB Datenbank", "MySQL_Database", "Port 3306", "> 1,0 Sekunde", "> 3,0 s / Ausfall", "OK (Port 3306) 🟢"),
        ("Fernwartung", "SSH_Service", "Port 22", "Verzögerung > 1s", "Ausfall / Refused", "OK (Port 22) 🟢"),
        ("Custom Check", "Active_TCP_Connections", "-", "> 100 Verbindungen", "> 200 Verbindungen", "OK (1 Verb.) 🟢"),
        ("CPU-Auslastung", "CPU utilization", "-", "> 80 % (5 Min)", "> 95 % (5 Min)", "OK (3–7 %) 🟢"),
        ("Arbeitsspeicher", "Memory", "-", "> 85 % genutzt", "> 95 % genutzt", "OK (19 %) 🟢"),
        ("Festplatte", "Filesystem /", "-", "> 85 % belegt", "> 95 % belegt", "OK (37 %) 🟢")
    ]

    p_h = tf_s.paragraphs[0]
    p_h.text = f"{svc_rows[0][0]:<22} {svc_rows[0][1]:<24} {svc_rows[0][2]:<12} {svc_rows[0][3]:<20} {svc_rows[0][4]:<20} {svc_rows[0][5]}"
    p_h.font.size = Pt(11)
    p_h.font.bold = True
    p_h.font.color.rgb = ACCENT_GREEN

    for row in svc_rows[1:]:
        pr = tf_s.add_paragraph()
        pr.text = f"{row[0]:<22} {row[1]:<24} {row[2]:<12} {row[3]:<20} {row[4]:<20} {row[5]}"
        pr.font.size = Pt(10.5)
        pr.font.color.rgb = TEXT_WHITE if "🟢" in row[5] else TEXT_MUTED

    set_notes(s9, """[ZEIT: 8:00 - 9:00 Min. | SPRECHER 3]
Auf unserem Webserver web-srv01 haben wir alle geforderten Anwendungsdienste aktiv eingebunden:
Den Apache-Webserver überwachen wir auf Port 80. Die Antwortzeit ist gemäß Anforderung M06 belegt: Ab 2 Sekunden gibt es eine Warnung, ab 5 Sekunden oder bei Ausfall ist es kritisch.
Die MariaDB-Datenbank überwachen wir auf Port 3306, den SSH-Dienst auf Port 22.
Und zusätzlich erfasst der Agent kontinuierlich alle Systemmetriken: CPU-Auslastung, RAM, Festplattenbelegung und Netzwerkinterfaces.""")

    # ==========================================
    # SLIDE 10: EIGENENTWICKLUNG CUSTOM CHECK
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_background(s10)
    add_header(s10, "Kapitel 08", "Eigenentwicklung: Custom Local Check (M09)", "Entwicklung eines eigenständigen Python-Plugins zur TCP-Verbindungsanalyse")

    c_code = add_card(s10, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0), RGBColor(15, 23, 42), ACCENT_GREEN)
    tf_c = c_code.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "#!/usr/bin/env python3\n# Local Check: active_tcp_connections.py\nimport subprocess, sys\n\ndef get_tcp_connections():\n    out = subprocess.check_output(['ss', '-ant'], text=True)\n    count = sum(1 for line in out.splitlines() if 'ESTAB' in line)\n    \n    warn, crit = 100, 200\n    status = 0\n    status_txt = 'OK'\n    \n    if count >= crit:\n        status, status_txt = 2, 'CRIT'\n    elif count >= warn:\n        status, status_txt = 1, 'WARN'\n        \n    print(f'{status} \"Active_TCP_Connections\" '\n          f'connections={count};{warn};{crit} '\n          f'{status_txt} - {count} aktive TCP Verbindungen')\n\nif __name__ == '__main__':\n    get_tcp_connections()"
    p.font.size = Pt(9.5)
    p.font.color.rgb = TEXT_WHITE

    c_expl = add_card(s10, Inches(7.0), Inches(1.8), Inches(5.5), Inches(5.0), CARD_BG, CARD_BORDER)
    tf_e = c_expl.text_frame
    tf_e.word_wrap = True
    p = tf_e.paragraphs[0]
    p.text = "💡 Funktionsweise & Checkmk-Protokoll"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    pts_e = [
        "Standard-Pfad: /usr/lib/check_mk_agent/local/",
        "Protokoll-Format: <STATUS> \"<NAME>\" <METRIK> <TEXT>",
        "",
        "Status-Codes:",
        "  • 0 = OK (Normalbetrieb unter 100 Verbindungen)",
        "  • 1 = WARN (Erhöhte Last ab 100 Verbindungen)",
        "  • 2 = CRIT (Kritische Last / DoS-Verdacht ab 200)",
        "",
        "Besonderer Mehrwert:",
        "  • Durch das Mitliefern der Metrik 'connections=X;100;200' generiert Checkmk automatisch RRD-Performance-Graphen im Dashboard.",
        "  • Beweist die grenzenlose Erweiterbarkeit von Checkmk."
    ]
    for pt in pts_e:
        pe = tf_e.add_paragraph()
        pe.text = pt
        pe.font.size = Pt(10)
        pe.font.color.rgb = TEXT_WHITE if "Mehrwert" in pt or "Protokoll" in pt else TEXT_MUTED

    set_notes(s10, """[ZEIT: 9:00 - 10:15 Min. | SPRECHER 3]
Eine besondere Prüfungsanforderung war M09: Die Eigenentwicklung eines Messwert-Skripts.
Wir haben in Python 3 ein Plugin geschrieben, das auf dem Webserver liegt: active_tcp_connections.py.
Das Skript liest über das Tool 'ss' alle aktiven TCP-Verbindungen im Zustand ESTABLISHED aus.
Das Geniale an Checkmk ist das Local-Check-Format: Das Skript gibt einfach den Statuscode – 0 für OK, 1 für Warnung, 2 für Kritisch –, den Servicenamen, die Performance-Metrik und einen Klartext aus.
Übersteigt die Zahl 100, gibt es eine Warnung, ab 200 wird es kritisch. Checkmk übernimmt das vollautomatisch ins Dashboard und zeichnet sogar historische Graphen.""")

    # ==========================================
    # SLIDE 11: STÖRUNGSSIMULATION
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_background(s11)
    add_header(s11, "Kapitel 09", "Störungssimulation & Validierung (M10)", "4 reale Ausfallszenarien simuliert und Reaktionszeiten protokolliert")

    c_sim = add_card(s11, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf_sim = c_sim.text_frame
    tf_sim.word_wrap = True

    sim_rows = [
        ("#", "Szenario", "Auslösebefehl", "Erwartung", "Tatsächliche Erkennung", "Reaktionszeit"),
        ("1", "Apache Web-Ausfall", "sudo systemctl stop apache2", "HTTP ➔ CRIT", "CRIT (Connection refused)", "47 Sek. ⚡"),
        ("2", "CPU-Volllast", "stress --cpu 4 --timeout 180", "CPU ➔ WARN/CRIT", "WARN (62s) ➔ CRIT (75s)", "62 Sek. ⚡"),
        ("3", "Festplatte voll", "dd if=/dev/zero of=/tmp/file", "Disk ➔ CRIT", "CRIT (Belegung > 95%)", "60 Sek. ⚡"),
        ("4", "Host-Totalausfall", "VM Power Off (VirtualBox)", "Host ➔ DOWN", "DOWN (ICMP Ping Fail)", "127 Sek. ⚡")
    ]

    p_h = tf_sim.paragraphs[0]
    p_h.text = f"{sim_rows[0][0]:<3} {sim_rows[0][1]:<20} {sim_rows[0][2]:<30} {sim_rows[0][3]:<18} {sim_rows[0][4]:<26} {sim_rows[0][5]}"
    p_h.font.size = Pt(11)
    p_h.font.bold = True
    p_h.font.color.rgb = ACCENT_GREEN

    for row in sim_rows[1:]:
        pr = tf_sim.add_paragraph()
        pr.text = f"{row[0]:<3} {row[1]:<20} {row[2]:<30} {row[3]:<18} {row[4]:<26} {row[5]}"
        pr.font.size = Pt(10.5)
        pr.font.color.rgb = TEXT_WHITE

    p_summary = tf_sim.add_paragraph()
    p_summary.text = "\nFAZIT DER STÖRUNGSTESTS:\n• 100 % Erkennungsrate aller Ausfälle in durchschnittlich unter 65 Sekunden.\n• Automatische Entwarnung: Nach Behebung sprangen alle Checks ohne manuelles Zutun wieder auf OK (Grün) zurück."
    p_summary.font.size = Pt(10.5)
    p_summary.font.color.rgb = ACCENT_GREEN

    set_notes(s11, """[ZEIT: 10:15 - 11:30 Min. | SPRECHER 3]
Ein Monitoring ist nur so gut, wie es im Ernstfall reagiert. Deshalb haben wir vier reale Störungen provoziert:
Test 1: Apache gestoppt. Nach 47 Sekunden meldete das Dashboard CRIT – Connection refused.
Test 2: CPU-Stresstest auf 4 Kernen. Nach 62 Sekunden Warnung, nach 75 Sekunden CRIT bei 98% Last.
Test 3: Die Festplatte künstlich vollgeschrieben. Nach genau 60 Sekunden schlug der Alarm bei über 95% Füllstand an.
Test 4: Der harte Host-Crash – VM ausgeschaltet. Nach 127 Sekunden meldete Checkmk 'Host DOWN, PING failed'.
Fazit: 100% Trefferquote in unter 2 Minuten, und nach Behebung sprangen alle Checks ohne manuellen Eingriff wieder auf Grün.""")

    # ==========================================
    # SLIDE 12: DATENANALYSE
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_background(s12)
    add_header(s12, "Kapitel 10", "Datenanalyse & Schwellwert-Validierung (Abgabeprodukt I)", "Untersuchung der Messkurven und Bestätigung der praxistauglichen Grenzwerte")

    analyses = [
        ("Messgröße 1: CPU-Auslastung", ACCENT_GREEN, [
            "Normalbetrieb: 5 bis 15 % Grundlast.",
            "Störfall: Steiler vertikaler Anstieg auf 98–100 %.",
            "Validierung des Grenzwerts: Schwelle bei 80 % mit 5-Minuten-Zeitfenster filtert kurzzeitige Update-Spitzen zuverlässig heraus.",
            "Ergebnis: Kein Fehlalarm-Risiko, maximaler Schutz."
        ]),
        ("Messgröße 2: Festplattenbelegung", ACCENT_BLUE, [
            "Normalbetrieb: Flacher linearer Verlauf bei ca. 37 %.",
            "Störfall: Steiler Füllkurvenanstieg auf über 95 %.",
            "Validierung des Grenzwerts: Warnstufe bei 85 % lässt Admins mehrere Tage Reaktionszeit für Log-Bereinigungen.",
            "Ergebnis: Verhindert Datenverlust und Dienststillstand."
        ]),
        ("Messgröße 3: HTTP-Verfügbarkeit", RGBColor(168, 85, 247), [
            "Normalbetrieb: Stabile Antwortzeiten unter 15 ms (200 OK).",
            "Störfall: Sofortiger binärer Ausschlag auf Connection Refused.",
            "Validierung des Grenzwerts: Schwelle bei 2,0s (Warn) und 5,0s (Crit) schützt Kunden vor quälend langsamen Ladezeiten.",
            "Ergebnis: Essentiell für geschäftskritische Webdienste."
        ])
    ]

    for i, (title, color, bullets) in enumerate(analyses):
        c = add_card(s12, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(5.0), CARD_BG, color)
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = color
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = TEXT_MUTED

    set_notes(s12, """[ZEIT: 11:30 - 12:30 Min. | SPRECHER 3]
In Abgabeprodukt I haben wir die Datenverläufe analysiert. Warum sind unsere Schwellwerte genau so gewählt?
Bei der CPU brauchen wir ein 5-Minuten-Zeitfenster bei 80%, damit ein kurzes apt-upgrade keinen Fehlalarm auslöst.
Bei der Festplatte lässt eine Warnschwelle bei 85% den Admins genügend Zeit zur Bereinigung, bevor das System kollabiert.
Und bei HTTP ist die Sache binär: Reagiert der Webserver länger als 5 Sekunden, können Mitarbeiter nicht arbeiten – hier ist sofortiges Handeln Pflicht. Unsere Grenzwerte haben sich als absolut praxistauglich erwiesen.""")

    # ==========================================
    # SLIDE 13: HERAUSFORDERUNGEN & LESSONS LEARNED
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_background(s13)
    add_header(s13, "Kapitel 11", "Herausforderungen & Lessons Learned", "Praxisprobleme während des Projekts und wie wir sie gelöst haben")

    problems = [
        ("Problem: Paketkonflikte auf Ubuntu 26.04", "Lösung: Offizieller Docker-Container", [
            "Neuere Perl-Versionen blockierten das native .deb-Paket von Checkmk.",
            "Lösung: Wir setzten Checkmk als Docker-Container auf – isoliert, stabil und mit automatischem Neustart bei Systemboot."
        ]),
        ("Problem: MariaDB Netzwerk-Bindung", "Lösung: Bind-Address auf 0.0.0.0", [
            "MariaDB lauschte standardmäßig nur auf 127.0.0.1 (Localhost).",
            "Lösung: Konfiguration in 50-server.cnf auf 0.0.0.0 angepasst, sodass der Port 3306 über das Host-Only-Netzwerk sauber überwacht werden kann."
        ]),
        ("Problem: Windows-Agent Firewall-Freigabe", "Lösung: Port 6556 TCP Rule", [
            "Der Windows-Agent lieferte zunächst keine Daten an den Linux-Server.",
            "Lösung: Port 6556 TCP im Host-Only-Netzwerk in der Windows Defender Firewall explizit freigegeben."
        ])
    ]

    for i, (prob, sol, desc) in enumerate(problems):
        c = add_card(s13, Inches(0.8), Inches(1.8 + i * 1.6), Inches(11.7), Inches(1.45))
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"❌ {prob}   ➔   ✅ {sol}"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        for d in desc:
            pd = tf.add_paragraph()
            pd.text = "   • " + d
            pd.font.size = Pt(10.5)
            pd.font.color.rgb = TEXT_MUTED

    set_notes(s13, """[ZEIT: 12:30 - 13:15 Min. | SPRECHER 1]
Natürlich lief in den drei Tagen nicht alles auf Knopfdruck. Zwei echte Herausforderungen:
Erstens: Paketkonflikte auf Ubuntu 26.04. Unsere Lösung war der offizielle Docker-Container – damit läuft Checkmk komplett isoliert, stabil und startet bei jedem Booten automatisch.
Zweitens: MariaDB lauschte standardmäßig nur auf 127.0.0.1. Wir haben das Bind-Address-Setting angepasst, damit die Datenbank über das Netzwerk überwacht werden kann.
Unsere wichtigste Lesson Learned: Eine saubere Netzwerkplanung vorab spart hintenraus Stunden an Fehlersuche.""")

    # ==========================================
    # SLIDE 14: PROJEKTERGEBNIS
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_background(s14)
    add_header(s14, "Kapitel 12", "Projektergebnis & Zielerreichung (Abgabeprodukt J)", "Alle 11 MUSS-Anforderungen zu 100 % erfüllt • Strukturierter Abnahmetest bestanden")

    kpis = [
        ("MUSS-Anforderungen", "11 / 11", "100 % erfüllt", ACCENT_GREEN),
        ("KANN-Anforderungen", "3 / 5", "60 % umgesetzt", ACCENT_BLUE),
        ("Störungsprüfungen", "4 / 4", "100 % erkannt", ACCENT_GREEN),
        ("Abnahmetests (T01–T12)", "13 / 13", "100 % bestanden", ACCENT_GREEN)
    ]

    for i, (label, val, sub, col) in enumerate(kpis):
        c = add_card(s14, Inches(0.8 + i * 2.95), Inches(1.8), Inches(2.8), Inches(2.0), CARD_BG, col)
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = label.upper()
        p.font.size = Pt(10)
        p.font.color.rgb = TEXT_MUTED
        pv = tf.add_paragraph()
        pv.text = val
        pv.font.size = Pt(32)
        pv.font.bold = True
        pv.font.color.rgb = col
        ps = tf.add_paragraph()
        ps.text = sub
        ps.font.size = Pt(11)
        ps.font.bold = True
        ps.font.color.rgb = TEXT_WHITE

    c_fazit = add_card(s14, Inches(0.8), Inches(4.1), Inches(11.7), Inches(2.7), CARD_BG, ACCENT_GREEN)
    tf_f = c_fazit.text_frame
    tf_f.word_wrap = True
    p = tf_f.paragraphs[0]
    p.text = "🏆 Fazit des Proof of Concept:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    fazit_pts = [
        "Die Checkmk Raw Edition 2.3 hat bewiesen, dass sie die Anforderungen der Müller & Partner GmbH vollständig erfüllt.",
        "Der Zeitrahmen von 3 Projekttagen (geplant: 39,0 h | Ist: 41,5 h) wurde mit einer minimalen Abweichung von +6,4 % eingehalten.",
        "Die Lösung arbeitet ressourcenschonend, benötigt keine teuren Lizenzen und ist sofort einsatzbereit."
    ]
    for fp in fazit_pts:
        pfp = tf_f.add_paragraph()
        pfp.text = "✓ " + fp
        pfp.font.size = Pt(11)
        pfp.font.color.rgb = TEXT_WHITE

    set_notes(s14, """[ZEIT: 13:15 - 14:00 Min. | SPRECHER 1]
Fassen wir das Gesamtergebnis zusammen:
Alle 11 Muss-Anforderungen sind zu 100% erfüllt.
Drei zusätzliche Kann-Anforderungen wurden implementiert.
Alle 4 Störungstests wurden erfolgreich bestanden.
Und im strukturierten Abnahmetest nach Kapitel 11 haben wir 13 von 13 Testfällen auf 'PASSED' gesetzt.
Mit 41,5 Arbeitsstunden lagen wir nur knapp 6% über dem Plan – der Proof of Concept ist damit auf ganzer Linie gelungen.""")

    # ==========================================
    # SLIDE 15: ROLLOUT-FAHRPLAN
    # ==========================================
    s15 = prs.slides.add_slide(blank_layout)
    add_background(s15)
    add_header(s15, "Kapitel 13", "Empfehlung & 3-Phasen-Rollout-Fahrplan", "Konkrete Handlungsempfehlung für die Geschäftsführung zur Produktivübernahme")

    phases = [
        ("Phase 1 (Woche 1–2)", "Pilotbetrieb auf Kernsystemen", ACCENT_GREEN, [
            "Installation auf dedizierter Hardware/VM.",
            "Anbindung der 10 kritischsten Server (Active Directory, DNS, ERP, File-Server).",
            "Einarbeitung des internen IT-Teams in die WATO-Administration."
        ]),
        ("Phase 2 (Woche 3–4)", "Vollständiger Rollout", ACCENT_BLUE, [
            "Erfassung aller Arbeitsplatz-PCs und NAS-Speicher über Windows/Linux-Agenten.",
            "Einrichtung der E-Mail- und SMS-Benachrichtigungsketten.",
            "Feintuning der Schwellwerte für den Normalbetrieb."
        ]),
        ("Phase 3 (Monat 2)", "Erweiterung & Netzinfrastruktur", RGBColor(168, 85, 247), [
            "Anbindung von Netzwerkswitches und Routern via SNMP.",
            "Zentrales Log-Monitoring und Auswertung historischer Daten.",
            "Kapazitätsplanung für zukünftiges Hardware-Wachstum."
        ])
    ]

    for i, (p_title, p_sub, color, steps) in enumerate(phases):
        c = add_card(s15, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(5.0), CARD_BG, color)
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = p_title.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = color
        pv = tf.add_paragraph()
        pv.text = p_sub
        pv.font.size = Pt(13)
        pv.font.bold = True
        pv.font.color.rgb = TEXT_WHITE
        for s in steps:
            ps = tf.add_paragraph()
            ps.text = "• " + s
            ps.font.size = Pt(10.5)
            ps.font.color.rgb = TEXT_MUTED

    set_notes(s15, """[ZEIT: 14:00 - 14:45 Min. | SPRECHER 1]
Unsere klare Handlungsempfehlung an die Geschäftsführung der Müller & Partner GmbH lautet daher: Checkmk Raw Edition sollte fest in den Produktivbetrieb übernommen werden.
Wir empfehlen einen 3-Phasen-Rollout:
Phase 1 in den ersten zwei Wochen: Ein dedizierter Server für Checkmk und die Anbindung der 10 kritischsten Kernserver.
Phase 2 im ersten Monat: Kompletter Rollout auf alle Clients und NAS-Systeme plus E-Mail-Alarmierungsketten.
Phase 3: SNMP-Überwachung der Switche und historische Kapazitätsplanung.""")

    # ==========================================
    # SLIDE 16: ABSCHLUSS & LIVE-DEMO
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_background(s16)

    # Large Checkmark Icon
    c_icon = add_card(s16, Inches(5.8), Inches(1.2), Inches(1.7), Inches(1.2), RGBColor(16, 185, 129), RGBColor(16, 185, 129))
    c_icon.fill.transparency = 0.8
    p = c_icon.text_frame.paragraphs[0]
    p.text = "✓"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.alignment = PP_ALIGN.CENTER

    tb_end = s16.shapes.add_textbox(Inches(0.8), Inches(2.6), Inches(11.7), Inches(1.8))
    tf_e = tb_end.text_frame
    tf_e.word_wrap = True
    p1 = tf_e.paragraphs[0]
    p1.text = "Vielen Dank für Ihre Aufmerksamkeit!"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.alignment = PP_ALIGN.CENTER
    p2 = tf_e.add_paragraph()
    p2.text = "Wir stehen nun für Ihre Fragen und die Live-Demonstration zur Verfügung."
    p2.font.size = Pt(16)
    p2.font.color.rgb = TEXT_MUTED
    p2.alignment = PP_ALIGN.CENTER

    # Live-Demo Access Card
    c_demo = add_card(s16, Inches(2.8), Inches(4.6), Inches(7.7), Inches(2.0), CARD_BG, ACCENT_GREEN)
    tf_d = c_demo.text_frame
    tf_d.word_wrap = True
    p = tf_d.paragraphs[0]
    p.text = "🖥️ LIVE-DEMONSTRATION BEREIT:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.alignment = PP_ALIGN.CENTER
    p_info = tf_d.add_paragraph()
    p_info.text = "Checkmk Dashboard: http://localhost:8080/cmk/  |  Login: cmkadmin / cmkadmin\nLive-Hosts: mon-srv01 (.101)  •  web-srv01 (.102)  •  win-client01 (.1)"
    p_info.font.size = Pt(11)
    p_info.font.color.rgb = TEXT_WHITE
    p_info.alignment = PP_ALIGN.CENTER

    set_notes(s16, """[ZEIT: 14:45 - 15:00 Min. | ALLE SPRECHER]
Damit sind wir am Ende unseres Vortrags angekommen.
Die Monitoring-Instanz läuft aktuell live auf unserem System – wir können Ihnen das Dashboard, die Host-Zustände und auf Wunsch auch gerne einen Live-Störungstest direkt vorführen.
Vielen Dank für Ihre Aufmerksamkeit – wir freuen uns auf Ihre Fragen!""")

    output_path = r"C:\Users\erolt\Desktop\monitor\IT-Monitoring_Abschlusspraesentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
