poe@echo off
setlocal

set ZIP_FILE=zipped-py.zip

:: Remove the zip file if it already exists
if exist "%ZIP_FILE%" del "%ZIP_FILE%"

:: Add all .py files from the current directory and subdirectories to the zip file, preserving the directory structure
"C:\Program Files\7-Zip\7z.exe" a -tzip "%ZIP_FILE%" ".\*.py" ".\*.toml" -r


echo Zip file created: %ZIP_FILE%
endlocal
