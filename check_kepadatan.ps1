$json = Get-Content 'TOD/kepadatanpenduduk.geojson' -Raw | ConvertFrom-Json
$vals = $json.features | ForEach-Object { $_.properties.Kepadatan_Penduduk } | Sort-Object
$count = $vals.Count
Write-Host "Count: $count"
Write-Host "Min: $($vals[0])"
Write-Host "Max: $($vals[$count-1])"
Write-Host "Q1: $($vals[[math]::Floor($count*0.2)])"
Write-Host "Q2: $($vals[[math]::Floor($count*0.4)])"
Write-Host "Q3: $($vals[[math]::Floor($count*0.6)])"
Write-Host "Q4: $($vals[[math]::Floor($count*0.8)])"
