@echo off
SET CURRENTDIR=%~dp0
SET SCENE=%~n0
SET LOG="%CURRENTDIR%%SCENE%_%USERNAME%_renderLog.txt"
SET IM="<Camera>\<RenderLayer>\<Camera>_<Scene>_<RenderLayer>"
SET TARGETDIR="%CURRENTDIR%render_images"
SET RENDERFILE="%CURRENTDIR%lighting\%SCENE%.ma"
rem ---------------------------------------------
echo #-----------------------
echo # All Source Below :
echo # Current work directory
echo %CURRENTDIR%
echo # Current work
echo %SCENE%
echo # Current work scene
echo %RENDERFILE%
echo # LOG
echo %LOG%
echo # Render Image
echo %IM%
echo # Render Image Directory
echo %TARGETDIR%
rem ---------------------------------------------
cd ..
cd ..
cd scripts
rem ---------------------------------------------
call relationship_check.bat %RENDERFILE%
if %ERRORLEVEL% NEQ 0 exit
call rendersetting_check.bat %RENDERFILE%
if %ERRORLEVEL% NEQ 0 exit
call version_check.bat %RENDERFILE%
if %ERRORLEVEL% NEQ 0 exit
call env.bat
set MAYA_RENDER_APP="%MAYA_INSTALL%\bin\Render.exe"
if NOT EXIST %MAYA_RENDER_APP% (
	echo %MAYA_RENDER_APP% is not found.
	pause
	exit
)
echo ===============================
echo ===============================
echo Go Maya Batch Render - %SCENE%
echo @
echo Do not quit this command window
echo ===============================
echo ===============================
%MAYA_RENDER_APP% -rd %TARGETDIR% -im %IM% -log %LOG% %RENDERFILE%
echo ===============================
echo ===============================
echo Render Process has been done !
echo Please check out log file : %LOG%
echo ===============================
echo ===============================