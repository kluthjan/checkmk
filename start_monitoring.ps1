# Checkmk Monitoring - Startskript
# Müller & Partner GmbH - POC IT-Monitoring
# ==========================================

Write-Host '=== Checkmk Monitoring Umgebung starten ===' -ForegroundColor Green
Write-Host ''

$VBoxManage = 'C:\Program Files\Oracle\VirtualBox\VBoxManage.exe'

# Prüfe ob VMs existieren
$vms = & $VBoxManage list vms
if ($vms -match 'Ubuntu') {
    Write-Host '[1/3] Starte Monitoring-Server (Ubuntu/Checkmk)...' -ForegroundColor Cyan
    & $VBoxManage startvm 'Ubuntu' --type gui
} else {
    Write-Host '[!] VM "Ubuntu" nicht gefunden!' -ForegroundColor Red
}

if ($vms -match 'web-srv01') {
    Write-Host '[2/3] Starte Webserver (web-srv01)...' -ForegroundColor Cyan
    & $VBoxManage startvm 'web-srv01' --type gui
} else {
    Write-Host '[!] VM "web-srv01" nicht gefunden!' -ForegroundColor Red
}

Write-Host ''
Write-Host '[3/3] Warte 30 Sekunden auf Boot...' -ForegroundColor Yellow
Start-Sleep -Seconds 30

Write-Host ''
Write-Host '=== Checkmk Dashboard oeffnen ===' -ForegroundColor Green
Start-Process 'http://localhost:8080/cmk/'

Write-Host ''
Write-Host 'Login-Daten:' -ForegroundColor White
Write-Host '  Benutzer: cmkadmin' -ForegroundColor White
Write-Host '  Passwort: cmkadmin' -ForegroundColor White
Write-Host ''
Write-Host 'Fertig! Das Dashboard oeffnet sich im Browser.' -ForegroundColor Green
