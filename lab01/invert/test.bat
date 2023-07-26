@echo off

set PROG = py invert.py
set OUT = "invert_matrix_out.txt"

echo Test matrix inverted
%PROG% matrix.txt > %OUT% || goto test_failed
fc %OUT% test_data\inverted_matrix.txt >nul || goto test_failed