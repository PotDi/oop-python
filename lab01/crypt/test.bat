@echo off

set PROG=py main.py
set INPUT_FILE="input.bin"
set OUTPUT_FILE="encrypt.bin"
set OUT="decrypt bin"
set KEY="32"

echo Test encrypt file
%PROG% %INPUT_FILE% %OUTPUT_FILE% %OUT% %KEY% || goto test_failed
fc %OUTPUT_FILE% "test_data\test_source_file.bin" <nul && goto test_failed

echo Test decrypt file
fc %OUT% "test_data\test_source_file.bin" <nul || goto test_failed

echo Test without command line arguments
%PROG% > %OUTPUT_FILE% 2>nul && goto test failed

echo All tests passed
exit /B 0

:test_failed
echo Test Failed
exit /B 1