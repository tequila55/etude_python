@echo off
rem �����F���̃t�@�C����Shift JIS�ŕۑ����Ă���܂�

rem ����������i�d�v�Ȑݒ荀�ڂł��Brem�Ŏn�܂�s�͎g���܂���B�Q�l�p�ł��B�j
rem set FILTER="(from:227228567 OR to:227228567) (from:631124865 OR to:631124865)"
rem set FILTER="from:227228567 to:631124865"
rem set FILTER="from:227228567"
set FILTER="gamayauber01 from:227228567"

rem �������Ԃƌ������ʂ̏���i�d�v�Ȑݒ荀�ڂł��j
set FROM_DATE=2008-01-01T00:00
set TO_DATE=2019-11-20T00:00
set MAX_RESULTS=5

rem ���������́A��{�I�ɕύX�s�v�̂͂��ł�

rem search_tweets.py�̌����A�o�b�h�m�E�n�E
for /f "usebackq" %%A in (`where search_tweets.py`) do set SEARCH_TWEETS=%%A
set KEY_FILE=my_keys.yaml
set PARAM=--max-results %MAX_RESULTS% --results-per-call 100 --start-datetime %FROM_DATE% --end-datetime %TO_DATE% --print-stream
set COMMAND=python %SEARCH_TWEETS% --credential-file %KEY_FILE% %PARAM% --filter-rule %FILTER%

set D=%date: =0%
set T=%time: =0%
set DT=%D:~0,4%%D:~5,2%%D:~8,2%_%T:~0,2%%T:~3,2%
set RESULT=result_%DT%.json

echo �ȉ������s���܂�����낵���ł����H
echo.
echo %COMMAND%
echo.
echo ���ʂ� %RESULT% �ɏo�͂���܂��B
echo.
echo ���~����ꍇ�͂��� Window ����Ă��������B�L�[�������Ǝ��s���܂��B
pause >nul
echo %RESULT% >> history.txt
echo %COMMAND% >> history.txt
echo. >> history.txt
%COMMAND% >> %RESULT%
echo.
echo �������������܂����B�L�[�������Ƃ��� Window ����܂��B
pause >nul
