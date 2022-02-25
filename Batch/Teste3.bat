@CHCP 65001 >nul
::UTF-8
@echo off
title Backup
mode 60, 20
color 02
:Principal
set /p nomearquivo=Digite o nome do arquivo:
call :procura %nomearquivo%

:procura
for /l %%a in (1,1,10) do (echo %~f1)
pause > nul