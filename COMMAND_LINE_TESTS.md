# AI2025 Terminal Command-Line Tests

Copy and paste these commands directly into your AI2025 Terminal to test functionality.

---

## 🚀 Quick Batch Test Script

Run all tests at once:
```bash
quick_terminal_tests.bat
```

---

## 📝 Individual Command Tests

### Test 1: Environment Check
```bash
echo Current Environment: %CONDA_DEFAULT_ENV%
```
**Expected Output:** `Current Environment: AI2025`

---

### Test 2: Prompt Check
```bash
echo %PROMPT%
```
**Expected Output:** Should contain `[AI2025-Terminal]`

---

### Test 3: Python Version
```bash
python --version
```
**Expected Output:** `Python 3.10.x` or higher

---

### Test 4: Python Executable Location
```bash
python -c "import sys; print(sys.executable)"
```
**Expected Output:** Path should contain `AI2025` environment

---

### Test 5: Working Directory
```bash
cd
```
**Expected Output:** Should show `F:\AI_Lab` or AI_Environment path

---

### Test 6: Environment Variables
```bash
echo AI_ENV_PATH: %AI_ENV_PATH%
echo CONDA_PATH: %CONDA_PATH%
echo CONDA_DEFAULT_ENV: %CONDA_DEFAULT_ENV%
```
**Expected Output:** All should be set with appropriate paths

---

### Test 7: Conda Info
```bash
conda info --envs
```
**Expected Output:** Should list AI2025 with an asterisk (*) indicating it's active

---

### Test 8: Pip Version
```bash
pip --version
```
**Expected Output:** Pip version with path in AI2025 environment

---

### Test 9: Test TensorBoard Import
```bash
python -c "import tensorboard; print('TensorBoard version:', tensorboard.__version__)"
```
**Expected Output:** TensorBoard version number

---

### Test 10: Test MLflow Import
```bash
python -c "import mlflow; print('MLflow version:', mlflow.__version__)"
```
**Expected Output:** MLflow version number

---

### Test 11: Test All Critical AI Packages
```bash
python -c "packages = ['langchain', 'streamlit', 'fastapi', 'pandas', 'numpy', 'torch', 'tensorboard', 'mlflow']; import importlib; results = [(p, 'OK' if importlib.util.find_spec(p) else 'MISSING') for p in packages]; [print(f'{p}: {r}') for p, r in results]"
```
**Expected Output:** All packages should show `OK`

---

### Test 12: Check Installed Packages
```bash
pip list | findstr /i "tensorboard mlflow langchain streamlit"
```
**Expected Output:** Should list all four packages with version numbers

---

### Test 13: TensorBoard Executable Check
```bash
where tensorboard
```
**Expected Output:** Path to tensorboard.exe in AI2025 environment

---

### Test 14: MLflow Executable Check
```bash
where mlflow
```
**Expected Output:** Path to mlflow.exe in AI2025 environment

---

### Test 15: Python Package Location
```bash
python -c "import site; print('\n'.join(site.getsitepackages()))"
```
**Expected Output:** Should show site-packages in AI2025 environment

---

### Test 16: Conda List (Selected Packages)
```bash
conda list | findstr /i "python numpy pandas"
```
**Expected Output:** Should show installed versions in AI2025

---

### Test 17: Return Command Exists
```bash
where return_to_menu.bat
```
**Expected Output:** Path to return_to_menu.bat in TEMP directory

---

### Test 18: Return Command Content (Preview)
```bash
type %TEMP%\return_to_menu.bat
```
**Expected Output:** Batch script that returns to main menu

---

### Test 19: PATH Variable Check
```bash
echo %PATH%
```
**Expected Output:** Should include conda Scripts directory and TEMP directory

---

### Test 20: Test PyTorch
```bash
python -c "import torch; print('PyTorch version:', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```
**Expected Output:** PyTorch version and CUDA availability status

---

## 🔬 Advanced Tests

### Test Interactive Python Session
```bash
python
```
Then in Python:
```python
import tensorboard
import mlflow
import langchain
import streamlit
import pandas as pd
import numpy as np

print(f"TensorBoard: {tensorboard.__version__}")
print(f"MLflow: {mlflow.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")

exit()
```

---

### Test TensorBoard Launch (Dry Run)
```bash
python -c "import subprocess; result = subprocess.run(['tensorboard', '--version'], capture_output=True, text=True); print(result.stdout if result.returncode == 0 else result.stderr)"
```
**Expected Output:** TensorBoard version

---

### Test MLflow Launch (Dry Run)
```bash
python -c "import subprocess; result = subprocess.run(['mlflow', '--version'], capture_output=True, text=True); print(result.stdout if result.returncode == 0 else result.stderr)"
```
**Expected Output:** MLflow version

---

### Test Port Availability (TensorBoard)
```bash
python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); result = s.connect_ex(('localhost', 6006)); s.close(); print('Port 6006 (TensorBoard):', 'IN USE' if result == 0 else 'AVAILABLE')"
```
**Expected Output:** Port status

---

### Test Port Availability (MLflow)
```bash
python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); result = s.connect_ex(('localhost', 5000)); s.close(); print('Port 5000 (MLflow):', 'IN USE' if result == 0 else 'AVAILABLE')"
```
**Expected Output:** Port status

---

### Test Port Availability (Streamlit)
```bash
python -c "import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); result = s.connect_ex(('localhost', 8501)); s.close(); print('Port 8501 (Streamlit):', 'IN USE' if result == 0 else 'AVAILABLE')"
```
**Expected Output:** Port status

---

### List All Python Packages
```bash
pip list
```
**Expected Output:** Complete list of installed packages

---

### Check Package Versions (Key Packages)
```bash
pip show tensorboard mlflow langchain streamlit fastapi
```
**Expected Output:** Detailed info for each package

---

### Test Jupyter Availability
```bash
jupyter --version
```
**Expected Output:** Jupyter versions for all components

---

### Test JupyterLab Availability
```bash
jupyter lab --version
```
**Expected Output:** JupyterLab version number

---

## 🎯 One-Line Comprehensive Test
```bash
python -c "import sys, os; packages = ['tensorboard', 'mlflow', 'langchain', 'streamlit', 'fastapi', 'pandas', 'numpy', 'torch']; print('='*60); print('AI2025 Terminal Status Report'); print('='*60); print(f'Python: {sys.version}'); print(f'Conda Env: {os.environ.get(\"CONDA_DEFAULT_ENV\", \"NOT SET\")}'); print(f'Working Dir: {os.getcwd()}'); print('Packages:'); [print(f'  - {p}: {\"OK\" if __import__(p) or True else \"FAIL\"}') for p in packages]; print('='*60)"
```
**Expected Output:** Complete status report with all package checks

---

## 🛑 Test Return Functionality

**⚠️ WARNING:** This will exit the terminal and return to main menu!

```bash
return_to_menu
```
**Expected Behavior:**
- Terminal displays return message
- Terminal closes
- AI Environment main menu appears

---

## 📊 Success Criteria

All tests should:
- ✅ Execute without errors
- ✅ Show AI2025 environment is active
- ✅ Confirm all packages are installed
- ✅ Display correct paths and versions
- ✅ Show custom prompt `[AI2025-Terminal]`

---

## 💡 Quick Test Sequence

Copy this entire block and paste it into the terminal:

```bash
echo.
echo === Quick Test Sequence ===
echo [1/8] Environment: %CONDA_DEFAULT_ENV%
python --version
pip --version
conda --version
python -c "import tensorboard, mlflow; print('[2/8] TensorBoard:', tensorboard.__version__); print('[3/8] MLflow:', mlflow.__version__)"
python -c "import langchain, streamlit, fastapi; print('[4/8] LangChain: OK'); print('[5/8] Streamlit: OK'); print('[6/8] FastAPI: OK')"
python -c "import pandas, numpy, torch; print('[7/8] Core packages: OK')"
echo [8/8] Working Directory: %CD%
echo === All Quick Tests Complete ===
echo.
```

---

## 📝 Notes

- Copy commands one at a time for best results
- Some commands may take a few seconds to complete
- If any test fails, refer to TERMINAL_TESTS.md for troubleshooting
- Run `python test_ai2025_terminal.py` for comprehensive automated testing
