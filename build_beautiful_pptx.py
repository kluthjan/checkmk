import collections
import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
import os
import win32com.client
import time

def create_beautiful_presentation(pptx_path):
    prs = Presentation()
    
    # Set slide dimensions to 16:9
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Colors
    BG_COLOR = RGBColor(15, 23, 42)      # Slate 900 (Dark background)
    ACCENT_COLOR = RGBColor(16, 185, 129) # Emerald 500 (Green accent for Checkmk)
    TEXT_LIGHT = RGBColor(241, 245, 249) # Slate 100
    TEXT_MUTED = RGBColor(148, 163, 184) # Slate 400
    CARD_BG = RGBColor(30, 41, 59)       # Slate 800

    def apply_bg(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR

    def add_header(slide, title_text):
        # Decorative top bar
        top_bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.1)
        )
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = ACCENT_COLOR
        top_bar.line.color.rgb = ACCENT_COLOR
        
        # Title
        txBox = slide.shapes.add_textbox(Inches(0.5), Inches(0.4), Inches(12), Inches(1))
        tf = txBox.text_frame
        p = tf.add_paragraph()
        p.text = title_text
        p.font.size = Pt(44)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = notes_text

    # --- Slide 1: Title Slide ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    
    # Graphic element: large accent box on the left
    left_box = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.5), Inches(7.5)
    )
    left_box.fill.solid()
    left_box.fill.fore_color.rgb = ACCENT_COLOR
    left_box.line.color.rgb = ACCENT_COLOR

    # Main Title
    txBox = slide.shapes.add_textbox(Inches(1.5), Inches(2), Inches(10), Inches(1.5))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "IT-Monitoring mit Checkmk"
    p.font.size = Pt(64)
    p.font.bold = True
    p.font.color.rgb = TEXT_LIGHT

    # Subtitle
    txBox = slide.shapes.add_textbox(Inches(1.5), Inches(3.2), Inches(10), Inches(1))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "Proof of Concept für Müller & Partner GmbH"
    p.font.size = Pt(32)
    p.font.color.rgb = ACCENT_COLOR

    # Team Names in a nice card
    card = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(5.5), Inches(10.5), Inches(1.2)
    )
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BG
    
    txBox = slide.shapes.add_textbox(Inches(1.7), Inches(5.6), Inches(10.1), Inches(1))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "Projektteam:\nJan Kluth | Marion Ballcke | Mathias Vorrau | Marco Schmidt | Robert Ortmann"
    p.font.size = Pt(22)
    p.font.color.rgb = TEXT_LIGHT
    p.alignment = PP_ALIGN.CENTER

    add_notes(slide, "Jan (0-2 Min):\nHerzlich willkommen zur Präsentation unseres Proof of Concepts für das neue IT-Monitoring der Müller & Partner GmbH. Wir sind das Grone Umschulungsteam: Jan, Marion, Mathias, Marco und Robert. Wir stellen Ihnen heute vor, wie wir in drei Tagen eine moderne, zentrale Überwachungslösung evaluiert und prototypisch umgesetzt haben.")

    # --- Slide 2: Ausgangslage & Zielsetzung ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    add_header(slide, "Ausgangslage & Zielsetzung")
    
    # Two columns layout
    # Left column: Ausgangslage
    card1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.5), Inches(5.9), Inches(5))
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = CARD_BG
    
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(5.3), Inches(4.5))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.add_paragraph()
    p.text = "Bisherige Situation"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR
    
    points = [
        "Wachsende IT-Infrastruktur",
        "Bisher manuelle Systemüberwachung",
        "Verzögerte Störungsmeldungen",
        "Gefahr von unbemerkten Ausfällen"
    ]
    for pt in points:
        p = tf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(24)
        p.font.color.rgb = TEXT_LIGHT
        p.space_before = Pt(14)

    # Right column: Zielsetzung
    card2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.5), Inches(5.9), Inches(5))
    card2.fill.solid()
    card2.fill.fore_color.rgb = CARD_BG
    card2.line.color.rgb = CARD_BG
    
    txBox = slide.shapes.add_textbox(Inches(7.2), Inches(1.8), Inches(5.3), Inches(4.5))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.add_paragraph()
    p.text = "Projektziele"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR
    
    points = [
        "Evaluation & Systemauswahl",
        "Planung der Architektur",
        "Prototypische Implementierung",
        "Zentrales Open-Source-Monitoring"
    ]
    for pt in points:
        p = tf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(24)
        p.font.color.rgb = TEXT_LIGHT
        p.space_before = Pt(14)

    add_notes(slide, "Jan (2-3 Min):\nDie Müller & Partner GmbH hat eine wachsende IT-Infrastruktur. Bisher wurde alles manuell überwacht. Das Problem: Störungen werden zu spät erkannt, Ausfälle bleiben unbemerkt. Unser Ziel war es daher, in diesem PoC ein zentrales Open-Source-Monitoringsystem zu evaluieren, zu planen und prototypisch umzusetzen.")

    # --- Slide 3: Nutzwertanalyse ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    add_header(slide, "Nutzwertanalyse & Systemauswahl")

    # Top intro text
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(12), Inches(0.5))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "Wir haben drei marktführende Open-Source Lösungen evaluiert:"
    p.font.size = Pt(28)
    p.font.color.rgb = TEXT_LIGHT

    # Three columns for the three systems
    systems = [
        ("Checkmk Raw", "4,40 / 5,00", ACCENT_COLOR, True),
        ("Zabbix", "4,20 / 5,00", TEXT_MUTED, False),
        ("Nagios Core", "3,30 / 5,00", TEXT_MUTED, False)
    ]
    
    for i, (name, score, color, is_winner) in enumerate(systems):
        x = Inches(0.5 + i*4.2)
        y = Inches(2.5)
        w = Inches(3.9)
        h = Inches(3)
        
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = color if is_winner else CARD_BG
        if is_winner:
            card.line.width = Pt(3)
            
        txBox = slide.shapes.add_textbox(x+Inches(0.2), y+Inches(0.5), w-Inches(0.4), Inches(2))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.add_paragraph()
        p.text = name
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = color
        p.alignment = PP_ALIGN.CENTER
        
        p = tf.add_paragraph()
        p.text = score
        p.font.size = Pt(28)
        p.font.color.rgb = TEXT_LIGHT
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(20)

    # Winner explanation
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(5.8), Inches(12), Inches(1))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.add_paragraph()
    p.text = "Entscheidung: Checkmk aufgrund hervorragender Bedienbarkeit (höchste Gewichtung: 20%), Out-of-the-Box Dashboards und zeitsparender Auto-Discovery."
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR

    add_notes(slide, "Marion (3-6 Min):\nUm das beste System zu finden, haben wir eine Nutzwertanalyse durchgeführt. Evaluiert wurden Checkmk, Zabbix und Nagios anhand von 7 Kriterien, darunter Kosten, Bedienbarkeit und Alarmierung.\n\nDas Ergebnis: Checkmk Raw Edition hat mit 4,40 Punkten gewonnen, dicht gefolgt von Zabbix mit 4,20. Nagios landete bei 3,30.\n\nAusschlaggebend für Checkmk war die extrem gute Bedienbarkeit - das am höchsten gewichtete Kriterium - sowie die sofort einsatzbereiten Dashboards und die automatische Erkennung von Diensten (Auto-Discovery).")

    # --- Slide 4: Technische Architektur ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    add_header(slide, "Technische Architektur der Testumgebung")

    # Draw nodes for architecture
    nodes = [
        ("Ubuntu VM", "Monitoring Server\n(Checkmk Docker, Port 8080)", Inches(0.5), Inches(2.5)),
        ("Web-Srv01 VM", "Linux Webserver\n(Apache, MySQL, SSH)", Inches(5.0), Inches(2.5)),
        ("Windows Host", "Windows Client\n(Checkmk Agent)", Inches(9.5), Inches(2.5))
    ]

    for title, desc, x, y in nodes:
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.3), Inches(2.5))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = ACCENT_COLOR
        card.line.width = Pt(2)
        
        txBox = slide.shapes.add_textbox(x, y+Inches(0.2), Inches(3.3), Inches(2))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.add_paragraph()
        p.text = title
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = TEXT_LIGHT
        p.alignment = PP_ALIGN.CENTER
        
        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(20)
        p.font.color.rgb = TEXT_MUTED
        p.alignment = PP_ALIGN.CENTER
        p.space_before = Pt(10)

    # Arrows/Connections
    line1 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(3.8), Inches(3.5), Inches(1.2), Inches(0.5))
    line1.fill.solid()
    line1.fill.fore_color.rgb = ACCENT_COLOR
    line1.line.color.rgb = ACCENT_COLOR
    
    line2 = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(8.3), Inches(3.5), Inches(1.2), Inches(0.5))
    line2.fill.solid()
    line2.fill.fore_color.rgb = ACCENT_COLOR
    line2.line.color.rgb = ACCENT_COLOR

    # Network details
    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(12), Inches(1.5))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "Netzwerk: VirtualBox Host-Only Adapter (192.168.56.0/24)"
    p.font.size = Pt(24)
    p.font.color.rgb = TEXT_LIGHT
    p.space_after = Pt(10)
    p2 = tf.add_paragraph()
    p2.text = "Kommunikation: Alle Systeme sicher vernetzt, lokales Port-Forwarding eingerichtet."
    p2.font.size = Pt(24)
    p2.font.color.rgb = TEXT_LIGHT

    add_notes(slide, "Mathias (6-9 Min):\nFür die Umsetzung haben wir drei Systeme aufgesetzt:\n1. Einen Ubuntu-Server als Monitoring-Zentrale mit Checkmk im Docker-Container.\n2. Einen Linux-Webserver (web-srv01) mit Apache, MySQL und SSH.\n3. Den Windows-Host-PC als Client.\n\nAlle Systeme kommunizieren über ein isoliertes VirtualBox Host-Only Netzwerk. Über Port-Forwarding machen wir das Dashboard lokal erreichbar.")

    # --- Slide 5: Monitoring in der Praxis ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    add_header(slide, "Monitoring-Konfiguration & Custom Checks")

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.5), Inches(12.333), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BG

    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.5), Inches(5))
    tf = txBox.text_frame
    tf.word_wrap = True
    
    p = tf.add_paragraph()
    p.text = "Automatisierung & Dienste"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR

    points = [
        "Hosts über REST-API angelegt",
        "Auto-Discovery erkannte sofort 19 Services auf Ubuntu und 22 auf web-srv01",
        "Überwachte Dienste (MUSS): HTTP, MySQL, SSH"
    ]
    for pt in points:
        p = tf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(24)
        p.font.color.rgb = TEXT_LIGHT
        p.space_before = Pt(10)

    p = tf.add_paragraph()
    p.text = "Custom Local Check (Python)"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR
    p.space_before = Pt(30)

    p = tf.add_paragraph()
    p.text = "• Wir haben ein eigenes Python-Skript entwickelt, das aktive TCP-Verbindungen überwacht."
    p.font.size = Pt(24)
    p.font.color.rgb = TEXT_LIGHT
    p.space_before = Pt(10)
    
    p = tf.add_paragraph()
    p.text = "• Schwellwerte: WARN bei 100, CRIT bei 200 Verbindungen."
    p.font.size = Pt(24)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(slide, "Marco (9-12 Min):\nDie Einrichtung ging dank Checkmk sehr schnell. Über die Auto-Discovery-Funktion wurden fast alle Dienste sofort erkannt.\n\nGemäß den Anforderungen überwachen wir Apache, MySQL und SSH inklusive Schwellwerten für Reaktionszeiten.\n\nZusätzlich haben wir einen 'Custom Local Check' in Python geschrieben. Dieser überwacht die Anzahl der aktiven TCP-Verbindungen auf dem Webserver und alarmiert uns bei Überlastung (Warnung bei 100, Kritisch bei 200 Verbindungen).")

    # --- Slide 6: Störungssimulation ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    add_header(slide, "Störungssimulation & Tests")

    txBox = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(12), Inches(0.5))
    tf = txBox.text_frame
    p = tf.add_paragraph()
    p.text = "Vier praxisnahe Szenarien erfolgreich getestet:"
    p.font.size = Pt(26)
    p.font.color.rgb = TEXT_LIGHT

    scenarios = [
        ("Apache-Ausfall", "Service gestoppt", "HTTP_Apache → CRIT"),
        ("CPU-Volllast", "Stress-Test (stress --cpu)", "CPU utilization → WARN/CRIT"),
        ("Festplatte voll", "dd command für 20GB", "Filesystem / → CRIT"),
        ("Host-Ausfall", "VM ausgeschaltet", "Host DOWN (Ping Fail)")
    ]

    y_pos = 2.0
    for name, action, result in scenarios:
        # Row card
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(y_pos), Inches(12.333), Inches(1.1))
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BG
        
        # Icon / Circle
        circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.8), Inches(y_pos+0.25), Inches(0.6), Inches(0.6))
        circle.fill.solid()
        circle.fill.fore_color.rgb = ACCENT_COLOR
        circle.line.color.rgb = ACCENT_COLOR
        
        tx = slide.shapes.add_textbox(Inches(1.6), Inches(y_pos+0.1), Inches(3.5), Inches(0.9))
        tx.text_frame.add_paragraph().text = name
        tx.text_frame.paragraphs[0].font.size = Pt(28)
        tx.text_frame.paragraphs[0].font.bold = True
        tx.text_frame.paragraphs[0].font.color.rgb = TEXT_LIGHT
        
        tx2 = slide.shapes.add_textbox(Inches(5.0), Inches(y_pos+0.1), Inches(4.0), Inches(0.9))
        tx2.text_frame.add_paragraph().text = action
        tx2.text_frame.paragraphs[0].font.size = Pt(22)
        tx2.text_frame.paragraphs[0].font.color.rgb = TEXT_MUTED
        
        tx3 = slide.shapes.add_textbox(Inches(9.0), Inches(y_pos+0.1), Inches(3.5), Inches(0.9))
        tx3.text_frame.add_paragraph().text = result
        tx3.text_frame.paragraphs[0].font.size = Pt(24)
        tx3.text_frame.paragraphs[0].font.bold = True
        tx3.text_frame.paragraphs[0].font.color.rgb = ACCENT_COLOR
        
        y_pos += 1.3

    add_notes(slide, "Robert (12-15 Min):\nUm sicherzugehen, dass unser Monitoring funktioniert, haben wir reale Störungen simuliert.\nWir haben den Apache-Dienst gestoppt, die CPU künstlich ausgelastet, die Festplatte volllaufen lassen und schließlich einen kompletten Host-Ausfall simuliert.\n\nIn allen vier Fällen hat Checkmk sofort und zuverlässig reagiert und den Status auf CRIT gesetzt.")

    # --- Slide 7: Fazit ---
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    apply_bg(slide)
    add_header(slide, "Fazit & Ausblick")

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.5), Inches(12.333), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = CARD_BG
    card.line.color.rgb = CARD_BG
    
    txBox = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.5), Inches(5))
    tf = txBox.text_frame
    tf.word_wrap = True
    
    p = tf.add_paragraph()
    p.text = "Ergebnisse des Proof of Concept"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR

    points = [
        "Ziel zu 100% erreicht: Zentrales Monitoring in 3 Tagen aufgebaut.",
        "Checkmk Raw Edition erwies sich als die beste Wahl.",
        "Drei Hosts werden erfolgreich in Echtzeit überwacht.",
        "Störungen werden sofort erkannt, Datenverlust wird verhindert."
    ]
    for pt in points:
        p = tf.add_paragraph()
        p.text = f"• {pt}"
        p.font.size = Pt(26)
        p.font.color.rgb = TEXT_LIGHT
        p.space_before = Pt(14)

    p = tf.add_paragraph()
    p.text = "Nächste Schritte"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = ACCENT_COLOR
    p.space_before = Pt(30)
    
    p = tf.add_paragraph()
    p.text = "• Einrichtung von E-Mail-Alarmierung."
    p.font.size = Pt(26)
    p.font.color.rgb = TEXT_LIGHT
    p.space_before = Pt(14)
    
    p = tf.add_paragraph()
    p.text = "• Verschlüsselung der Agentenkommunikation (TLS)."
    p.font.size = Pt(26)
    p.font.color.rgb = TEXT_LIGHT

    add_notes(slide, "Robert (12-15 Min Fortsetzung):\nFazit: Unser PoC war ein voller Erfolg. Das zentrale Monitoring mit Checkmk steht und überwacht unsere Systeme in Echtzeit. Störungen werden sofort erkannt.\n\nAls nächste Schritte empfehlen wir die Einrichtung einer E-Mail-Alarmierung und die Aktivierung der TLS-Verschlüsselung für die sichere Datenübertragung.\n\nVielen Dank für Ihre Aufmerksamkeit! Wir beantworten nun gerne Ihre Fragen.")

    # Save
    prs.save(pptx_path)
    print(f"Präsentation gespeichert unter: {pptx_path}")

def export_to_pdf(pptx_path, pdf_path):
    print("Exportiere nach PDF...")
    try:
        powerpoint = win32com.client.Dispatch("PowerPoint.Application")
        powerpoint.Visible = 1
        
        # Versuche zuerst die Datei zu öffnen (Read-Only)
        deck = powerpoint.Presentations.Open(pptx_path, WithWindow=False)
        deck.SaveAs(pdf_path, 32) # 32 is the format code for PDF
        deck.Close()
        print(f"PDF erfolgreich exportiert unter: {pdf_path}")
    except Exception as e:
        print(f"Fehler beim PDF Export: {e}")
        # Manchmal hilft es, COM-Objekte aufzuräumen
    finally:
        try:
            powerpoint.Quit()
        except:
            pass

if __name__ == "__main__":
    work_dir = r"C:\Users\erolt\Desktop\monitor"
    pptx_filename = os.path.join(work_dir, "IT-Monitoring_Praesentation.pptx")
    pdf_filename = os.path.join(work_dir, "IT-Monitoring_Praesentation.pdf")
    
    # Generate PPTX
    create_beautiful_presentation(pptx_filename)
    
    # Small delay before PDF export
    time.sleep(2)
    
    # Export to PDF
    export_to_pdf(pptx_filename, pdf_filename)
