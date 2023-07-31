while ($true) {
    $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $location = Get-Location
    $city = "Tu Ciudad"  # Reemplaza "Tu Ciudad" con el nombre de tu ciudad

    Write-Output "Ejecutando git add ."
    git add .

    Write-Output "Ejecutando git commit"
    git commit -m "fecha $date sitio $location ciudad $city"

    Write-Output "Ejecutando git push"
    git push

    Write-Output "Esperando 10 minutos..."
    Start-Sleep -Seconds 600
}
