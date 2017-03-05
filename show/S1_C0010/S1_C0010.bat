@echo off
SET MAYARENDER="C:\Program Files\Autodesk\Maya2015\bin\Render.exe"
SET CURRENTDIR=%~dp0
SET SCENE=%~n0
SET LOG="%CURRENTDIR%%SCENE%_%USERNAME%_renderLog.txt"
SET IM="<Camera>\<RenderLayer>\<Camera>_<Scene>_<RenderLayer>"
SET TARGETDIR="%CURRENTDIR%render_images"
SET RENDERFILE="%CURRENTDIR%lighting\%SCENE%.ma"
rem ---------------------------------------------
echo #Render Application
echo %MAYARENDER%
echo #Current work directory
echo %CURRENTDIR%
echo #Current work file
echo %SCENE%
echo #Current work scene
echo %RENDERFILE%
echo #Log file path
echo %LOG%
echo #Render image format
echo %IM%
echo #Render image directory
echo %TARGETDIR%
rem ---------------------------------------------
cd ..
cd ..
cd scripts
call relationship_check.bat %RENDERFILE%
if %ERRORLEVEL% NEQ 0 exit
call rendersetting_check.bat %RENDERFILE%
if %ERRORLEVEL% NEQ 0 exit
echo ===============================
echo ===============================
echo Go Maya Batch Render - %SCENE%
echo @
echo Do not quit this command window
echo ===============================
echo ===============================
%MAYARENDER% -rd %TARGETDIR% -im %IM% -log %LOG% %RENDERFILE%
echo ===============================
echo ===============================
echo Render Process has been done !
echo ===============================
echo ===============================