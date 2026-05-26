 = Get-Content "z:\All Data\Documents\Kuliah\smt6\FCT\sirubi_2\index.html" -Raw

 = "            <!-- PANEL 1: Rute Eksisting -->"
 = "            <!-- PANEL 6: Aksi Bawah (Lokasi & Reset) -->"

 = .IndexOf()
 = .IndexOf()

if ( -eq -1 -or  -eq -1) {
    Write-Host "Markers not found"
    exit 1
}

 = .Substring(0, )
 = .Substring()
 = .Substring(,  - $startIdx)

# Split by "            <!-- PANEL "
$parts = $panelsText -split "            <!-- PANEL "

$panels = @{}
foreach ($p in $parts) {
    if ([string]::IsNullOrWhiteSpace($p)) { continue }
    $fullStr = "            <!-- PANEL " + $p
    if ($p -match "^1: Rute Eksisting") { $panels["1"] = $fullStr }
    elseif ($p -match "^2: Pencarian") { $panels["2"] = $fullStr }
    elseif ($p -match "^2\.5: Filter Kategori Sekolah") { $panels["2.5"] = $fullStr }
    elseif ($p -match "^3: Legenda") { $panels["3"] = $fullStr }
    elseif ($p -match "^4: Basemap Toggle") { $panels["4"] = $fullStr }
    elseif ($p -match "^5: Rekomendasi Halte") { $panels["5"] = $fullStr }
}

$newOrder = @("2", "1", "5", "2.5", "4", "3")
$newPanelsText = ""
foreach ($k in $newOrder) {
    $newPanelsText += $panels[$k]
}

$newHtml = $prefix + $newPanelsText + $suffix

Set-Content -Path "z:\All Data\Documents\Kuliah\smt6\FCT\sirubi_2\index.html" -Value $newHtml -Encoding UTF8
Write-Host "Reordered panels successfully."
