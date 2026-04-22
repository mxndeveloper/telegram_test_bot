# build_with_secrets.ps1
Write-Host "=== Build Docker image with embedded secrets ===" -ForegroundColor Cyan

$botToken = Read-Host -Prompt "Enter your BOT_TOKEN" -AsSecureString
$botTokenPlain = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($botToken))

$webhookUrl = Read-Host -Prompt "Enter your WEBHOOK_URL (e.g., https://your-app.bothost.ru/webhook)"

$webhookSecret = Read-Host -Prompt "Enter your WEBHOOK_SECRET (any random string)" -AsSecureString
$webhookSecretPlain = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($webhookSecret))

Write-Host "Building Docker image bothost-bot:latest ..." -ForegroundColor Yellow

docker build `
  --build-arg BOT_TOKEN="$botTokenPlain" `
  --build-arg WEBHOOK_URL="$webhookUrl" `
  --build-arg WEBHOOK_SECRET="$webhookSecretPlain" `
  -t bothost-bot:latest .

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Image built successfully. Now export it with:" -ForegroundColor Green
    Write-Host "docker save bothost-bot:latest -o bothost-bot.tar" -ForegroundColor Cyan
} else {
    Write-Host "❌ Build failed. Check error messages." -ForegroundColor Red
}