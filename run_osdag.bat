@echo off
setlocal

REM Ask user for OSI filename
set /p OSI_FILE=Enter the OSI filename: 

REM Define error log file
set ERROR_LOG="error_log.txt"

REM Clear previous error log
if exist %ERROR_LOG% del %ERROR_LOG%

REM Run OSI file validation script
python validate_osi.py %OSI_FILE% >> %ERROR_LOG% 2>&1

REM Display error log
type %ERROR_LOG%

REM Keep window open for review
pause
