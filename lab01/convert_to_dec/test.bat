@echo off

set PROG=py converter_bin_to_dec.py
set OUT="%TEMP%\bin_to_dec_out.txt"

echo Test 0
%PROG% 0 > %OUT% || goto test_failed
fc %OUT% test_data\0.txt >nul || goto test_failed

echo Test 1101
%PROG% 1101 > %OUT% 2>nul || goto test_failed
fc %OUT% test_data\1101.txt >nul || goto test_failed

echo Test non binary digits
%PROG% 102 > %OUT% 2>nul && goto test_failed

echo Test without command line arguments
%PROG% > %OUT% 2>nul && goto test_failed

echo All tests passed
exit /B 0

:test_failed
echo Test failed
exit /B 1
