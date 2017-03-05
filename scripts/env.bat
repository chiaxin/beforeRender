@echo off
set MAYA_INSTALL="C:/Program Files/Autodesk/Maya2015"
if NOT EXIST %MAYA_INSTALL% (
	echo %MAYA_INSTALL% is not exists!
	pause
) ELSE (
	set MAYA_INSTALL=%MAYA_INSTALL:"=%
rem "
)