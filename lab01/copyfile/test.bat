@echo off

set PROG=py copymanager.py
set INPUT_FILE="test.txt"
set OUTPUT_FILE="test_out.txt"

echo Test without command line arguments
%PROG% > %OUTPUT_FILE% 2>nul && goto test failed

echo Test copying with text in file
%PROG% %INPUT_FILE% %OUTPUT_FILE% 2>nul || goto test_failed
fc %OUTPUT_FILE% %INPUT_FILE% >nul || goto test_failed

echo All tests passed
exit /B 0

:test_failed
exit /B 1