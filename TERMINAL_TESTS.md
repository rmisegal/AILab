# AI2025 Terminal Tests

Quick manual tests to verify AI2025 Terminal functionality.

## Automated Test Suite

Run the comprehensive test suite:
```bash
python test_ai2025_terminal.py
```

## Manual Quick Tests

Copy and paste these commands one at a time in the AI2025 Terminal:

### 1. Check Python Environment
```bash
python --version
```
**Expected:** Python 3.10.x or higher

### 2. Check Conda Environment
```bash
conda info --envs
```
**Expected:** Should show AI2025 as active (marked with *)

### 3. Test Python Import
```bash
python -c "import sys; print(f'Python: {sys.version}'); print(f'Executable: {sys.executable}')"
```
**Expected:** Should show Python in AI2025 environment path

### 4. Test TensorBoard
```bash
python -c "import tensorboard; print(f'TensorBoard version: {tensorboard.__version__}')"
```
**Expected:** Should print TensorBoard version without errors

### 5. Test MLflow
```bash
python -c "import mlflow; print(f'MLflow version: {mlflow.__version__}')"
```
**Expected:** Should print MLflow version without errors

### 6. Test Critical AI Packages
```bash
python -c "import langchain, streamlit, fastapi, pandas, numpy, torch; print('All packages imported successfully!')"
```
**Expected:** "All packages imported successfully!"

### 7. Check Prompt
Look at your command prompt. It should show:
```
[AI2025-Terminal] F:\AI_Lab>
```

### 8. Check Working Directory
```bash
cd
```
**Expected:** Should show F:\AI_Lab or F:\AI_Lab\AI_Environment

### 9. Test Pip
```bash
pip --version
```
**Expected:** Should show pip version in AI2025 environment

### 10. Test Package List
```bash
pip list | findstr /i "tensorboard mlflow"
```
**Expected:** Should show both tensorboard and mlflow in the list

### 11. Test Environment Variables
```bash
echo %CONDA_DEFAULT_ENV%
```
**Expected:** AI2025

```bash
echo %AI_ENV_PATH%
```
**Expected:** Path to AI Environment (e.g., F:\AI_Lab)

### 12. Test Return Command Exists
```bash
where return_to_menu.bat
```
**Expected:** Should show path to return_to_menu.bat in TEMP directory

### 13. Verify Return Command Content (Optional)
```bash
type %TEMP%\return_to_menu.bat
```
**Expected:** Should show batch script that returns to main menu

## Advanced Tests

### Test TensorBoard Launch (Port Check)
```bash
python -c "import socket; s = socket.socket(); result = s.connect_ex(('localhost', 6006)); s.close(); print('TensorBoard port available' if result != 0 else 'TensorBoard already running')"
```

### Test MLflow Launch (Port Check)
```bash
python -c "import socket; s = socket.socket(); result = s.connect_ex(('localhost', 5000)); s.close(); print('MLflow port available' if result != 0 else 'MLflow already running')"
```

### List All Installed Packages
```bash
pip list
```

### Check Conda Packages
```bash
conda list
```

## Expected Results Summary

| Test | Expected Result |
|------|----------------|
| Python Version | 3.10.x or higher |
| Conda Environment | AI2025 (active) |
| Custom Prompt | `[AI2025-Terminal]` |
| TensorBoard | Installed and importable |
| MLflow | Installed and importable |
| Working Directory | F:\AI_Lab |
| Return Command | exists in TEMP |
| Environment Variables | AI_ENV_PATH and CONDA_DEFAULT_ENV set |

## Testing the Return Command

⚠️ **WARNING:** This will exit the terminal and return to the main menu!

```bash
return_to_menu
```

**Expected:** Terminal closes and main AI Environment menu appears

## Troubleshooting

If any test fails:

1. **Python not found**: Conda environment not activated properly
2. **Package not found**: Run `pip install <package-name>`
3. **Wrong environment**: Verify with `conda info --envs`
4. **Custom prompt missing**: PROMPT variable not set correctly
5. **Return command not found**: Check TEMP environment variable

## Success Criteria

✅ All 13 manual tests pass
✅ Automated test suite passes with 100% success rate
✅ No errors when importing tensorboard and mlflow
✅ Custom prompt displays correctly
✅ return_to_menu command exists and works
