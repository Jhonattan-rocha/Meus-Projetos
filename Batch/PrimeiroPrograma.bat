@CHCP 65001 >nul 
::UTF-8
REM ativa o UTF8, caracteres especiais
@echo off
:inicio
title Rotina
mode 60, 20
color 02
cls
echo.
echo ╔═══════════════╦══════════════╦══════════════╗
echo ║     Backup    ║Menu de Rotina║              ║
echo ╠═══════════════╩══════════════╩══════════════╣
echo ║ ╔═════════════════════════════════════════╗ ║
echo ║ ║[1] Word              [10] NotePad       ║ ║
echo ║ ║[2] Excel             [11] Baixar vídeos ║ ║
echo ║ ║[3] PowerPoint        [12] Teams         ║ ║
echo ║ ║[4] Sites de costume  [13] Aulas gravadas║ ║
echo ║ ║[5] Calculadora       [14] Steam         ║ ║
echo ║ ║[6] Genshin Impact    [15] Eclipse       ║ ║
echo ║ ║[7] Encerrar programa [16] Pycharm       ║ ║
echo ║ ║[8] Pasta da fatec    [17] CMD           ║ ║
echo ║ ║[9] Bloco de notas    [18] Encerrar algo ║ ║
echo ║ ╚═════════════════════════════════════════╝ ║
echo ╚═════════════════════════════════════════════╝
echo.
set /p "op=-Digite o que deseja fazer agora-->"
if %op% == Backup (goto:salva)
if %op% lss 0 (goto:ERRO)
if %op% gtr 18 (goto:ERRO)
if %op% == 1 (goto:Word)
if %op% == 2 (goto:Excel)
if %op% == 3 (goto:PowerPoint)
if %op% == 4 (goto:Sites)
if %op% == 5 (goto:Calculadora)
if %op% == 6 (goto:genshin)
if %op% == 7 (exit)
if %op% == 8 (goto:Pasta)
if %op% == 9 (goto:Bloco) 
if %op% == 10 (goto:NotePad)
if %op% == 11 (goto:atuber)
if %op% == 12 (goto:Teams)
if %op% == 13 (goto:Aulas)
if %op% == 14 (goto:steam)
if %op% == 15 (goto:eclipse)
if %op% == 16 (goto:py)
if %op% == 17 (goto:cmd)
if %op% == 18 (goto:encerrar)
:salva
call Backup.bat
goto:inicio
:ERRO
	title ERROR
	mode 20, 5
	cls
	echo ++++++++++++++++++
	echo +-Erro-no numero-+
	echo +----Digitado----+
	echo ++++++++++++++++++
	pause > nul 
	goto:inicio

:encerrar
set /p "nome=-->Digite o nome do programa que deseja encerrar: "
TASKKILL /IM %nome%.exe | find "%nome%.exe"
goto:inicio

:Word
 start winword.exe
 goto:inicio
 
:Excel
 start excel.exe
 goto:inicio

:PowerPoint
 start powerpnt.exe
 goto:inicio
 
:Sites
 start https://www.youtube.com/watch?v=hdonNbzHHXE&list=RDMM&index=72
 start https://www.youtube.com/watch?v=kXYiU_JCYtU
 start https://www.youtube.com/watch?v=1mjlM_RnsVE
 start https://www.youtube.com/watch?v=ucanNEj49YY
 start https://www.youtube.com/watch?v=xk5y5JAwtI4
 start https://disqus.com/home/inbox/
 start https://mangalivre.net
 goto:inicio
 
:Calculadora
start calc.exe
goto:inicio

:genshin
cd \Program Files\Genshin Impact\Genshin Impact game
start GenshinImpact
goto:inicio

:Bloco
start notepad.exe
goto:inicio

:Pasta
set /p escolha=Digite qual semestre voce deseja acessar(ou 0 para a pasta da fatec):
if %escolha% == 0 (goto:fatec)
if %escolha% gtr 0 (goto:semestre)
else(
	cls
	echo ============
	echo ====ERRO====
	echo ============
	pause > nul
	goto:inicio)
:fatec
start C:\Users\User\Documents\Fatec
goto:inicio
:semestre
start C:\Users\User\Documents\Fatec\%escolha%°semestre
goto:inicio

:NotePad
cd C:\Program Files (x86)\Notepad++
start notepad++
goto:inicio

:atuber
cd C:\Program Files (x86)\DsNET Corp\aTube Catcher 2.0
start yct
goto:inicio

:Teams
start https://teams.microsoft.com/_?culture=pt-br&country=BR&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school/conversations/03%20-%20Junho_Julho?threadId=19:e539d0189bf24ef1bba44696600a22cf@thread.tacv2&ctx=channel
goto:inicio

:Aulas
start https://web.microsoftstream.com/studio/groups
goto:inicio

:steam
cd C:\Program Files (x86)\Steam
start steam
goto:inicio

:eclipse
cd C:\Users\User\eclipse\java-2020-12\eclipse
start eclipse
goto:inicio

:py
cd C:\Program Files\JetBrains\PyCharm Community Edition 2021.1\bin
start pycharm64
goto:inicio

:cmd
cd C:\
start cmd.exe
goto:inicio
