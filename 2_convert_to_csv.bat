@echo off
rem �����F���̃t�@�C����Shift JIS�ŕۑ����Ă���܂�

set IN_FILE=%1
set OUT_FILE=%~n1.csv

rem ���������́A��{�I�ɕύX�s�v�̂͂��ł�
set COMMAND=python jsons_to_koa_csv.py %IN_FILE% %OUT_FILE%

echo �ȉ������s���܂�����낵���ł����H
echo.
echo %COMMAND%
echo.
echo ���ʂ� %OUT_FILE% �ɏo�͂���܂��B
echo.
echo ���~����ꍇ�͂��� Window ����Ă��������B�L�[�������Ǝ��s���܂��B
pause >nul
echo %OUT_FILE% >> history.txt
echo %COMMAND% >> history.txt
echo. >> history.txt
%COMMAND%
echo.
echo �������������܂����B�L�[�������Ƃ��� Window ����܂��B
pause >nul
