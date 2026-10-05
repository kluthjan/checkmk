#!/bin/bash
# =============================================================================
# Störungssimulation: Ausfall Apache-Webserver
# Projekt: Zentrales IT-Monitoring – Müller & Partner GmbH
# Autor: Grone Umschulungsteam
# Datum: September 2026
# Beschreibung: Stoppt den Apache2-Dienst, um den Ausfall eines
#               Netzwerkdienstes zu simulieren.
# =============================================================================

echo "=============================================="
echo "  STÖRUNGSSIMULATION: Apache-Webserver Ausfall"
echo "=============================================="
echo ""
echo "Zeitpunkt: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Aktuellen Status prüfen
echo "[INFO] Aktueller Apache2-Status:"
systemctl status apache2 --no-pager 2>/dev/null || echo "  Apache2 ist nicht installiert oder nicht aktiv."
echo ""

# Apache stoppen
echo "[AKTION] Stoppe Apache2-Dienst..."
sudo systemctl stop apache2

echo ""
echo "[INFO] Apache2-Status nach dem Stoppen:"
systemctl status apache2 --no-pager 2>/dev/null
echo ""

echo "=============================================="
echo "  Apache2 wurde gestoppt."
echo "  Prüfen Sie das Monitoring-Dashboard!"
echo ""
echo "  Zum Wiederherstellen:"
echo "  sudo systemctl start apache2"
echo "=============================================="
