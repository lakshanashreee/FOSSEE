@echo off
setlocal

REM Define error log file
set ERROR_LOG="error_log.txt"

REM Clear previous error log
if exist %ERROR_LOG% del %ERROR_LOG%

REM Loop through all OSI files in the directory
for %%F in (*.osi) do (
    echo Validating: %%F >> %ERROR_LOG%
    
    REM Run Osdag CLI tool (Module Extraction)
    python -m osdag.cli_shell find-module -i "%%F" >> %ERROR_LOG% 2>&1

    REM Run OSI file validation script
    python validate_osi.py "%%F" >> %ERROR_LOG% 2>&1
)

REM Display error log
type %ERROR_LOG%

REM Keep window open for review
pause
