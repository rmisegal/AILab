@echo off
REM Quick AI2025 Terminal Tests
REM Run this in the AI2025 Terminal to verify functionality

echo.
echo ========================================================================
echo  AI2025 Terminal Quick Tests
echo ========================================================================
echo.

echo [Test 1] Checking Conda Environment...
echo -------------------------------
echo Current Environment: %CONDA_DEFAULT_ENV%
if "%CONDA_DEFAULT_ENV%"=="AI2025" (
    echo [PASS] AI2025 environment is active
) else (
    echo [FAIL] Wrong environment: %CONDA_DEFAULT_ENV%
)
echo.

echo [Test 2] Checking Custom Prompt...
echo -------------------------------
echo Current Prompt: %PROMPT%
echo %PROMPT% | findstr /C:"AI2025-Terminal" >nul
if %errorlevel% equ 0 (
    echo [PASS] Custom prompt is set
) else (
    echo [FAIL] Custom prompt not found
)
echo.

echo [Test 3] Checking Python Version...
echo -------------------------------
python --version
if %errorlevel% equ 0 (
    echo [PASS] Python is available
) else (
    echo [FAIL] Python not found
)
echo.

echo [Test 4] Checking Working Directory...
echo -------------------------------
echo Current Directory: %CD%
echo Expected: %AI_ENV_PATH%
if "%CD%"=="%AI_ENV_PATH%" (
    echo [PASS] Correct working directory
) else (
    echo [INFO] Different directory, but may be valid
)
echo.

echo [Test 5] Checking Pip Command...
echo -------------------------------
pip --version
if %errorlevel% equ 0 (
    echo [PASS] Pip is available
) else (
    echo [FAIL] Pip not found
)
echo.

echo [Test 6] Checking Conda Command...
echo -------------------------------
conda --version
if %errorlevel% equ 0 (
    echo [PASS] Conda is available
) else (
    echo [FAIL] Conda not found
)
echo.

echo [Test 7] Checking TensorBoard Installation...
echo -------------------------------
python -c "import tensorboard; print(f'TensorBoard {tensorboard.__version__}')" 2>nul
if %errorlevel% equ 0 (
    echo [PASS] TensorBoard is installed
) else (
    echo [FAIL] TensorBoard not found
)
echo.

echo [Test 8] Checking MLflow Installation...
echo -------------------------------
python -c "import mlflow; print(f'MLflow {mlflow.__version__}')" 2>nul
if %errorlevel% equ 0 (
    echo [PASS] MLflow is installed
) else (
    echo [FAIL] MLflow not found
)
echo.

echo [Test 9] Checking Return Command...
echo -------------------------------
if exist "%TEMP%\return_to_menu.bat" (
    echo [PASS] return_to_menu.bat exists at %TEMP%
) else (
    echo [FAIL] return_to_menu.bat not found
)
echo.

echo [Test 10] Checking Environment Variables...
echo -------------------------------
if defined AI_ENV_PATH (
    echo [PASS] AI_ENV_PATH is set: %AI_ENV_PATH%
) else (
    echo [FAIL] AI_ENV_PATH not set
)

if defined CONDA_PATH (
    echo [PASS] CONDA_PATH is set: %CONDA_PATH%
) else (
    echo [FAIL] CONDA_PATH not set
)
echo.

echo ========================================================================
echo  Tests Complete!
echo ========================================================================
echo.
echo To run Python-based comprehensive tests, execute:
echo    python test_ai2025_terminal.py
echo.

pause
