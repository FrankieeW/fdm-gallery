@echo off
set dist="%~dp0..\fdm-gallery.fda"
cd /d "%~dp0..\plugin"
del /f "%dist%" 2>nul
powershell -command "Compress-Archive -Path * -DestinationPath '%dist%'"