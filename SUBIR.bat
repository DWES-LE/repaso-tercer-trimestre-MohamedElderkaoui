@echo off

:LOOP
git add .
git commit -m "fecha %date% hora %time% sitio %cd% ciudad %location%"
git push

timeout /t 600 > nul
goto LOOP
