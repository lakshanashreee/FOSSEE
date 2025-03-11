@echo off
setlocal

REM Define error log file
set ERROR_LOG="error_log.txt"

REM Clear previous error log
if exist %ERROR_LOG% del %ERROR_LOG%

REM Run OSI file validation script once for all files
python validate_osi.py >> %ERROR_LOG% 2>&1

REM Display error log
type %ERROR_LOG%

REM Keep window open for review
pause
