#!/bin/bash
# =============================================================================
# Störungssimulation: Kritische Festplattenbelegung
# Projekt: Zentrales IT-Monitoring – Müller & Partner GmbH
# Autor: Grone Umschulungsteam
# Datum: September 2026
# Beschreibung: Füllt die Festplatte künstlich mit einer großen Datei,
#               um die Erkennung durch das Monitoring zu testen.
# =============================================================================

TESTDATEI="/tmp/monitoring_disk_test.dat"
GROESSE_MB=15000  # 15 GB Testdatei

echo "=============================================="
echo "  STÖRUNGSSIMULATION: Festplattenbelegung"
echo "=============================================="
echo ""
echo "Start:     $(date '+%Y-%m-%d %H:%M:%S')"
echo "Testdatei: ${TESTDATEI}"
echo "Größe:     ${GROESSE_MB} MB"
echo ""

# Aktuelle Belegung anzeigen
echo "[INFO] Aktuelle Festplattenbelegung:"
df -h /
echo ""

echo "[START] Erzeuge Testdatei (${GROESSE_MB} MB)..."
dd if=/dev/zero of="$TESTDATEI" bs=1M count="$GROESSE_MB" status=progress 2>&1

echo ""
echo "[INFO] Festplattenbelegung nach Simulation:"
df -h /
echo ""

echo "=============================================="
echo "  Prüfen Sie jetzt das Monitoring-Dashboard!"
echo "  Warten Sie auf WARN/CRIT-Alarme."
echo ""
echo "  Zum Aufräumen ausführen:"
echo "  rm ${TESTDATEI}"
echo "=============================================="
