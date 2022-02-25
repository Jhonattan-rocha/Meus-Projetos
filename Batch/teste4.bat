@CHCP 65001 >nul 
::UTF-8
@echo off
title Teste4 - gravando variaveis em arquivos separados
mode 60, 20
color 02
:ficha
call Teste5.bat

echo %nome% %idade% %sexo% %aniversario%
pause > nul