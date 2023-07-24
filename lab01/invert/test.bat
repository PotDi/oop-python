@echo off

set PROG=py invert.py
set INPUT_FILE="matrix.txt"
set OUTPUT_FILE="test_out.txt"

echo Test without command line arguments
%PROG% > %OUTPUT_FILE% 2>nul && goto test failed

echo Test Inverted matrix
%PROG%