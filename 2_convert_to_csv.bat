@echo off
rem メモ：このファイルはShift JISで保存してあります

set IN_FILE=%1
set OUT_FILE=%~n1.csv

rem ここから先は、基本的に変更不要のはずです
set COMMAND=python jsons_to_koa_csv.py %IN_FILE% %OUT_FILE%

echo 以下を実行しますがよろしいですか？
echo.
echo %COMMAND%
echo.
echo 結果は %OUT_FILE% に出力されます。
echo.
echo 中止する場合はこの Window を閉じてください。キーを押すと実行します。
pause >nul
echo %OUT_FILE% >> history.txt
echo %COMMAND% >> history.txt
echo. >> history.txt
%COMMAND%
echo.
echo 処理が完了しました。キーを押すとこの Window を閉じます。
pause >nul
