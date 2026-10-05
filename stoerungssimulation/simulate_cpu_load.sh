#!/bin/bash
# =============================================================================
# Störungssimulation: Hohe CPU-Auslastung
# Projekt: Zentrales IT-Monitoring – Müller & Partner GmbH
# Autor: Grone Umschulungsteam
# Datum: September 2026
# Beschreibung: Erzeugt künstlich hohe CPU-Last für die Störungssimulation.
#               Verwendet den 'stress' Befehl oder alternativ eine Bash-Schleife.
# =============================================================================

# Konfiguration
DAUER=300   # Dauer der Simulation in Sekunden (5 Minuten)
KERNE=4     # Anzahl der zu belastenden CPU-Kerne

echo "=============================================="
echo "  STÖRUNGSSIMULATION: Hohe CPU-Auslastung"
echo "=============================================="
echo ""
echo "Start:    $(date '+%Y-%m-%d %H:%M:%S')"
echo "Dauer:    ${DAUER} Sekunden"
echo "CPU-Kerne: ${KERNE}"
echo ""

# Prüfe ob 'stress' installiert ist
if command -v stress &> /dev/null; then
    echo "[INFO] Verwende 'stress' für die CPU-Lastgenerierung..."
    echo "[START] CPU-Stress wird gestartet..."
    stress --cpu "$KERNE" --timeout "$DAUER"
    echo ""
    echo "[ENDE] CPU-Stress beendet: $(date '+%Y-%m-%d %H:%M:%S')"
else
    echo "[WARNUNG] 'stress' ist nicht installiert."
    echo "[INFO] Verwende Bash-Schleifen als Alternative..."
    echo "[TIPP] Installation: sudo apt install stress"
    echo ""
    echo "[START] CPU-Last wird generiert..."
    
    # Alternative: CPU-Last durch Endlosschleifen erzeugen
    PIDS=()
    for ((i=1; i<=KERNE; i++)); do
        (while true; do :; done) &
        PIDS+=($!)
        echo "  [+] CPU-Last-Prozess $i gestartet (PID: ${PIDS[-1]})"
    done
    
    echo ""
    echo "[INFO] Warte ${DAUER} Sekunden..."
    sleep "$DAUER"
    
    # Aufräumen: Alle gestarteten Prozesse beenden
    echo ""
    echo "[AUFRÄUMEN] Beende CPU-Last-Prozesse..."
    for pid in "${PIDS[@]}"; do
        kill "$pid" 2>/dev/null
        echo "  [-] Prozess $pid beendet"
    done
    
    echo ""
    echo "[ENDE] CPU-Stress beendet: $(date '+%Y-%m-%d %H:%M:%S')"
fi

echo ""
echo "=============================================="
echo "  System sollte sich jetzt normalisieren."
echo "  Prüfen Sie das Monitoring-Dashboard!"
echo "=============================================="
