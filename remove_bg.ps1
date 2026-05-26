Add-Type -AssemblyName System.Drawing

$imgPath = 'z:\All Data\Documents\Kuliah\smt6\FCT\sirubi_2\rekomendasi_halte.png'
$bmp = New-Object System.Drawing.Bitmap $imgPath
$width = $bmp.Width
$height = $bmp.Height

for ($x = 0; $x -lt $width; $x++) {
    for ($y = 0; $y -lt $height; $y++) {
        $pixel = $bmp.GetPixel($x, $y)
        if ($pixel.R -ge 230 -and $pixel.G -ge 230 -and $pixel.B -ge 230) {
            $bmp.SetPixel($x, $y, [System.Drawing.Color]::Transparent)
        }
    }
}

$outPath = 'z:\All Data\Documents\Kuliah\smt6\FCT\sirubi_2\rekomendasi_halte_trans.png'
$bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
