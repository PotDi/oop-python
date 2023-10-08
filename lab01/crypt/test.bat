@echo off

set PROG=py main.py
set INPUT_FILE="input.bin"
set OUTPUT_FILE="encrypt.bin"
set OUT="decrypt bin"

echo Test encrypt file
%PROG% %INPUT_FILE% %OUTPUT_FILE% %OUT% 2>nul || goto test_failed
fc %OUTPUT_FILE% "test_data\test_source_file.bin" <nul || goto test_failed

echo All tests passed
exit /B 0

:test_failed
echo Test Failed
exit /B 1