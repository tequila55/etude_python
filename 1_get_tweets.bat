@echo off
rem メモ：このファイルはShift JISで保存してあります

rem 検索文字列（重要な設定項目です。remで始まる行は使われません。参考用です。）
rem set FILTER="(from:227228567 OR to:227228567) (from:631124865 OR to:631124865)"
rem set FILTER="from:227228567 to:631124865"
rem set FILTER="from:227228567"
set FILTER="gamayauber01 from:227228567"

rem 検索期間と検索結果の上限（重要な設定項目です）
set FROM_DATE=2008-01-01T00:00
set TO_DATE=2019-11-20T00:00
set MAX_RESULTS=5

rem ここから先は、基本的に変更不要のはずです

rem search_tweets.pyの検索、バッドノウハウ
for /f "usebackq" %%A in (`where search_tweets.py`) do set SEARCH_TWEETS=%%A
set KEY_FILE=my_keys.yaml
set PARAM=--max-results %MAX_RESULTS% --results-per-call 100 --start-datetime %FROM_DATE% --end-datetime %TO_DATE% --print-stream
set COMMAND=python %SEARCH_TWEETS% --credential-file %KEY_FILE% %PARAM% --filter-rule %FILTER%

set D=%date: =0%
set T=%time: =0%
set DT=%D:~0,4%%D:~5,2%%D:~8,2%_%T:~0,2%%T:~3,2%
set RESULT=result_%DT%.json

echo 以下を実行しますがよろしいですか？
echo.
echo %COMMAND%
echo.
echo 結果は %RESULT% に出力されます。
echo.
echo 中止する場合はこの Window を閉じてください。キーを押すと実行します。
pause >nul
echo %RESULT% >> history.txt
echo %COMMAND% >> history.txt
echo. >> history.txt
%COMMAND% >> %RESULT%
echo.
echo 処理が完了しました。キーを押すとこの Window を閉じます。
pause >nul
