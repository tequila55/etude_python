@echo off
rem �����F���̃t�@�C����Shift JIS�ŕۑ����Ă���܂�

rem ����������i�d�v�Ȑݒ荀�ڂł��j
rem set FILTER="(from:227228567 OR to:227228567) (from:631124865 OR to:631124865)"
rem set FILTER="from:227228567 to:631124865"
rem set FILTER="from:227228567 "
set FILTER="gamayauber01 from:227228567"

rem �������Ԃƌ�������i�d�v�Ȑݒ荀�ڂł��j
set FROM_DATE=2008-01-01T00:00
set TO_DATE=2019-11-20T00:00
set MAX_RESULTS=1000

rem ���������́A��{�I�ɕύX�s�v�̂͂��ł�

for /f "usebackq" %%A in (`where search_tweets.py`) do set SEARCH_TWEETS=%%A
set KEY_FILE=my_keys.yaml
set PARAM=--max-results %MAX_RESULTS% --results-per-call 100 --start-datetime %FROM_DATE% --end-datetime %TO_DATE% --print-stream
set COMMAND=python %SEARCH_TWEETS%  --credential-file %KEY_FILE% %PARAM% --filter-rule %FILTER%

echo �ȉ������s���܂�����낵���ł����H�i���~����ꍇ��Window����Ă��������j
echo.
echo %COMMAND%
echo.
pause
echo %COMMAND% >> search_command.txt
%COMMAND% >> search_history.txt
pause
