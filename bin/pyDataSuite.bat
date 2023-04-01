@REM Prepare script
@echo off
setlocal

@REM Get parent directory and move up to it
set PARENT_DIR=%~dp0..
cd %PARENT_DIR%

@REM Execute python module with all args
python -m pyDataSuite %*