# Agri Mitra - Push to GitHub
# Run this after creating a repo at https://github.com/new (e.g. "agri-mitra")

$repo = Read-Host "Enter your GitHub username"
if (-not $repo) { Write-Host "Cancelled."; exit 1 }

$git = "C:\Program Files\Git\bin\git.exe"
Set-Location $PSScriptRoot

& $git remote remove origin 2>$null
& $git remote add origin "https://github.com/$repo/agri-mitra.git"
& $git push -u origin main

Write-Host "Done! Your repo: https://github.com/$repo/agri-mitra"
