@echo off
set TOOLS_FOLDER=%~dp0
set TOOLS_FOLDER=%TOOLS_FOLDER:~0,-1%
for %%i in ("%TOOLS_FOLDER%\..") do set WORKSPACE_FOLDER=%%~fi
set TRANSLATION_FOLDER=%WORKSPACE_FOLDER%\src\assets\translations\
echo %TOOLS_FOLDER%
python %TOOLS_FOLDER%\bible_dumper.py %TRANSLATION_FOLDER%
