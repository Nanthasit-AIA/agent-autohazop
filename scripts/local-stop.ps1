<#
    Stop everything started by local-start.ps1.

        .\scripts\local-stop.ps1

    Only touches ports 3000 / 5000 / 8000 and cloudflared, so nothing else on
    the machine is affected. Azure is untouched - see infra/README.md for that.
#>
$ports = @(3000, 5000, 8000)
$stopped = 0

foreach ($port in $ports) {
    $conns = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
    if (-not $conns) { Write-Host ("  port {0,-5} already stopped" -f $port) -ForegroundColor DarkGray; continue }

    foreach ($procId in ($conns.OwningProcess | Select-Object -Unique)) {
        $p = Get-Process -Id $procId -ErrorAction SilentlyContinue
        if (-not $p) { continue }
        try {
            Stop-Process -Id $procId -Force -ErrorAction Stop
            Write-Host ("  port {0,-5} stopped {1} (pid {2})" -f $port, $p.ProcessName, $procId) -ForegroundColor Green
            $stopped++
        } catch {
            Write-Host ("  port {0,-5} could not stop pid {1}: {2}" -f $port, $procId, $_) -ForegroundColor Red
        }
    }
}

# Flask's reloader and npm both spawn children that can keep a port held.
Start-Sleep -Seconds 2
foreach ($port in $ports) {
    $again = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
    if ($again) {
        foreach ($procId in ($again.OwningProcess | Select-Object -Unique)) {
            try { Stop-Process -Id $procId -Force -ErrorAction Stop; Write-Host ("  port {0,-5} stopped leftover child (pid {1})" -f $port, $procId) -ForegroundColor Green }
            catch { }
        }
    }
}

$cf = Get-Process cloudflared -ErrorAction SilentlyContinue
if ($cf) {
    $cf | Stop-Process -Force -ErrorAction SilentlyContinue
    Write-Host "  cloudflared stopped - the public URL is now dead" -ForegroundColor Green
    $stopped++
} else {
    Write-Host "  cloudflared already stopped" -ForegroundColor DarkGray
}

Start-Sleep -Seconds 1
Write-Host "`nFinal state:" -ForegroundColor Cyan
foreach ($port in $ports) {
    $c = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
    if ($c) { Write-Host ("  port {0,-5} STILL LISTENING" -f $port) -ForegroundColor Red }
    else { Write-Host ("  port {0,-5} free" -f $port) -ForegroundColor Green }
}
Write-Host ""
