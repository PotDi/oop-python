@echo off

set PROG=py copymanager.py
set INPUT_FILE="test.txt"
set OUTPUT_FILE="test2.txt"
set OUT="%TEMP%\test_out.txt"

echo Test copying with text in file
%PROG% %INPUT_FILE% %OUTPUT_FILE% 2>nul || goto test_failed
fc %OUTPUT_FILE% "test_data\test_copy_text.txt" >nul || goto test_failed
#протестировать когда входной файл отсутствует
echo Test without command line arguments
%PROG% > %OUT% 2>nul && goto test failed


echo All tests passed
exit /B 0

:test_failed
echo Test Failed
exit /B 1