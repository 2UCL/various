@echo off

net session >nul 2>&1

if %ERRORLEVEL% equ 0 (
	echo Already running as Administrator.
) else ( 
	if "%~1" equ "" (
		powershell start-process cmd -ArgumentList '/k ""cd /d %CD%""' -verb runas
	) else (
		powershell start-process %* -verb runas
	)
)