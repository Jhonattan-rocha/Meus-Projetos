@CHCP 65001 >nul
::UTF-8
@echo off
title Teste
mode 50, 20
color 02
:inicio
Shutdown –r –t 10 –c "O computador explodirá em 10 segundos"
pause >nul