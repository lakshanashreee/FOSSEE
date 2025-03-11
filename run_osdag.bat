@echo off
setlocal

REM Define error log file
set ERROR_LOG="error_log.txt"

REM Clear previous error log
if exist %ERROR_LOG% del %ERROR_LOG%

echo Running OSI file validation...
python validate_osi.py >> %ERROR_LOG% 2>&1

echo.
echo Running Pytest for validation tests...
pytest test_validate_osi.py >> %ERROR_LOG% 2>&1

echo.
echo === Error Log ===
type %ERROR_LOG%

echo.
echo Validation completed. Check error_log.txt for details.
pause
