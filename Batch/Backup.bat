@CHCP 65001 >nul 
::UTF-8
@echo off
title Backup
mode 60, 20
color 02
:inicio
cd C:\Users\User\Documents
if exist C:\Users\User\Documents\Fatec (xcopy /E /I Fatec "C:\Users\User\Documents\Backup") else (echo Ocorreu um erro ao salvar a pasta)
:fim
pause > nul
