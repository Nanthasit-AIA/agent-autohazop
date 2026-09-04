<#
    Stop everything started by local-start.ps1.

        .\scripts\local-stop.ps1

    Targets ports 3000 / 5000 / 8000, this repo's own service processes, and
    cloudflared. Nothing else on the machine is touched. Azure is untouched -
    see infra/README.md for that.
#>
$ports = @(3000, 5000, 8000)
$repo = Split-Path -Parent $PSScriptRoot

function Stop-ByPort($port) {
    # Flask's reloader hands the socket to a child, and Windows keeps reporting
    # the (now dead) parent as the owner - so re-query each round rather than
    # trusting one snapshot.
    for ($i = 0; $i -lt 4; $i++) {
        $conns = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
        if (-not $conns) { return $true }
        foreach ($procId in ($conns.OwningProcess | Select-Object -Unique)) {
            if (Get-Process -Id $procId -ErrorAction SilentlyContinue) {
                Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
            }
        }
        Start-Sleep -Milliseconds 1200
    }
    return -not (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue)
}

Write-Host ""
foreach ($port in $ports) {
    $was = [bool](Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue)
    if (-not $was) { Write-Host ("  port {0,-5} already stopped" -f $port) -ForegroundColor DarkGray; continue }
    if (Stop-ByPort $port) { Write-Host ("  port {0,-5} stopped" -f $port) -ForegroundColor Green }
    else { Write-Host ("  port {0,-5} still held - see below" -f $port) -ForegroundColor Yellow }
}

# Catch orphans that survived their parent: only processes whose command line
# points into this repo or its service venv, so unrelated work is never killed.
$orphans = Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
    $_.Name -match '^(python|node)\.exe$' -and $_.CommandLine -and (
        $_.CommandLine -like "*$repo*" -or $_.CommandLine -like "*aah01lib*"
    )
}
foreach ($o in $orphans) {
    Stop-Process -Id $o.ProcessId -Force -ErrorAction SilentlyContinue
    Write-Host ("  stopped orphan {0} (pid {1})" -f $o.Name, $o.ProcessId) -ForegroundColor Green
}

$cf = Get-Process cloudflared -ErrorAction SilentlyContinue
if ($cf) {
    $cf | Stop-Process -Force -ErrorAction SilentlyContinue
    Write-Host "  cloudflared stopped - the public URL is now dead" -ForegroundColor Green
} else {
    Write-Host "  cloudflared already stopped" -ForegroundColor DarkGray
}

Start-Sleep -Seconds 2
Write-Host "`nFinal state:" -ForegroundColor Cyan
$bad = 0
foreach ($port in $ports) {
    if (Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue) {
        Write-Host ("  port {0,-5} STILL LISTENING" -f $port) -ForegroundColor Red; $bad++
    } else {
        Write-Host ("  port {0,-5} free" -f $port) -ForegroundColor Green
    }
}
if ($bad) { Write-Host "`nRun the script again, or find the holder with: netstat -ano | findstr :5000" -ForegroundColor Yellow }
Write-Host ""
