:: AI Environment Version Checker v3.0.28
@echo off
setlocal EnableDelayedExpansion

:: AI Environment Version Checker v3.0.26
:: Windows wrapper for Python version checker

set "SCRIPT_VERSION=3.0.28"
set "SCRIPT_DATE=2025-08-14"

title AI Environment Version Checker v%SCRIPT_VERSION%

echo ================================================================
echo                   AI Environment Version Checker
echo                     Version %SCRIPT_VERSION% (%SCRIPT_DATE%)
echo                     Windows Wrapper for Python Checker
echo ================================================================
echo.

:: Determine current directory (AI Environment directory)
set "AI_ENV_PATH=%~dp0"
:: Remove trailing backslash
if "%AI_ENV_PATH:~-1%"=="\" set "AI_ENV_PATH=%AI_ENV_PATH:~0,-1%"

:: Navigate to AI Environment directory
cd /d "%AI_ENV_PATH%"

echo [INFO] Checking file versions in: %CD%
echo [INFO] Using Python version checker: check_versions.py
echo.

:: Check if Python version checker exists
if not exist "check_versions.py" (
    echo [ERROR] check_versions.py not found
    echo [ERROR] Please ensure all Python files are in %AI_ENV_PATH%\src
    echo [INFO] Expected location: %AI_ENV_PATH%\check_versions.py
    echo.
    echo [INFO] Available files in src directory:
    if exist "src\" (
        dir /b src\*.py
    ) else (
        echo [ERROR] src directory not found
    )
    echo.
    pause
    exit /b 1
)

:: Check if we have Python available
python --version >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Python not found in PATH
    echo [INFO] Trying to use conda environment...
    
    :: Try to find conda python
    if exist "Miniconda\envs\AI2025\python.exe" (
        echo [INFO] Using conda Python: Miniconda\envs\AI2025\python.exe
        "Miniconda\envs\AI2025\python.exe" check_versions.py
    ) else (
        echo [ERROR] Neither system Python nor conda Python found
        echo [INFO] Please ensure Python is installed or use run_ai_env.bat
        echo.
        pause
        exit /b 1
    )
) else (
    echo [INFO] Using system Python
    python check_versions.py
)

echo.
echo [INFO] Version check completed
echo [INFO] For detailed configuration: type "python check_versions.py"
echo.



