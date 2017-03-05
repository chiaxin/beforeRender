@echo off
set PYTHONIOENCODING=UTF-8
set CURRENT_DIR=%~dp0
set CHECK_SCRIPT=%CURRENT_DIR%/relationship_check.py
set MAYAFILE=%1
call %CURRENT_DIR%/env.bat
set MAYA_INSTALL=%MAYA_INSTALL:"=%
rem "
set MAYAPY_APP=%MAYA_INSTALL%/bin/mayapy.exe

if NOT EXIST "%MAYAPY_APP%" (
	echo %MAYAPY_APP% is not found.
	pause
	exit
)
if NOT EXIST "%CHECK_SCRIPT%" (
	echo %CHECK_SCRIPT% is not found.
	pause
	exit
)
if NOT EXIST "%MAYAFILE%" (
	echo %MAYAFILE% is not found.
	pause
	exit
)
"%MAYAPY_APP%" "%CHECK_SCRIPT%" "%MAYAFILE%"
if %ERRORLEVEL% NEQ 0 pause