@CHCP 65001 >nul 
::UTF-8
REM ativa o UTF8, caracteres especiais
@echo off
:inicio
title Mostrar arquivos de uma pasta
mode 60, 20
color 02
cls

set caminho=''
for /d /r C:\Users\User\Desktop %%a in (*) do (%caminnho%=%caminnho%%%a)
echo teste
pause