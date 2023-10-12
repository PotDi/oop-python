@echo off

set PROG=py main_replace.py
set SOURCE_FILE="file.txt"
set SRC_TEXT="счет"
set CHANGE_TEXT="вес"

echo Test change text
%PROG% %SOURCE_FILE% %SRC_TEXT% %CHANGE_TEXT% || goto test_failed
FINDSTR "вес" %SOURCE_FILE% <nul && goto test_failed

echo Test without command line arguments
%PROG% 2>nul && goto test failed


echo All tests passed
exit /B 0

:test_failed
echo Test Failed
exit /B 1