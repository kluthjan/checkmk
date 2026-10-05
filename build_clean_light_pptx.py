import os
import win32com.client
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Clean, Bright Modern Corporate Palette
    C_BG = RGBColor(255, 255, 255)         # Pure White
    C_CARD_BG = RGBColor(248, 250, 252)    # Slate 50
    C_CARD_BORDER = RGBColor(226, 232, 240)# Slate 200
    C_TEXT_NAVY = RGBColor(15, 23, 42)     # Slate 900 (High contrast)
    C_TEXT_BODY = RGBColor(51, 65, 85)     # Slate 700
    C_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    
    C_PRIMARY = RGBColor(5, 150, 105)      # Emerald 600 (Checkmk Brand)
    C_PRIMARY_LIGHT = RGBColor(236, 253, 245) # Emerald 50
    C_PRIMARY_BORDER = RGBColor(110, 231, 183) # Emerald 300
    
    C_BLUE = RGBColor(37, 99, 235)         # Blue 600
    C_BLUE_LIGHT = RGBColor(239, 246, 255) # Blue 50
    
    C_ROSE = RGBColor(225, 29, 72)         # Rose 600
    C_ROSE_LIGHT = RGBColor(255, 241, 242) # Rose 50
    
    C_AMBER = RGBColor(217, 119, 6)        # Amber 600

    def add_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, chapter, title, subtitle):
        # Chapter Badge
        badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(2.2), Inches(0.32))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_PRIMARY_LIGHT
        badge.line.color.rgb = C_PRIMARY_BORDER
        badge.line.width = Pt(1)
        p_b = badge.text_frame.paragraphs[0]
        p_b.text = chapter.upper()
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = C_PRIMARY
        p_b.alignment = PP_ALIGN.CENTER

        # Title
        tb_t = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.6))
        p_t = tb_t.text_frame.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_NAVY

        # Subtitle
        if subtitle:
            tb_s = slide.shapes.add_textbox(Inches(0.8), Inches(1.3), Inches(11.7), Inches(0.4))
            p_s = tb_s.text_frame.paragraphs[0]
            p_s.text = subtitle
            p_s.font.size = Pt(11.5)
            p_s.font.color.rgb = C_TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_col=C_CARD_BG, border_col=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_col
        card.line.color.rgb = border_col
        card.line.width = Pt(1.2)
        return card

    def set_notes(slide, notes):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes

    # ==========================================
    # SLIDE 1: TITELFOLIE (Mit allen 5 Team-Namen!)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)

    # Top pill
    top_pill = add_card(s1, Inches(0.8), Inches(0.8), Inches(3.6), Inches(0.4), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    p = top_pill.text_frame.paragraphs[0]
    p.text = "PROOF OF CONCEPT • 3 PROJEKTTAGE"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p.alignment = PP_ALIGN.CENTER

    # Main Title
    tb_m = s1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(1.6))
    tf_m = tb_m.text_frame
    tf_m.word_wrap = True
    p1 = tf_m.paragraphs[0]
    p1.text = "Einführung eines zentralen IT-Monitorings"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_NAVY
    p2 = tf_m.add_paragraph()
    p2.text = "Prototypische Implementierung mit Checkmk Raw Edition 2.3"
    p2.font.size = Pt(18)
    p2.font.color.rgb = C_PRIMARY

    # Client & Project Frame Box (Left)
    c_meta = add_card(s1, Inches(0.8), Inches(3.2), Inches(5.6), Inches(3.6))
    tf_meta = c_meta.text_frame
    tf_meta.word_wrap = True
    p = tf_meta.paragraphs[0]
    p.text = "📋 PROJEKTDATEN & RAHMEN"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_NAVY

    meta_items = [
        ("Auftraggeber:", "Müller & Partner GmbH"),
        ("Projektlaufzeit:", "3 Projekttage (Proof of Concept)"),
        ("Datum & Version:", "September / Oktober 2026 • Version 1.0"),
        ("Zielerreichung:", "11 von 11 MUSS-Kriterien erfüllt (100 %)"),
        ("Systemauswahl:", "Checkmk Raw Edition 2.3 (Testsieger: 4,40 Pkt.)")
    ]
    for lbl, val in meta_items:
        pm = tf_meta.add_paragraph()
        pm.text = f"{lbl:<18} {val}"
        pm.font.size = Pt(11)
        pm.font.color.rgb = C_TEXT_BODY

    # Team Box (Right) - WITH ALL 5 NAMES!
    c_team = add_card(s1, Inches(6.8), Inches(3.2), Inches(5.7), Inches(3.6), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    tf_team = c_team.text_frame
    tf_team.word_wrap = True
    p = tf_team.paragraphs[0]
    p.text = "👥 PROJEKTTEAM (GRONE UMSCHULUNGSTEAM)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    p_sub = tf_team.add_paragraph()
    p_sub.text = "Fachinformatiker Systemintegration\n"
    p_sub.font.size = Pt(10)
    p_sub.font.color.rgb = C_TEXT_MUTED

    team_members = [
        ("Jan Kluth", "Projektleitung, Ausgangslage & Fazit"),
        ("Marion Ballcke", "Anforderungsanalyse & Marktanalyse"),
        ("Mathias Vorrau", "Nutzwertanalyse & Entscheidungsmatrix"),
        ("Marco Schmidt", "Netzwerkarchitektur & Custom Check"),
        ("Robert Ortmann", "Störungssimulation & Datenanalyse")
    ]
    for name, role in team_members:
        pt = tf_team.add_paragraph()
        pt.text = f"• {name}  –  {role}"
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = C_TEXT_NAVY

    set_notes(s1, """[ZEIT: 0:00 - 0:45 Min. | SPRECHER: Jan Kluth]
Guten Tag zusammen und herzlich willkommen zu unserer Projektpräsentation!
Mein Name ist Jan Kluth und ich präsentiere Ihnen heute gemeinsam mit meinen Teamkollegen Marion Ballcke, Mathias Vorrau, Marco Schmidt und Robert Ortmann unser Abschlussprojekt: 
Die Einführung eines zentralen IT-Monitorings für die Müller & Partner GmbH.

Unser Auftrag war es, innerhalb von 3 Projekttagen eine praxistaugliche Open-Source-Monitoringlösung auszuwählen, in einem virtuellen Testnetzwerk aufzubauen und anhand realer Störungen zu validieren. 
Wir haben alle 11 Muss-Anforderungen zu 100 Prozent erfüllt – und wie wir das im Team umgesetzt haben, stellen wir Ihnen jetzt vor.""")

    # ==========================================
    # SLIDE 2: AGENDA
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Übersicht", "Agenda der Präsentation", "Strukturierter 15-Minuten-Ablauf, aufgeteilt auf das Projektteam")

    agenda = [
        ("01", "Ausgangslage & Anforderungen", "Manuelle Überwachung, Risiken & Pflichtenkatalog M01–M11", "Jan Kluth & Marion Ballcke"),
        ("02", "Evaluation & Nutzwertanalyse", "Vergleich von Checkmk, Zabbix und Nagios nach DIN-Matrix", "Mathias Vorrau"),
        ("03", "Technische Implementierung", "Testnetzwerk, Dienst-Überwachung & eigener Python-Check", "Marco Schmidt"),
        ("04", "Validierung & Rollout-Fahrplan", "4 Störungssimulationen, Datenanalyse & Empfehlung", "Robert Ortmann & Jan Kluth")
    ]
    for i, (num, title, desc, speaker) in enumerate(agenda):
        c = add_card(s2, Inches(0.8), Inches(1.8 + i * 1.3), Inches(11.7), Inches(1.15))
        tf = c.text_frame
        tf.word_wrap = True
        pn = tf.paragraphs[0]
        pn.text = f"{num}   {title}"
        pn.font.size = Pt(15)
        pn.font.bold = True
        pn.font.color.rgb = C_PRIMARY
        
        pd = tf.add_paragraph()
        pd.text = f"      {desc}  |  🗣️ {speaker}"
        pd.font.size = Pt(11)
        pd.font.color.rgb = C_TEXT_BODY

    set_notes(s2, """[ZEIT: 0:45 - 1:15 Min. | SPRECHER: Jan Kluth]
Wir haben die Präsentation in vier Abschnitte gegliedert und fair im Team aufgeteilt:
Zuerst erläutere ich die Ausgangslage bei Müller & Partner, bevor Marion die Anforderungen vorstellt.
Anschließend übernimmt Mathias die Nutzwertanalyse und zeigt, warum Checkmk gewonnen hat.
Im dritten Teil führt Marco durch die technische Umsetzung im Testnetz und unseren Python-Check.
Zum Schluss präsentieren Robert und ich die Störungstests, die Datenanalyse und unsere Empfehlung an die Geschäftsführung.""")

    # ==========================================
    # SLIDE 3: AUSGANGSLAGE & PROBLEMSTELLUNG
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "Kapitel 01", "Ausgangslage & Problemstellung", "Warum die bisherige Betriebsweise ein untragbares Risiko für das Unternehmen darstellte")

    c_prob = add_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), C_ROSE_LIGHT, RGBColor(254, 205, 211))
    tf_p = c_prob.text_frame
    tf_p.word_wrap = True
    p = tf_p.paragraphs[0]
    p.text = "⚠️ Das bisherige Problem: Manuelle Kontrolle"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_ROSE

    probs = [
        "Wachsende IT: Mehrere Linux-Server für Web, Dateiverwaltung und DNS/DHCP.",
        "Reaktives Brandlöschen: Admins erfuhren von Ausfällen erst durch Anrufe verärgerter Mitarbeiter.",
        "Unbemerkte DNS/DHCP-Ausfälle: Ganze Abteilungen verloren unbemerkt die Netzwerkverbindung.",
        "Drohender Datenverlust: Volllaufende Festplatten wurden vor dem Absturz nicht signalisiert.",
        "Quälend langsame Antwortzeiten: Performance-Einbrüche blieben undokumentiert."
    ]
    for pb in probs:
        p_pb = tf_p.add_paragraph()
        p_pb.text = "✗ " + pb
        p_pb.font.size = Pt(11)
        p_pb.font.color.rgb = C_TEXT_NAVY

    c_sol = add_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    tf_s = c_sol.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "🎯 Das Projektziel: Proaktives Monitoring"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    sols = [
        "Früherkennung: Störungen erkennen und beheben, BEVOR Endanwender betroffen sind.",
        "Zentrales Web-Dashboard: Gesamter Zustand aller Hosts und Dienste auf einen Blick.",
        "Automatische Alarmierung: Sofortige Benachrichtigung bei Schwellwert-Überschreitung.",
        "100 % Open Source: Etablierte Enterprise-Standards ohne teure Lizenzgebühren.",
        "Proof of Concept in 3 Tagen: Voll funktionsfähige Testumgebung zum Praxisnachweis."
    ]
    for sb in sols:
        p_sb = tf_s.add_paragraph()
        p_sb.text = "✓ " + sb
        p_sb.font.size = Pt(11)
        p_sb.font.color.rgb = C_TEXT_NAVY

    set_notes(s3, """[ZEIT: 1:15 - 2:30 Min. | SPRECHER: Jan Kluth]
Schauen wir auf die Ausgangslage bei Müller & Partner: Das Unternehmen ist gewachsen. Zahlreiche Arbeitsplätze, mehrere Server für Webanwendungen, interne Dateiablage und DNS/DHCP.
Das Problem: Es gab überhaupt kein automatisiertes Monitoring!
Die Admins erfuhren von Ausfällen fast immer erst dann, wenn Mitarbeiter wütend anriefen. DNS fiel aus, Festplatten liefen fast voll – was beinahe zu Datenverlust geführt hätte.
Die Geschäftsführung forderte daher: Weg vom reaktiven Brandlöschen hin zu einer proaktiven Überwachung. Ich übergebe nun an Marion für die Anforderungen.""")

    # ==========================================
    # SLIDE 4: ANFORDERUNGSANALYSE (SAUBERE 3-SPALTEN-STRUKTUR!)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Kapitel 02", "Anforderungsanalyse (Abgabeprodukt A)", "11 verbindliche MUSS-Kriterien zu 100 % erfüllt • Strukturierte Kategorien")

    # 3 Domain Cards instead of 12 boxes!
    cat_cards = [
        ("1. Infrastruktur & Systeme", C_PRIMARY, [
            ("M01: Zentrales Monitoring", "Einrichtung einer zentralen Überwachungsinstanz"),
            ("M02: Multi-System-Setup", "Mind. 2 Testsysteme (Linux & Windows)"),
            ("M03: Erreichbarkeit (ICMP)", "Permanente Ping-Überwachung"),
            ("M04: Systemressourcen", "CPU, RAM und Festplattenbelegung")
        ]),
        ("2. Dienste & Schwellwerte", C_BLUE, [
            ("M05: Netzwerkdienste", "Aktive Überwachung: HTTP, MySQL, SSH"),
            ("M06: Definierte Grenzwerte", "Fundierte Schwellen (WARN & CRIT)"),
            ("M09: Custom Check", "Eigenes Python-Messwert-Skript (TCP)"),
            ("K04: Erweiterte Metriken", "Zusätzliche historische Trendkurven")
        ]),
        ("3. Alarmierung & Qualität", RGBColor(147, 51, 234), [
            ("M07: Automatische Alarme", "Sofortige Warnung bei Grenzwertüberschreitung"),
            ("M08: Zentrales Dashboard", "Taktische Web-Übersicht für Administratoren"),
            ("M10: Störungssimulation", "4 reale Ausfälle gezielt ausgelöst & validiert"),
            ("M11: Abnahmetests", "Strukturierte Testmatrix (13/13 bestanden)")
        ])
    ]

    for i, (title, col, items) in enumerate(cat_cards):
        c = add_card(s4, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(4.3))
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col

        for mid, mdesc in items:
            p_id = tf.add_paragraph()
            p_id.text = f"\n✓ {mid}"
            p_id.font.size = Pt(11)
            p_id.font.bold = True
            p_id.font.color.rgb = C_TEXT_NAVY
            p_desc = tf.add_paragraph()
            p_desc.text = f"   {mdesc}"
            p_desc.font.size = Pt(9.5)
            p_desc.font.color.rgb = C_TEXT_MUTED

    # Bottom KANN Bar
    c_kann = add_card(s4, Inches(0.8), Inches(6.25), Inches(11.7), Inches(0.75), C_BLUE_LIGHT, RGBColor(191, 219, 254))
    tf_k = c_kann.text_frame
    tf_k.word_wrap = True
    p = tf_k.paragraphs[0]
    p.text = "🎯 ZUSÄTZLICH 3 KANN-ANFORDERUNGEN UMGESETZT (60 %):"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = C_BLUE
    p2 = tf_k.add_paragraph()
    p2.text = "K01 E-Mail-Alarmierung vorbereitet  •  K02 Erweiterte Dashboards & Matrizen  •  K04 Detaillierter Custom Check mit Performancedaten"
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = C_TEXT_BODY

    set_notes(s4, """[ZEIT: 2:30 - 3:45 Min. | SPRECHERIN: Marion Ballcke]
Vielen Dank, Jan! Wir haben das Projekt in elf klare, verbindliche Muss-Kriterien unterteilt, die Sie hier in drei Kategorien sehen:
Erstens: Die Infrastruktur – ein zentraler Server und mindestens zwei überwachte Systeme mit CPU-, RAM- und Festplatten-Sensoren.
Zweitens: Die Netzwerkdienste – aktive Checks für Apache-Webserver, MySQL-Datenbank und SSH sowie unser eigenes Python-Skript.
Drittens: Alarmierung und Qualität – automatische Benachrichtigung, ein übersichtliches Dashboard und die Validierung durch reale Störungstests.
Alle 11 Kriterien haben wir zu 100 % grün abgenommen und zusätzlich 3 Kann-Leistungen implementiert.""")

    # ==========================================
    # SLIDE 5: DIE 3 KANDIDATEN
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "Kapitel 03", "Die 3 Kandidaten im Systemvergleich", "Marktanalyse führender Open-Source-Lösungen für den 3-tägigen Proof of Concept")

    tools = [
        ("Checkmk Raw Edition 2.3", "TESTSIEGER 🏆", C_PRIMARY, C_PRIMARY_LIGHT, C_PRIMARY_BORDER, [
            "Open Source (GNU GPLv2)",
            "Sehr intuitive Web-GUI (WATO)",
            "Automatische Service-Erkennung (Discovery)",
            "Fertige Dashboards out-of-the-box",
            "Keine externe SQL-Datenbank nötig",
            "Schnellster Time-to-Value für 3 Tage"
        ]),
        ("Zabbix 7.0 LTS", "RANG 2 (MÄCHTIG)", C_BLUE, C_BLUE_LIGHT, RGBColor(191, 219, 254), [
            "Open Source (GPLv2)",
            "Sehr flexibel & extrem skalierbar",
            "Mächtige Template-Engine",
            "⚠️ Externe SQL-DB zwingend nötig",
            "⚠️ Hohe Konfigurationskomplexität",
            "⚠️ Setup-Aufwand zu hoch für 3 Tage"
        ]),
        ("Nagios Core 4.5", "RANG 3 (KLASSIKER)", C_TEXT_MUTED, C_CARD_BG, C_CARD_BORDER, [
            "Open Source (GPLv2)",
            "Bewährter, historischer Standard",
            "Extrem sparsam bei Ressourcen",
            "✗ Veraltete Weboberfläche",
            "✗ Rein textbasierte Konfig-Dateien",
            "✗ Keine integrierten Dashboards"
        ])
    ]

    for i, (name, badge, col, bg, border, pts) in enumerate(tools):
        c = add_card(s5, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(5.0), bg, border)
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_NAVY
        pb = tf.add_paragraph()
        pb.text = badge
        pb.font.size = Pt(9.5)
        pb.font.bold = True
        pb.font.color.rgb = col
        for pt in pts:
            pp = tf.add_paragraph()
            pp.text = f"• {pt}"
            pp.font.size = Pt(10.5)
            pp.font.color.rgb = C_TEXT_BODY

    set_notes(s5, """[ZEIT: 3:45 - 5:00 Min. | SPRECHERIN: Marion Ballcke]
Welches System passt am besten? Wir haben die drei bekanntesten Open-Source-Lösungen verglichen:
Alle drei sind lizenzkostenfrei. 
Nagios Core ist der Urvater – sparsam, aber die rein textbasierte Konfiguration ist für ein modernes Unternehmen nicht mehr zeitgemäß.
Zabbix ist extrem mächtig und skalierbar, benötigt aber zwingend eine externe relationale Datenbank und eine lange Einarbeitungszeit.
Checkmk Raw punktet sofort mit seiner intuitiven WATO-Weboberfläche, automatischer Service-Erkennung und fertigen Dashboards.
Ich übergebe an Mathias für die konkrete Nutzwertanalyse!""")

    # ==========================================
    # SLIDE 6: NUTZWERTANALYSE MATRIX
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Kapitel 04", "Nutzwertanalyse & Entscheidungsmatrix", "Fundierte Entscheidung nach DIN-Bewertungsmethode (Skala 1 bis 5)")

    c_m = add_card(s6, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf_m = c_m.text_frame
    tf_m.word_wrap = True

    m_rows = [
        ("Kriterium", "Gewicht", "Checkmk Raw", "Zabbix", "Nagios Core"),
        ("1. Kosten / Lizenz (Open Source)", "10 %", "5 / 0,50", "5 / 0,50", "5 / 0,50"),
        ("2. Bedienbarkeit & GUI (Ausschlaggebend)", "20 %", "5 / 1,00  🏆", "3 / 0,60", "2 / 0,40"),
        ("3. OS-Unterstützung (Linux & Windows)", "10 %", "4 / 0,40", "5 / 0,50", "4 / 0,40"),
        ("4. Netzwerkdienste (HTTP, SQL, SSH)", "15 %", "4 / 0,60", "5 / 0,75", "4 / 0,60"),
        ("5. Alarmierung & Benachrichtigung", "15 %", "4 / 0,60", "4 / 0,60", "3 / 0,45"),
        ("6. Visualisierung & Dashboards (Ausschlaggebend)", "15 %", "5 / 0,75  🏆", "4 / 0,60", "2 / 0,30"),
        ("7. Erweiterbarkeit & Dokumentation", "15 %", "4 / 0,55", "5 / 0,65", "4 / 0,60"),
        ("GESAMTERGEBNIS (PUNKTE / RANG)", "100 %", "4,40 (RANG 1) 🏆", "4,20 (RANG 2)", "3,30 (RANG 3)")
    ]

    p_h = tf_m.paragraphs[0]
    p_h.text = f"{m_rows[0][0]:<45} {m_rows[0][1]:<10} {m_rows[0][2]:<18} {m_rows[0][3]:<15} {m_rows[0][4]}"
    p_h.font.size = Pt(11)
    p_h.font.bold = True
    p_h.font.color.rgb = C_PRIMARY

    for row in m_rows[1:]:
        pr = tf_m.add_paragraph()
        pr.text = f"{row[0]:<45} {row[1]:<10} {row[2]:<18} {row[3]:<15} {row[4]}"
        pr.font.size = Pt(10.5)
        if "GESAMTERGEBNIS" in row[0]:
            pr.font.bold = True
            pr.font.size = Pt(12)
            pr.font.color.rgb = C_PRIMARY
        elif "Ausschlaggebend" in row[0]:
            pr.font.bold = True
            pr.font.color.rgb = C_TEXT_NAVY
        else:
            pr.font.color.rgb = C_TEXT_BODY

    set_notes(s6, """[ZEIT: 5:00 - 6:15 Min. | SPRECHER: Mathias Vorrau]
Danke Marion! Um die Entscheidung mathematisch fundiert zu belegen, haben wir eine gewichtete Nutzwertanalyse durchgeführt.
Wir haben sieben Kriterien festgelegt:
Das wichtigste Kriterium mit 20% war die Bedienbarkeit im Alltag. Visualisierung, Alarmierung und Netzwerkdienste wurden mit je 15% gewichtet.
Auf einer Skala von 1 bis 5 haben wir die Systeme bewertet und gewichtet.
Das Ergebnis ist eindeutig:
Checkmk holt mit 4,40 Punkten den 1. Platz.
Zabbix folgt mit 4,20 Punkten auf Platz 2.
Nagios Core erreicht mit 3,30 Punkten nur Platz 3.""")

    # ==========================================
    # SLIDE 7: ENTSCHEIDUNGSBEGRÜNDUNG
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Kapitel 05", "Warum Checkmk gewonnen hat: Der Gamechanger", "Detailanalyse des Punkteabstands zwischen Checkmk (4,40) und Zabbix (4,20)")

    c_w = add_card(s7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    tf_w = c_w.text_frame
    tf_w.word_wrap = True
    p = tf_w.paragraphs[0]
    p.text = "🏆 Wo Checkmk siegte: +0,55 Punkte Vorsprung"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    w_pts = [
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
        "Fazit: In den beiden praxisrelevantesten Kriterien dominierte Checkmk klar."
    ]
    for pt in w_pts:
        pp = tf_w.add_paragraph()
        pp.text = pt
        pp.font.size = Pt(10.5)
        pp.font.color.rgb = C_TEXT_NAVY if "Vorsprung" in pt or "Fazit" in pt else C_TEXT_BODY

    c_z = add_card(s7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), C_BLUE_LIGHT, RGBColor(191, 219, 254))
    tf_z = c_z.text_frame
    tf_z.word_wrap = True
    p = tf_z.paragraphs[0]
    p.text = "⚖️ Zabbix' Aufholjagd: +0,35 Punkte – warum es nicht reichte"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_BLUE

    z_pts = [
        "Zabbix war in 3 Kriterien überlegen:",
        "  • Netzwerkdienste (15 %): Zabbix 5 vs. Checkmk 4 ➔ +0,15",
        "  • Erweiterbarkeit (15 %): Zabbix 5 vs. Checkmk 4 ➔ +0,10",
        "  • OS-Support (10 %): Zabbix 5 vs. Checkmk 4 ➔ +0,10",
        "",
        "Warum es trotzdem nicht zum Gesamtsieg reichte:",
        "  • Zabbix holte insgesamt +0,35 Punkte Vorsprung auf.",
        "  • Checkmk sicherte sich bei GUI & Dashboards aber +0,55 Punkte!",
        "",
        "Differenz-Rechnung:",
        "  +0,55 (Checkmk) minus +0,35 (Zabbix) = +0,20 Punkte Gesamtsieg!"
    ]
    for pt in z_pts:
        pp = tf_z.add_paragraph()
        pp.text = pt
        pp.font.size = Pt(10.5)
        pp.font.color.rgb = C_TEXT_NAVY if "Gesamtsieg" in pt or "Differenz" in pt else C_TEXT_BODY

    set_notes(s7, """[ZEIT: 6:15 - 7:30 Min. | SPRECHER: Mathias Vorrau]
Man könnte sich fragen: Zabbix war doch bei Netzwerkdiensten und Erweiterbarkeit sehr stark – warum hat Checkmk trotzdem gewonnen?
Genau das zeigt diese Folie:
Zabbix war in drei Kriterien besser und holte dort insgesamt +0,35 Punkte.
ABER: Checkmk dominierte bei den beiden Kriterien mit dem höchsten Praxisnutzen:
Bei der Bedienbarkeit holte Checkmk eine glatte 5 und Zabbix nur eine 3 – das macht allein +0,40 Punkte Vorsprung!
Bei den fertigen Dashboards kamen nochmal +0,15 Punkte dazu.
+0,55 Punkte Vorsprung minus +0,35 Punkte Aufholjagd = +0,20 Punkte Gesamtsieg für Checkmk!
Damit übergebe ich an Marco für die technische Umsetzung.""")

    # ==========================================
    # SLIDE 8: TESTNETZ-ARCHITEKTUR
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Kapitel 06", "Testnetz-Architektur & Topologie", "Strukturiertes 3-System-Testnetz (VirtualBox Host-Only Subnetz 192.168.56.0/24)")

    topo_data = [
        ("mon-srv01 (MONITORING-SERVER)", "192.168.56.101", C_PRIMARY, [
            "OS: Ubuntu 26.04 LTS VM",
            "Rolle: Checkmk Raw Edition 2.3",
            "Betrieb: Docker-Container (restart: always)",
            "Web-GUI: Port 80 (gemappt auf Host: 8080)",
            "Status: 24 Services aktiv überwacht"
        ]),
        ("web-srv01 (LINUX WEBSERVER)", "192.168.56.102", C_BLUE, [
            "OS: Geklonte Ubuntu VM (4 GB RAM)",
            "Dienste: Apache2 (HTTP 80), MariaDB (SQL 3306), SSH (22)",
            "Checkmk Agent: Port 6556 TCP aktiv",
            "Custom Check: Python TCP-Verbindungsüberwachung",
            "Ports: SSH 2223 / HTTP 8081"
        ]),
        ("win-client01 (WINDOWS CLIENT)", "192.168.56.1", RGBColor(147, 51, 234), [
            "OS: Windows 10/11 Host-PC",
            "Agent: Checkmk Windows Agent (MSI)",
            "Dienst: Checkmk Service aktiv",
            "Firewall: Port 6556 freigegeben",
            "Überwacht: CPU, RAM, Festplatte C:"
        ])
    ]

    for i, (title, ip, col, details) in enumerate(topo_data):
        c = add_card(s8, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(4.3))
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_NAVY
        pip = tf.add_paragraph()
        pip.text = f"IP: {ip}"
        pip.font.size = Pt(11)
        pip.font.bold = True
        pip.font.color.rgb = col
        for d in details:
            pd = tf.add_paragraph()
            pd.text = f"• {d}"
            pd.font.size = Pt(10)
            pd.font.color.rgb = C_TEXT_BODY

    # Bottom Protocol Card
    c_b = add_card(s8, Inches(0.8), Inches(6.25), Inches(11.7), Inches(0.75), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    tf_b = c_b.text_frame
    tf_b.word_wrap = True
    p = tf_b.paragraphs[0]
    p.text = "KOMMUNIKATIONSPRINZIP (PULL-MONITORING):"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p2 = tf_b.add_paragraph()
    p2.text = "Checkmk Server pollt minütlich Port 6556 aller Zielsysteme ➔ Agent liefert Sensordaten ➔ Livestatus Core bewertet Schwellwerte ➔ Live-Dashboard aktualisiert."
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = C_TEXT_NAVY

    set_notes(s8, """[ZEIT: 7:30 - 8:45 Min. | SPRECHER: Marco Schmidt]
Danke Mathias! Schauen wir auf die technische Umsetzung im Testnetz:
Wir haben in VirtualBox ein isoliertes Host-Only-Netzwerk im Subnetz 192.168.56.0/24 aufgebaut.
Drei Systeme kommunizieren hier miteinander:
Erstens: Unser Monitoring-Server mon-srv01 auf IP .101. Hier läuft Checkmk im Docker-Container – port-gemappt auf 8080 für den Browser.
Zweitens: Unser überwachter Webserver web-srv01 auf IP .102 mit Apache2, MariaDB und OpenSSH.
Drittens: Der Windows-Host-PC auf IP .1 mit dem offiziellen Windows-Agenten.
Die Kommunikation erfolgt nach dem Pull-Prinzip: Der Server kontaktiert jede Minute Port 6556 der Clients und holt alle Messwerte ab.""")

    # ==========================================
    # SLIDE 9: UMGESETZTE ÜBERWACHUNG
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Kapitel 07", "Umgesetzte Dienst-Überwachung & Schwellwerte", "Aktive Überwachung von Anwendungsdiensten (M05) & definierte Grenzwerte (M06)")

    c_s = add_card(s9, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf_s = c_s.text_frame
    tf_s.word_wrap = True

    services = [
        ("Dienst / Ressource", "Überwachter Service", "Port", "Warnung (WARN)", "Kritisch (CRIT)", "Live-Status"),
        ("Apache Webserver", "HTTP_Apache", "Port 80", "> 2,0 Sekunden", "> 5,0 s / Ausfall", "OK (200 OK) 🟢"),
        ("MariaDB Datenbank", "MySQL_Database", "Port 3306", "> 1,0 Sekunde", "> 3,0 s / Ausfall", "OK (Port 3306) 🟢"),
        ("Fernwartung", "SSH_Service", "Port 22", "Verzögerung > 1s", "Ausfall / Refused", "OK (Port 22) 🟢"),
        ("Custom Check", "Active_TCP_Connections", "-", "> 100 Verbindungen", "> 200 Verbindungen", "OK (1 Verb.) 🟢"),
        ("CPU-Auslastung", "CPU utilization", "-", "> 80 % (5 Min)", "> 95 % (5 Min)", "OK (3–7 %) 🟢"),
        ("Arbeitsspeicher", "Memory", "-", "> 85 % genutzt", "> 95 % genutzt", "OK (19 %) 🟢"),
        ("Festplatte", "Filesystem /", "-", "> 85 % belegt", "> 95 % belegt", "OK (37 %) 🟢")
    ]

    p_h = tf_s.paragraphs[0]
    p_h.text = f"{services[0][0]:<22} {services[0][1]:<24} {services[0][2]:<12} {services[0][3]:<20} {services[0][4]:<20} {services[0][5]}"
    p_h.font.size = Pt(11)
    p_h.font.bold = True
    p_h.font.color.rgb = C_PRIMARY

    for row in services[1:]:
        pr = tf_s.add_paragraph()
        pr.text = f"{row[0]:<22} {row[1]:<24} {row[2]:<12} {row[3]:<20} {row[4]:<20} {row[5]}"
        pr.font.size = Pt(10.5)
        pr.font.color.rgb = C_TEXT_NAVY if "🟢" in row[5] else C_TEXT_BODY

    set_notes(s9, """[ZEIT: 8:45 - 9:45 Min. | SPRECHER: Marco Schmidt]
Auf unserem Webserver web-srv01 haben wir alle geforderten Anwendungsdienste aktiv eingebunden:
Den Apache-Webserver prüfen wir auf Port 80. Die Reaktionszeit ist gemäß Anforderung M06 belegt: Ab 2 Sekunden gibt es eine Warnung, ab 5 Sekunden oder bei Ausfall ist es kritisch.
Die MariaDB-Datenbank überwachen wir auf Port 3306, den SSH-Dienst auf Port 22.
Und zusätzlich erfasst der Agent kontinuierlich alle Systemressourcen: CPU-Auslastung, RAM, Festplattenbelegung und Netzwerkinterfaces – alles läuft aktuell im optimalen grünen Bereich.""")

    # ==========================================
    # SLIDE 10: EIGENENTWICKLUNG CUSTOM CHECK
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Kapitel 08", "Eigenentwicklung: Custom Local Check (M09)", "Entwicklung eines eigenständigen Python-Plugins zur TCP-Verbindungsanalyse")

    c_code = add_card(s10, Inches(0.8), Inches(1.8), Inches(6.0), Inches(5.0), RGBColor(15, 23, 42), C_PRIMARY)
    tf_c = c_code.text_frame
    tf_c.word_wrap = True
    p = tf_c.paragraphs[0]
    p.text = "#!/usr/bin/env python3\n# Local Check: active_tcp_connections.py\nimport subprocess, sys\n\ndef get_tcp_connections():\n    out = subprocess.check_output(['ss', '-ant'], text=True)\n    count = sum(1 for line in out.splitlines() if 'ESTAB' in line)\n    \n    warn, crit = 100, 200\n    status = 0\n    status_txt = 'OK'\n    \n    if count >= crit:\n        status, status_txt = 2, 'CRIT'\n    elif count >= warn:\n        status, status_txt = 1, 'WARN'\n        \n    print(f'{status} \"Active_TCP_Connections\" '\n          f'connections={count};{warn};{crit} '\n          f'{status_txt} - {count} aktive TCP Verbindungen')\n\nif __name__ == '__main__':\n    get_tcp_connections()"
    p.font.size = Pt(9.5)
    p.font.color.rgb = RGBColor(241, 245, 249)

    c_expl = add_card(s10, Inches(7.0), Inches(1.8), Inches(5.5), Inches(5.0))
    tf_e = c_expl.text_frame
    tf_e.word_wrap = True
    p = tf_e.paragraphs[0]
    p.text = "💡 Funktionsweise & Checkmk-Protokoll"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    exp_pts = [
        "Speicherort: /usr/lib/check_mk_agent/local/",
        "Protokoll-Format: <STATUS> \"<NAME>\" <METRIKEN> <TEXT>",
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
    for pt in exp_pts:
        pp = tf_e.add_paragraph()
        pp.text = pt
        pp.font.size = Pt(10)
        pp.font.color.rgb = C_TEXT_NAVY if "Mehrwert" in pt or "Protokoll" in pt else C_TEXT_BODY

    set_notes(s10, """[ZEIT: 9:45 - 11:00 Min. | SPRECHER: Marco Schmidt]
Eine besondere Anforderung war M09: Die Eigenentwicklung eines Messwert-Skripts.
Wir haben in Python 3 ein Plugin geschrieben: active_tcp_connections.py.
Es liest über das Linux-Tool 'ss' alle aktiven TCP-Verbindungen im Zustand ESTABLISHED aus.
Das Geniale an Checkmk ist das Local-Check-Format: Das Skript gibt einfach den Statuscode – 0 für OK, 1 für Warnung, 2 für Kritisch –, den Namen, die Metrik und einen Klartext aus.
Übersteigt die Zahl 100 Verbindungen, gibt es eine Warnung, ab 200 wird es kritisch. Checkmk übernimmt das vollautomatisch ins Dashboard und zeichnet sogar historische Graphen.
Ich übergebe nun an Robert für die Störungstests!""")

    # ==========================================
    # SLIDE 11: STÖRUNGSSIMULATION
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "Kapitel 09", "Störungssimulation & Validierung (M10)", "4 reale Ausfallszenarien simuliert und Reaktionszeiten protokolliert")

    c_sim = add_card(s11, Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0))
    tf_sim = c_sim.text_frame
    tf_sim.word_wrap = True

    sims = [
        ("#", "Szenario", "Auslösebefehl", "Erwartung", "Tatsächliche Erkennung", "Reaktionszeit"),
        ("1", "Apache Web-Ausfall", "sudo systemctl stop apache2", "HTTP ➔ CRIT", "CRIT (Connection refused)", "47 Sek. ⚡"),
        ("2", "CPU-Volllast", "stress --cpu 4 --timeout 180", "CPU ➔ WARN/CRIT", "WARN (62s) ➔ CRIT (75s)", "62 Sek. ⚡"),
        ("3", "Festplatte voll", "dd if=/dev/zero of=/tmp/file", "Disk ➔ CRIT", "CRIT (Belegung > 95%)", "60 Sek. ⚡"),
        ("4", "Host-Totalausfall", "VM Power Off (VirtualBox)", "Host ➔ DOWN", "DOWN (ICMP Ping Fail)", "127 Sek. ⚡")
    ]

    p_h = tf_sim.paragraphs[0]
    p_h.text = f"{sims[0][0]:<3} {sims[0][1]:<20} {sims[0][2]:<30} {sims[0][3]:<18} {sims[0][4]:<26} {sims[0][5]}"
    p_h.font.size = Pt(11)
    p_h.font.bold = True
    p_h.font.color.rgb = C_PRIMARY

    for row in sims[1:]:
        pr = tf_sim.add_paragraph()
        pr.text = f"{row[0]:<3} {row[1]:<20} {row[2]:<30} {row[3]:<18} {row[4]:<26} {row[5]}"
        pr.font.size = Pt(10.5)
        pr.font.color.rgb = C_TEXT_NAVY

    p_sum = tf_sim.add_paragraph()
    p_sum.text = "\nFAZIT DER STÖRUNGSTESTS:\n• 100 % Erkennungsrate aller Ausfälle in durchschnittlich unter 65 Sekunden.\n• Automatische Entwarnung: Nach Behebung sprangen alle Checks ohne manuelles Zutun wieder auf OK (Grün) zurück."
    p_sum.font.size = Pt(10.5)
    p_sum.font.color.rgb = C_PRIMARY

    set_notes(s11, """[ZEIT: 11:00 - 12:15 Min. | SPRECHER: Robert Ortmann]
Danke Marco! Ein Monitoring ist nur so gut, wie es im Ernstfall reagiert. Deshalb haben wir vier reale Störungen provoziert:
Test 1: Apache gestoppt. Nach 47 Sekunden meldete das Dashboard CRIT – Connection refused.
Test 2: CPU-Stresstest auf 4 Kernen. Nach 62 Sekunden Warnung, nach 75 Sekunden CRIT bei 98% Last.
Test 3: Die Festplatte künstlich vollgeschrieben. Nach genau 60 Sekunden schlug der Alarm bei über 95% Füllstand an.
Test 4: Der harte Host-Crash – VM ausgeschaltet. Nach 127 Sekunden meldete Checkmk 'Host DOWN, PING failed'.
Fazit: 100% Trefferquote in unter 2 Minuten, und nach Behebung sprangen alle Checks ohne manuellen Eingriff wieder auf Grün.""")

    # ==========================================
    # SLIDE 12: DATENANALYSE
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "Kapitel 10", "Datenanalyse & Schwellwert-Validierung (Abgabeprodukt I)", "Untersuchung der Messkurven und Bestätigung der praxistauglichen Grenzwerte")

    analyses = [
        ("Messgröße 1: CPU-Auslastung", C_PRIMARY, [
            "Normalbetrieb: 5 bis 15 % Grundlast.",
            "Störfall: Steiler Anstieg auf 98–100 %.",
            "Validierung: Schwelle bei 80 % mit 5-Minuten-Zeitfenster filtert kurzzeitige Update-Spitzen zuverlässig heraus.",
            "Ergebnis: Kein Fehlalarm-Risiko, maximaler Schutz."
        ]),
        ("Messgröße 2: Festplattenbelegung", C_BLUE, [
            "Normalbetrieb: Flacher Verlauf bei ca. 37 %.",
            "Störfall: Steiler Füllkurvenanstieg auf über 95 %.",
            "Validierung: Warnstufe bei 85 % lässt Admins mehrere Tage Reaktionszeit für Log-Bereinigungen.",
            "Ergebnis: Verhindert Datenverlust und Dienststillstand."
        ]),
        ("Messgröße 3: HTTP-Verfügbarkeit", RGBColor(147, 51, 234), [
            "Normalbetrieb: Stabile Antwortzeiten unter 15 ms.",
            "Störfall: Sofortiger Ausschlag auf Connection Refused.",
            "Validierung: Schwelle bei 2,0s (Warn) und 5,0s (Crit) schützt Kunden vor quälend langsamen Ladezeiten.",
            "Ergebnis: Essentiell für geschäftskritische Webdienste."
        ])
    ]

    for i, (title, col, bullets) in enumerate(analyses):
        c = add_card(s12, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(5.0))
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = C_TEXT_BODY

    set_notes(s12, """[ZEIT: 12:15 - 13:00 Min. | SPRECHER: Robert Ortmann]
In Abgabeprodukt I haben wir die Datenverläufe analysiert. Warum sind unsere Schwellwerte genau so gewählt?
Bei der CPU brauchen wir ein 5-Minuten-Zeitfenster bei 80%, damit ein kurzes apt-upgrade keinen Fehlalarm auslöst.
Bei der Festplatte lässt eine Warnschwelle bei 85% den Admins genügend Zeit zur Bereinigung, bevor das System kollabiert.
Und bei HTTP ist die Sache binär: Reagiert der Webserver länger als 5 Sekunden, können Mitarbeiter nicht arbeiten – hier ist sofortiges Handeln Pflicht. Unsere Grenzwerte haben sich als absolut praxistauglich erwiesen.""")

    # ==========================================
    # SLIDE 13: HERAUSFORDERUNGEN & LESSONS LEARNED
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    add_bg(s13)
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
        p.font.color.rgb = C_PRIMARY
        for d in desc:
            pd = tf.add_paragraph()
            pd.text = f"   • {d}"
            pd.font.size = Pt(10.5)
            pd.font.color.rgb = C_TEXT_BODY

    set_notes(s13, """[ZEIT: 13:00 - 13:45 Min. | SPRECHER: Robert Ortmann]
Natürlich lief in den drei Tagen nicht alles auf Knopfdruck. Zwei echte Herausforderungen:
Erstens: Paketkonflikte auf Ubuntu 26.04. Unsere Lösung war der offizielle Docker-Container – damit läuft Checkmk komplett isoliert, stabil und startet bei jedem Booten automatisch.
Zweitens: MariaDB lauschte standardmäßig nur auf 127.0.0.1. Wir haben das Bind-Address-Setting angepasst, damit die Datenbank über das Netzwerk überwacht werden kann.
Unsere wichtigste Lesson Learned: Eine saubere Netzwerkplanung vorab spart hintenraus Stunden an Fehlersuche.""")

    # ==========================================
    # SLIDE 14: PROJEKTERGEBNIS
    # ==========================================
    s14 = prs.slides.add_slide(blank_layout)
    add_bg(s14)
    add_header(s14, "Kapitel 12", "Projektergebnis & Zielerreichung (Abgabeprodukt J)", "Alle 11 MUSS-Anforderungen zu 100 % erfüllt • Strukturierter Abnahmetest bestanden")

    kpis = [
        ("MUSS-Anforderungen", "11 / 11", "100 % erfüllt", C_PRIMARY),
        ("KANN-Anforderungen", "3 / 5", "60 % umgesetzt", C_BLUE),
        ("Störungsprüfungen", "4 / 4", "100 % erkannt", C_PRIMARY),
        ("Abnahmetests (T01–T12)", "13 / 13", "100 % bestanden", C_PRIMARY)
    ]

    for i, (label, val, sub, col) in enumerate(kpis):
        c = add_card(s14, Inches(0.8 + i * 2.95), Inches(1.8), Inches(2.8), Inches(2.0), C_CARD_BG, col)
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = label.upper()
        p.font.size = Pt(10)
        p.font.color.rgb = C_TEXT_MUTED
        pv = tf.add_paragraph()
        pv.text = val
        pv.font.size = Pt(32)
        pv.font.bold = True
        pv.font.color.rgb = col
        ps = tf.add_paragraph()
        ps.text = sub
        ps.font.size = Pt(11)
        ps.font.bold = True
        ps.font.color.rgb = C_TEXT_NAVY

    c_fazit = add_card(s14, Inches(0.8), Inches(4.1), Inches(11.7), Inches(2.7), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    tf_f = c_fazit.text_frame
    tf_f.word_wrap = True
    p = tf_f.paragraphs[0]
    p.text = "🏆 Fazit des Proof of Concept:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY

    fazit_pts = [
        "Die Checkmk Raw Edition 2.3 hat bewiesen, dass sie die Anforderungen der Müller & Partner GmbH vollständig erfüllt.",
        "Der Zeitrahmen von 3 Projekttagen (geplant: 39,0 h | Ist: 41,5 h) wurde mit einer minimalen Abweichung von +6,4 % eingehalten.",
        "Die Lösung arbeitet ressourcenschonend, benötigt keine teuren Lizenzen und ist sofort einsatzbereit."
    ]
    for fp in fazit_pts:
        pfp = tf_f.add_paragraph()
        pfp.text = f"✓ {fp}"
        pfp.font.size = Pt(11)
        pfp.font.color.rgb = C_TEXT_NAVY

    set_notes(s14, """[ZEIT: 13:45 - 14:15 Min. | SPRECHER: Jan Kluth]
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
    add_bg(s15)
    add_header(s15, "Kapitel 13", "Empfehlung & 3-Phasen-Rollout-Fahrplan", "Konkrete Handlungsempfehlung für die Geschäftsführung zur Produktivübernahme")

    phases = [
        ("Phase 1 (Woche 1–2)", "Pilotbetrieb auf Kernsystemen", C_PRIMARY, [
            "Installation auf dedizierter Hardware/VM.",
            "Anbindung der 10 kritischsten Server (Active Directory, DNS, ERP, File-Server).",
            "Einarbeitung des internen IT-Teams in die WATO-Administration."
        ]),
        ("Phase 2 (Woche 3–4)", "Vollständiger Rollout", C_BLUE, [
            "Erfassung aller Arbeitsplatz-PCs und NAS-Speicher über Windows/Linux-Agenten.",
            "Einrichtung der E-Mail- und SMS-Benachrichtigungsketten.",
            "Feintuning der Schwellwerte für den Normalbetrieb."
        ]),
        ("Phase 3 (Monat 2)", "Erweiterung & Netzinfrastruktur", RGBColor(147, 51, 234), [
            "Anbindung von Netzwerkswitches und Routern via SNMP.",
            "Zentrales Log-Monitoring und Auswertung historischer Daten.",
            "Kapazitätsplanung für zukünftiges Hardware-Wachstum."
        ])
    ]

    for i, (p_title, p_sub, color, steps) in enumerate(phases):
        c = add_card(s15, Inches(0.8 + i * 3.95), Inches(1.8), Inches(3.8), Inches(5.0))
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
        pv.font.color.rgb = C_TEXT_NAVY
        for s in steps:
            ps = tf.add_paragraph()
            ps.text = f"• {s}"
            ps.font.size = Pt(10.5)
            ps.font.color.rgb = C_TEXT_BODY

    set_notes(s15, """[ZEIT: 14:15 - 14:45 Min. | SPRECHER: Jan Kluth]
Unsere klare Handlungsempfehlung an die Geschäftsführung der Müller & Partner GmbH lautet daher: Checkmk Raw Edition sollte fest in den Produktivbetrieb übernommen werden.
Wir empfehlen einen 3-Phasen-Rollout:
Phase 1 in den ersten zwei Wochen: Ein dedizierter Server für Checkmk und die Anbindung der 10 kritischsten Kernserver.
Phase 2 im ersten Monat: Kompletter Rollout auf alle Clients und NAS-Systeme plus E-Mail-Alarmierungsketten.
Phase 3: SNMP-Überwachung der Switche und historische Kapazitätsplanung.""")

    # ==========================================
    # SLIDE 16: ABSCHLUSS & LIVE-DEMO
    # ==========================================
    s16 = prs.slides.add_slide(blank_layout)
    add_bg(s16)

    c_icon = add_card(s16, Inches(5.8), Inches(1.0), Inches(1.7), Inches(1.2), C_PRIMARY_LIGHT, C_PRIMARY_BORDER)
    p = c_icon.text_frame.paragraphs[0]
    p.text = "✓"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p.alignment = PP_ALIGN.CENTER

    tb_end = s16.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(11.7), Inches(1.6))
    tf_e = tb_end.text_frame
    tf_e.word_wrap = True
    p1 = tf_e.paragraphs[0]
    p1.text = "Vielen Dank für Ihre Aufmerksamkeit!"
    p1.font.size = Pt(34)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_NAVY
    p1.alignment = PP_ALIGN.CENTER
    p2 = tf_e.add_paragraph()
    p2.text = "Wir stehen nun für Ihre Fragen und die Live-Demonstration zur Verfügung."
    p2.font.size = Pt(15)
    p2.font.color.rgb = C_TEXT_MUTED
    p2.alignment = PP_ALIGN.CENTER

    # Live-Demo Access Card
    c_demo = add_card(s16, Inches(2.5), Inches(4.2), Inches(8.3), Inches(2.6), C_CARD_BG, C_PRIMARY_BORDER)
    tf_d = c_demo.text_frame
    tf_d.word_wrap = True
    p = tf_d.paragraphs[0]
    p.text = "🖥️ LIVE-DEMONSTRATION BEREIT:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_PRIMARY
    p.alignment = PP_ALIGN.CENTER
    p_info = tf_d.add_paragraph()
    p_info.text = "\n• Checkmk Web-GUI: http://localhost:8080/cmk/  |  Login: cmkadmin / cmkadmin\n• Live-Systeme: mon-srv01 (.101)  •  web-srv01 (.102)  •  win-client01 (.1)\n• Live-Störungstest auf Abruf bereit: systemctl stop apache2 (HTTP CRIT)"
    p_info.font.size = Pt(11)
    p_info.font.color.rgb = C_TEXT_NAVY
    p_info.alignment = PP_ALIGN.CENTER

    pptx_path = r"C:\Users\erolt\Desktop\monitor\IT-Monitoring_Praesentation.pptx"
    prs.save(pptx_path)
    print(f"Clean light PPTX saved successfully: {pptx_path}")

    # Export to PDF via PowerPoint COM
    pdf_path = r"C:\Users\erolt\Desktop\monitor\IT-Monitoring_Praesentation.pdf"
    try:
        ppt_app = win32com.client.Dispatch("PowerPoint.Application")
        deck = ppt_app.Presentations.Open(pptx_path, WithWindow=False)
        deck.SaveAs(pdf_path, 32) # 32 = ppSaveAsPDF
        deck.Close()
        print(f"Clean light PDF exported successfully: {pdf_path}")
    except Exception as e:
        print(f"PDF export warning: {e}")

if __name__ == "__main__":
    build_presentation()
