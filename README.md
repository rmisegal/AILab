# AI Environment Python System v3.0.28

**A portable, modular AI development environment for Windows with interactive Python-based management**

---

## 📋 **Overview**

The AI Environment Python System is a comprehensive, self-contained development environment designed for AI and machine learning work. It provides an interactive menu-driven interface for managing conda environments, AI models (via Ollama), Jupyter Lab, VS Code, and various development tools - all from a portable installation.

---

## ⚠️ **Prerequisites**

Before using this system, you **must** run the `install-0` setup script to install all required dependencies and configure the base environment.

### **Installation Requirements:**
1. Run `install-0.bat` (or equivalent installer)
2. Wait for successful completion
3. Verify installation before proceeding

**The system will NOT function properly without completing the initial installation.**

---

## 🎯 **Core Features**

### **1. Interactive Menu System**
The system provides a Python-based interactive menu (`activate_ai_env.py`) that serves as the central hub for all operations:

- **Full color-coded interface** - Easy-to-read menus with status indicators
- **Real-time status updates** - Shows running processes and environment state
- **Context-aware options** - Menu items adapt based on current system state
- **Keyboard navigation** - Simple number-based selection system

### **2. Environment Management**
Manages conda environments and Python installations:

- **Automatic conda detection** - Finds Miniconda in multiple locations (relative path, PATH variable, common install locations)
- **AI2025 environment activation** - Pre-configured Python environment with AI packages
- **PATH management** - Safe PATH manipulation with backup/restore capabilities
- **Environment validation** - Comprehensive checks for packages and dependencies

### **3. AI Model Management (Ollama)**
Complete integration with Ollama for local AI model hosting:

- **Model download** - Interactive selection from popular models or custom URLs
- **Model loading** - Automatic loading with Python usage examples
- **Model status checking** - View loaded and available models
- **Model deletion** - Storage space management
- **Help documentation** - Detailed guides for each model (phi, llama2, mistral, codellama, gpt-oss)

### **4. Application Launchers**
One-click launching of development tools:

- **Jupyter Lab** - Full sub-menu with server management (start, stop, status, custom ports)
- **VS Code** - Automatic workspace configuration with AI2025 environment
- **AI2025 Terminal** - Enhanced command prompt with pre-activated environment
- **Custom applications** - Extensible launcher system

### **5. Process Management**
Background process tracking and control:

- **Automatic tracking** - Monitors Ollama, Jupyter Lab, VS Code
- **Status display** - View all running processes with PIDs
- **Clean shutdown** - Stop all tracked processes on exit
- **Process persistence** - JSON-based storage for session recovery

### **6. Component Testing**
Comprehensive validation system with 9 different tests:

- **Directory structure** - Verifies AI Environment layout
- **Conda installation** - Checks conda executable and version
- **AI2025 environment** - Validates Python environment
- **Python packages** - Tests psutil, colorama, requests, numpy, pandas
- **Ollama server** - Optional AI server availability check
- **System integration** - PATH, environment variables, Windows commands
- **AI model system** - Model management functionality
- **Jupyter Lab system** - Server management functionality
- **Help documentation** - Model help files availability

---

## 🏗️ **Architecture**

### **Modular Design**
The system is split into focused, maintainable modules (all under 250 lines):

```
src/
├── activate_ai_env.py          # Main entry point and orchestration
├── ai_menu_system.py            # Interactive menu display and navigation
├── ai_action_handlers.py        # Menu action implementations
├── ai_component_tester.py       # Comprehensive testing system
├── ai_path_manager.py           # PATH and environment variable management
├── ai_conda_manager.py          # Conda environment operations
├── ai_component_setup.py        # Component initialization and setup
├── ai_ollama_manager.py         # Ollama server management
├── ai_process_manager.py        # Background process tracking
├── ai_jupyter_manager.py        # Jupyter Lab management
├── ai_model_manager.py          # AI model management hub
├── ai_model_downloader.py       # Model download operations
├── ai_model_loader.py           # Model loading and usage instructions
├── ai_document_viewer.py        # Markdown document viewer
├── ai_update_manager.py         # System update functionality
├── ai_vscode_config.py          # VS Code workspace configuration
└── ai_status_display.py         # Status information display
```

### **Configuration System**
Modular JSON-based configuration:

```
config/
├── metadata.json                # System information and features
├── expected_versions.json       # File version tracking
├── install_config.json          # Package requirements
└── version_history.json         # Complete changelog

version_config.json              # Main configuration with references
```

---

## 🔧 **How It Works**

### **Startup Sequence**

1. **run_ai_env.bat** (Launcher)
   - Detects current directory using `%~dp0` (supports any drive/folder)
   - Calls `setup_python_env.bat` to prepare environment
   - Launches `activate_ai_env.py` with configured Python

2. **setup_python_env.bat** (Environment Preparation)
   - Auto-detects Miniconda installation (relative path, PATH, or common locations)
   - Configures PATH with conda and Python executables
   - Activates AI2025 conda environment
   - Verifies Python packages (psutil, colorama)
   - Exports environment variables for main script

3. **activate_ai_env.py** (Main System)
   - Loads all modules from `src/` directory
   - Initializes process manager and status display
   - Displays main menu with available options
   - Handles user input and dispatches to action handlers
   - Manages background processes and cleanup

### **Menu Options Explained**

#### **Option 1: Full Activation**
- Activates conda environment
- Configures PATH variables
- Starts Ollama server
- Optionally loads AI model
- Returns to menu for further operations

#### **Option 2: Restore Original PATH**
- Removes all AI Environment paths from PATH
- Deactivates conda environment
- Restores system to pre-activation state
- Useful for testing or troubleshooting

#### **Option 3: Activate Conda Environment**
- Activates AI2025 conda environment only
- Does not start additional services
- Minimal activation for quick Python work

#### **Option 4: Test All Components**
- Runs comprehensive 9-test suite
- Displays detailed results for each test
- Shows success rate and failure details
- Validates entire system setup

#### **Option 5: Setup Flask**
- Checks Flask installation
- Installs Flask if missing
- Useful for web development projects

#### **Option 6: Setup Ollama Server**
- Checks Ollama installation
- Starts Ollama server in background
- Tracks process for management
- Prerequisite for AI model operations

#### **Option 7: Download AI Models**
- Interactive model management sub-menu
- Download from popular list or custom URL
- Load models with Python examples
- Check model status and delete unused models
- View detailed help for each model

#### **Option 8: Run Environment Validation**
- Compares installed packages with `install_config.json`
- Reports missing packages
- Offers installation options
- Ensures complete system setup

#### **Option 9: Launch Applications**
- Sub-menu for development tools
- Jupyter Lab with full server management
- VS Code with workspace configuration
- AI2025 Terminal with pre-activated environment
- Each app tracked as background process

#### **Option 10: Background Processes**
- Displays all tracked processes
- Shows PIDs, names, and status
- Allows selective or bulk process termination
- JSON persistence across sessions

#### **Option 11: Advanced Options**
- Version & documentation viewer
- Update system (scans `new_versions/` folder)
- System utilities and troubleshooting

#### **Option 12: Quit**
- Exits menu system
- Leaves background processes running
- Environment remains activated
- Can restart menu without re-activation

#### **Option 13: Exit and Close All**
- Stops all tracked background processes
- Optionally deactivates conda environment
- Clean system shutdown
- Recommended for complete session end

---

## 📤 **Outputs**

### **Console Output**
- **Color-coded status messages**: Green (success), yellow (warning), red (error), cyan (info)
- **Progress indicators**: Step-by-step operation feedback
- **Test results**: Detailed pass/fail for each component
- **Process information**: PIDs, names, and statuses

### **File Outputs**
- **background_processes.json**: Tracked process data
- **validation_report.json**: Environment validation results
- **Logs** (if configured): Operation logs for debugging

### **Environment Changes**
- **PATH variable**: Modified with conda/Python paths during activation
- **Environment variables**: CONDA_DEFAULT_ENV, CONDA_PREFIX, AI_PYTHON_EXE, etc.
- **Background processes**: Ollama server, Jupyter Lab, VS Code

---

## 🎨 **User Experience Features**

### **Markdown Document Viewer**
- Full markdown rendering with syntax highlighting
- Code block support with borders
- Proper formatting for headers, lists, bold, italic
- Pagination for long documents
- Used for viewing model help files and documentation

### **Enhanced Terminal**
- Custom prompt: `[AI2025-Terminal]`
- Pre-activated conda environment
- All AI packages ready
- `return_to_menu` command to return to main menu

### **Visual Clarity**
- All menus use high-contrast colors (no dark blue on black)
- Status indicators (✅ ❌ ⚠️) for quick scanning
- Organized hierarchical menus
- Clear option numbering

---

## 🚀 **Portable Design**

The system is fully portable and uses **relative paths** throughout:

- **No hard-coded drive letters**: All scripts detect their location using `%~dp0`
- **Auto-detection**: Finds Miniconda wherever it's installed
- **USB-friendly**: Can run from any drive (C:, D:, F:, etc.)
- **Folder-agnostic**: Works from any folder path
- **No registry modifications**: Everything self-contained

This makes it ideal for:
- USB-based portable development environments
- Multi-computer usage
- Testing and demonstration
- Offline AI development

---

## 📚 **Additional Resources**

### **Help System**
The `help/` directory contains detailed guides for:
- **phi_2_7b.txt**: Phi 2.7B model documentation
- **llama2_7b.txt**: Llama2 7B model documentation
- **mistral_7b.txt**: Mistral 7B model documentation
- **codellama_7b.txt**: CodeLlama 7B model documentation
- **gpt_oss_20b.txt**: GPT-OSS 20B model documentation

Each file includes:
- Model description and capabilities
- Download instructions
- Python usage examples
- Optimization tips
- Official documentation links

### **Configuration Reference**
- **version_config.json**: System version and metadata references
- **install_config.json**: Complete package requirements list
- **expected_versions.json**: File version tracking for updates

---

## 🆘 **Troubleshooting**

### **Common Issues**

**"Module not found" errors:**
- Ensure all files are extracted to the same directory
- Verify `src/` folder contains all Python modules
- Check that Python can import from relative paths

**"Python not found" errors:**
- Run **Full Activation** (Option 1)
- Verify Miniconda installation exists
- Check `setup_python_env.bat` output for errors

**"Conda environment not found":**
- Verify AI2025 environment exists in Miniconda
- Re-run `install-0` setup if environment is missing
- Check `Miniconda/envs/AI2025/` directory

**Background processes not tracked:**
- Check `background_processes.json` file permissions
- Ensure process started through the menu system
- Verify psutil package is installed

---

## 📞 **Version Checking**

To verify your installation version:

```bash
# Windows (Batch)
check_versions.bat

# Cross-platform (Python - recommended)
python check_versions.py
```

Expected output:
```
[SUCCESS] All files have correct versions (100%)
[INFO] Your AI Environment system is up to date!
```

---

**AI Environment Python System v3.0.28**
**Advanced and Modular AI Development Environment Management System** 🚀
