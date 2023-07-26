@echo off

set PROG = py invert.py
set OUT = "invert_matrix_out.txt"

echo Test matrix inverted
%PROG% matrix.txt > %OUT% || goto test_failed
fc %OUT% test_data\inverted_matrix.txt >nul || goto test_failed
=======
set PROG=py invert.py
set INPUT_FILE="matrix.txt"
set OUTPUT_FILE="test_out.txt"

echo Test without command line arguments
%PROG% > %OUTPUT_FILE% 2>nul && goto test failed
