@echo off

set PROG=py invert.py
set INPUT_FILE="matrix.txt"
set OUTPUT_FILE="test_out.txt"

echo Test matrix inverted
%PROG% %INPUT_FILE% > %OUTPUT_FILE% || goto test_failed
fc %OUTPUT_FILE% test_data\inverted_matrix.txt >nul || goto test_failed

echo Test without command line arguments
%PROG% > %OUTPUT_FILE% 2>nul && goto test failed

echo All tests passed
exit /B 0

:test_failed
echo Test failed
exit /B 1