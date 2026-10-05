# Checkmk Monitoring - Startskript
# Müller & Partner GmbH - POC IT-Monitoring
# ==========================================

Write-Host '===================================================' -ForegroundColor Green
Write-Host '   Müller & Partner GmbH - IT-Monitoring Starter   ' -ForegroundColor Green
Write-Host '===================================================' -ForegroundColor Green
Write-Host ''

$VBoxManage = 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'
$VBoxVM = 'C:\Program Files\Oracle\VirtualBox\VirtualBoxVM.exe'

# 1. Prüfe laufende VMs
$runningVms = & $VBoxManage list runningvms

# Starte Ubuntu (Checkmk Server)
if ($runningVms -match 'Ubuntu') {
    Write-Host '[✓] Monitoring-Server (Ubuntu) laeuft bereits.' -ForegroundColor Green
    Write-Host '    Oeffne/Aktiviere GUI-Fenster...' -ForegroundColor Cyan
    Start-Process $VBoxVM -ArgumentList '--startvm "Ubuntu"'
} else {
    Write-Host '[1/3] Starte Monitoring-Server (Ubuntu/Checkmk)...' -ForegroundColor Cyan
    Start-Process $VBoxVM -ArgumentList '--startvm "Ubuntu"'
}

# Starte web-srv01 (Linux Webserver)
if ($runningVms -match 'web-srv01') {
    Write-Host '[✓] Webserver (web-srv01) laeuft bereits.' -ForegroundColor Green
    Write-Host '    Oeffne/Aktiviere GUI-Fenster...' -ForegroundColor Cyan
    Start-Process $VBoxVM -ArgumentList '--startvm "web-srv01"'
} else {
    Write-Host '[2/3] Starte Webserver (web-srv01)...' -ForegroundColor Cyan
    Start-Process $VBoxVM -ArgumentList '--startvm "web-srv01"'
}

Write-Host ''
Write-Host 'Tipp: Falls ein VM-Fenster im Hintergrund bleibt, klicke im' -ForegroundColor Yellow
Write-Host 'VirtualBox-Manager einfach oben auf "Zeigen" (gruener Pfeil)!' -ForegroundColor Yellow
Write-Host ''

# 2. Prüfe Erreichbarkeit des Checkmk Web-Ports
Write-Host '[3/3] Warte auf Initialisierung des Monitoring-Servers...' -ForegroundColor Cyan
$maxRetries = 15
$ready = $false
for ($i = 1; $i -le $maxRetries; $i++) {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:8080/cmk/" -UseBasicParsing -TimeoutSec 2 -ErrorAction Stop
        if ($response.StatusCode -eq 200) {
            $ready = $true
            break
        }
    } catch {
        Write-Host "    Warte auf Webserver... ($i/$maxRetries)" -ForegroundColor Gray
        Start-Sleep -Seconds 3
    }
}

Write-Host ''
Write-Host '=== Checkmk Dashboard oeffnen ===' -ForegroundColor Green
Start-Process 'http://localhost:8080/cmk/'

Write-Host ''
Write-Host '=== Interaktive Praesentation oeffnen ===' -ForegroundColor Green
$presPath = Join-Path $PSScriptRoot 'Nutzwertanalyse_Praesentation.html'
if (Test-Path $presPath) {
    Start-Process $presPath
}

Write-Host ''
Write-Host '===================================================' -ForegroundColor White
Write-Host '  Dashboard:    http://localhost:8080/cmk/' -ForegroundColor White
Write-Host '  Benutzer:     cmkadmin' -ForegroundColor White
Write-Host '  Passwort:     cmkadmin' -ForegroundColor White
Write-Host '===================================================' -ForegroundColor White
Write-Host 'Fertig! Dashboard und Praesentation wurden geoeffnet.' -ForegroundColor Green
