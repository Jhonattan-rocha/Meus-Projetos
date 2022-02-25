@echo off
title Programa Bat
mode 80,40
color 0f
:inicio
cls
echo.
REM comentar
echo ++++++++++++++++++++++++++++
echo  M E N U  P R I N C I P A L
echo ++++++++++++++++++++++++++++
echo [1] Executar o Word
echo [2] Executar o Excel
echo [3] Executar o PowerPoint
echo [4] Executar o Access
echo [5] Acessar a Web
echo [6] Calculadora
echo [7] Testar conexao de rede
echo [8] Checar disco
echo [9] Encerrar programa
echo ++++++++++++++++++++++++++++
set /p op=Digite uma opcao desejada:
if %op% == 1 (goto:Word)
if %op% == 2 (goto:Excel)
if %op% == 3 (goto:PowerPoint)
if %op% == 4 (goto:Access)
if %op% == 5 (goto:Web)
if %op% == 6 (goto:Calculadora)
if %op% == 7 (goto:Conexao)
if %op% == 8 (goto:Disco)
if %op% == 9 (exit) else (
	echo.
	echo +++++++++++++++++
	echo  Opcao Invalida!
	echo +++++++++++++++++
	pause > nul
	goto:inicio)

:Word
 start winword.exe
 goto:inicio
 
:Excel
 start excel.exe
 goto:inicio

:PowerPoint
 start powerpnt.exe
 goto:inicio

:Access
 start msaccess.exe
 goto:inicio
 
:Web
 set /p site=Digite o endereco da pagina:
 start %site%
 goto:inicio
 
:Calculadora
 start calc.exe
 goto:inico
 
:Conexao
 set /p conexao=Digite o IP da maquina ou endereco:
 ping %conexao% -t
 goto:inicio
 
:Disco
 start chkdsk c: /f
 goto:inicio 