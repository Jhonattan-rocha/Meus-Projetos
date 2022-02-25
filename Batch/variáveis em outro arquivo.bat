@CHCP 65001 >nul 
::UTF-8
REM ativa o UTF8, caracteres especiais
@echo off
:inicio
if exist config.bat (call config.bat) else  (goto:cria)
color %cor_fundo%%cor_letra%
title %titulo%

echo este é o resultado final
pause > nul
:cria
set /p "cor_letra=Digite uma cor de 0-9 ou de A a F: "
echo.
set /p "cor_fundo=Digite a cor de fundo de 0-9 ou de A-F: "
echo.
set /p "titulo=Digite o titulo: "
echo.

msg * Abra novamente o script

(
echo set cor_letra=%cor_letra%
echo set cor_fundo=%cor_fundo%
echo set titulo=%titulo%
)>config.bat
