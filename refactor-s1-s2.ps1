# PowerShell script to refactor S1-S2 skills

# Update s1-competitor references
Get-ChildItem -Path "skills/s1-competitor/references" -Recurse -File | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $content = $content -replace 'S201', 'S101'
    $content = $content -replace 'S202', 'S102'
    $content = $content -replace 'S2-S201', 'S1-S101'
    $content = $content -replace 'S2-S202', 'S1-S102'
    $content = $content -replace 'stages/s2', 'stages/s1'
    $content = $content -replace 'S2阶段', 'S1阶段'
    Set-Content $_.FullName $content -NoNewline
}

# Update template.md
$content = Get-Content "skills/s1-competitor/template.md" -Raw
$content = $content -replace 'S201', 'S101'
$content = $content -replace 'S202', 'S102'
$content = $content -replace 'S2-S201', 'S1-S101'
$content = $content -replace 'S2-S202', 'S1-S102'
$content = $content -replace 'stages/s2', 'stages/s1'
$content = $content -replace 'S2阶段', 'S1阶段'
Set-Content "skills/s1-competitor/template.md" $content -NoNewline

Write-Host "S1-competitor updated"
