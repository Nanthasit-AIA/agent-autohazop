<#
    Start the whole stack on this machine.

        .\scripts\local-start.ps1              # UI :3000, extraction :8000, HAZOP :5000
        .\scripts\local-start.ps1 -Tunnel      # ...plus a public Cloudflare URL

    Reads LITELLM_API_KEY and OPENAI_API_KEY from .env at the repo root.
    Creates services/pid-extract/.venv on first run.

    Stop everything with .\scripts\local-stop.ps1
#>
param(
    [switch]$Tunnel,
    [string]$Model = "gpt-5.5",
    [string]$DemoToken = ""
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

# ---------- secrets ----------
$envFile = Join-Path $root ".env"
if (-not (Test-Path $envFile)) {
    Write-Host "No .env at the repo root. Copy .env.example to .env and fill in LITELLM_API_KEY." -ForegroundColor Red
    exit 1
}
$vals = @{}
foreach ($line in Get-Content $envFile) {
    if ($line -match '^\s*([A-Z_][A-Z0-9_]*)\s*=\s*(.*)$') { $vals[$Matches[1]] = $Matches[2].Trim().Trim('"') }
}
if (-not $vals["LITELLM_API_KEY"]) { Write-Host "LITELLM_API_KEY missing from .env" -ForegroundColor Red; exit 1 }

# ---------- python env for the extraction service ----------
$venv = Join-Path $root "services\pid-extract\.venv"
$py = Join-Path $venv "Scripts\python.exe"
if (-not (Test-Path $py)) {
    Write-Host "Creating services/pid-extract/.venv (first run only)..." -ForegroundColor Cyan
    python -m venv $venv
    & $py -m pip install -q --upgrade pip
    & $py -m pip install -q -r (Join-Path $root "services\pid-extract\requirements.txt")
}

$store = Join-Path $root "backend\static\store"
New-Item -ItemType Directory -Force -Path (Join-Path $store "results") | Out-Null
$seed = Join-Path $root "backend\static\data\*.json"
if (Test-Path $seed) { Copy-Item $seed (Join-Path $store "results") -Force -ErrorAction SilentlyContinue }

function Start-Svc($name, $file, $argList, $workDir, $envVars) {
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $file
    $psi.Arguments = $argList
    $psi.WorkingDirectory = $workDir
    $psi.UseShellExecute = $false
    foreach ($k in $envVars.Keys) { $psi.EnvironmentVariables[$k] = [string]$envVars[$k] }
    $p = [System.Diagnostics.Process]::Start($psi)
    Write-Host ("  {0,-22} pid {1}" -f $name, $p.Id) -ForegroundColor Green
}

$baseUrl = $vals["LITELLM_BASE_URL"]
if (-not $baseUrl) { $baseUrl = "https://scgc-llmproxy.scg.com" }

Write-Host "`nStarting services..." -ForegroundColor Cyan

# 1. P&ID extraction API
Start-Svc "extraction :8000" $py "app.py" (Join-Path $root "services\pid-extract") @{
    PORT = "8000"; PYTHONUNBUFFERED = "1"
    LITELLM_BASE_URL = $baseUrl
    LITELLM_API_KEY = $vals["LITELLM_API_KEY"]
    EXTRACT_MODEL = $Model
    STORAGE_BACKEND = "local"; LOCAL_STORE_DIR = $store
    ALLOWED_ORIGINS = "*"; DEMO_TOKEN = $DemoToken
}

# 2. HAZOP agent (uses the venv from the main checkout)
$hazopPy = "C:\Users\idtcu\agent-autohazop\backend\aah01lib\Scripts\python.exe"
if (Test-Path $hazopPy) {
    Start-Svc "HAZOP :5000" $hazopPy "app.py" (Join-Path $root "backend") @{
        PYTHONUNBUFFERED = "1"
        OPENAI_API_KEY = $vals["OPENAI_API_KEY"]
        DEMO_TOKEN = $DemoToken
    }
} else {
    Write-Host "  HAZOP :5000          skipped - venv not found at $hazopPy" -ForegroundColor Yellow
}

# 3. Nuxt UI. Empty API bases keep everything same-origin through the dev proxy.
Start-Svc "UI :3000" "cmd.exe" "/c npm run dev -- --host 0.0.0.0" $root @{
    NUXT_PUBLIC_EXTRACT_API_BASE = ""
    NUXT_PUBLIC_HAZOP_API_BASE = ""
    NUXT_PUBLIC_DEMO_TOKEN = $DemoToken
}

# 4. Optional public URL
if ($Tunnel) {
    $cf = "C:\Users\idtcu\cloudflared.exe"
    if (Test-Path $cf) {
        Start-Svc "cloudflared" $cf "tunnel --url http://127.0.0.1:3000 --no-autoupdate" $root @{}
        Write-Host "`n  The public URL is random and appears in cloudflared's own output." -ForegroundColor Yellow
        Write-Host "  It changes every restart." -ForegroundColor Yellow
    } else {
        Write-Host "  cloudflared          not found at $cf" -ForegroundColor Yellow
    }
}

Write-Host "`nUI will be ready at http://localhost:3000 in ~20s (first start is slower)." -ForegroundColor Cyan
Write-Host "Stop everything: .\scripts\local-stop.ps1`n" -ForegroundColor Cyan
