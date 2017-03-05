@echo off
set PYTHONIOENCODING=UTF-8
set mayaver=Maya2015
set currentdir=%~dp0
set mayapy="%ProgramFiles%/Autodesk/%mayaver%/bin/mayapy.exe"
set mayascript="%currentdir%/relationship_check.py"
set mayafile=%1
%mayapy% %mayascript% %mayafile%
if %ERRORLEVEL% NEQ 0 pause