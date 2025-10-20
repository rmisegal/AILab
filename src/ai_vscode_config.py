#!/usr/bin/env python3
"""
AI Environment Module v3.0.26
Date: 2025-08-14
Time: 10:30

AI Environment - VS Code Configuration Manager
Handles creation of VS Code workspace configurations and settings
"""

import json
from pathlib import Path

try:
    from colorama import Fore, Style
except ImportError:
    class Fore:
        GREEN = RED = YELLOW = CYAN = BLUE = MAGENTA = ""
    class Style:
        RESET_ALL = ""

class VSCodeConfigManager:
    """Manages VS Code configuration creation for AI Environment integration"""
    
    def __init__(self, ai_env_path):
        self.ai_env_path = Path(ai_env_path)
        
    def print_info(self, message):
        """Print info message"""
        print(f"{Fore.YELLOW}[INFO] {message}{Style.RESET_ALL}")
        
    def print_success(self, message):
        """Print success message"""
        print(f"{Fore.GREEN}[OK] {message}{Style.RESET_ALL}")
        
    def print_error(self, message):
        """Print error message"""
        print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}")

    def _normalize_path(self, path):
        """Convert Windows path to forward slashes for configuration files"""
        return str(path).replace('\\', '/')

    def _build_path_string(self):
        """Build PATH environment variable string"""
        ai2025_path = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025')
        ai2025_scripts = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'Scripts')
        src_path = self._normalize_path(self.ai_env_path / 'src')
        return f"{ai2025_path};{ai2025_scripts};{src_path};${{env:PATH}}"

    def _build_terminal_args(self):
        """Build terminal activation arguments"""
        activate_bat = self._normalize_path(self.ai_env_path / "Miniconda" / "Scripts" / "activate.bat")
        ai2025_env = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025")
        
        return [
            "/k",
            activate_bat,
            ai2025_env,
            "&&",
            "echo [AI2025-Terminal] Environment Active - Type 'python activate_ai_env.py' to access main menu"
        ]

    def _create_settings_json(self, vscode_dir):
        """Create enhanced settings.json configuration"""
        # Pre-process paths
        python_path = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025" / "python.exe")
        conda_path = self._normalize_path(self.ai_env_path / "Miniconda" / "Scripts" / "conda.exe")
        venv_path = self._normalize_path(self.ai_env_path / "Miniconda" / "envs")
        flake8_path = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025" / "Scripts" / "flake8.exe")
        autopep8_path = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025" / "Scripts" / "autopep8.exe")
        
        # Terminal arguments
        terminal_args = self._build_terminal_args()
        
        settings = {
            # Python Configuration - Aligned with AI Environment v3.0.26
            "python.defaultInterpreterPath": python_path,
            "python.condaPath": conda_path,
            "python.venvPath": venv_path,
            "python.terminal.activateEnvironment": True,
            "python.terminal.activateEnvInCurrentTerminal": True,
            
            # Terminal Configuration - Integrated with AI Environment System
            "terminal.integrated.defaultProfile.windows": "AI2025-Terminal",
            "terminal.integrated.profiles.windows": {
                "AI2025-Terminal": {
                    "path": "cmd.exe",
                    "args": terminal_args,
                    "icon": "snake",
                    "color": "terminal.ansiGreen"
                },
                "PowerShell": {
                    "source": "PowerShell",
                    "icon": "terminal-powershell"
                },
                "Command Prompt": {
                    "path": [
                        "${env:windir}\\Sysnative\\cmd.exe",
                        "${env:windir}\\System32\\cmd.exe"
                    ],
                    "args": [],
                    "icon": "terminal-cmd"
                }
            },
            
            # Python Linting and Formatting
            "python.linting.enabled": True,
            "python.linting.pylintEnabled": False,
            "python.linting.flake8Enabled": True,
            "python.linting.flake8Path": flake8_path,
            "python.formatting.provider": "autopep8",
            "python.formatting.autopep8Path": autopep8_path,
            
            # File Associations
            "files.associations": {"*.py": "python"},
            
            # Auto-save and formatting
            "files.autoSave": "onFocusChange",
            "editor.formatOnSave": True,
            "editor.codeActionsOnSave": {"source.organizeImports": True},
            
            # IntelliSense Configuration
            "python.analysis.typeCheckingMode": "basic",
            "python.analysis.autoImportCompletions": True,
            "python.analysis.completeFunctionParens": True,
            
            # Workspace specific settings
            "python.envFile": "${workspaceFolder}/.env",
            
            # Extension settings
            "extensions.autoUpdate": False,
            "extensions.autoCheckUpdates": False,
            
            # Disable telemetry for privacy
            "telemetry.telemetryLevel": "off",
            
            # Editor settings
            "editor.minimap.enabled": True,
            "editor.lineNumbers": "on",
            "editor.rulers": [80, 120],
            "editor.tabSize": 4,
            "editor.insertSpaces": True,
            
            # Git settings
            "git.enabled": True,
            "git.path": "git",
            
            # Jupyter settings
            "jupyter.askForKernelRestart": False,
            "jupyter.interactiveWindowMode": "single",
            
            # Search settings
            "search.exclude": {
                "**/node_modules": True,
                "**/bower_components": True,
                "**/*.code-search": True,
                "**/__pycache__": True,
                "**/*.pyc": True
            }
        }
        
        settings_file = vscode_dir / "settings.json"
        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)

    def _create_launch_json(self, vscode_dir):
        """Create enhanced launch.json configuration"""
        # Pre-process paths for launch configurations
        python_path = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025" / "python.exe")
        main_system_program = self._normalize_path(self.ai_env_path / "activate_ai_env.py")
        main_system_cwd = self._normalize_path(self.ai_env_path)
        conda_prefix_norm = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025")
        pythonpath_norm = self._normalize_path(self.ai_env_path / "src")
        ai_env_path_norm = self._normalize_path(self.ai_env_path)
        path_string = self._build_path_string()
        
        launch_config = {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "AI Environment: Current File",
                    "type": "python",
                    "request": "launch",
                    "program": "${file}",
                    "console": "integratedTerminal",
                    "cwd": "${workspaceFolder}",
                    "python": python_path,
                    "env": {
                        "CONDA_DEFAULT_ENV": "AI2025",
                        "CONDA_PREFIX": conda_prefix_norm,
                        "PATH": path_string,
                        "PYTHONPATH": pythonpath_norm,
                        "AI_ENV_PATH": ai_env_path_norm
                    },
                    "envFile": "${workspaceFolder}/.env",
                    "stopOnEntry": False,
                    "internalConsoleOptions": "neverOpen"
                },
                {
                    "name": "AI Environment: Main System",
                    "type": "python",
                    "request": "launch",
                    "program": main_system_program,
                    "console": "integratedTerminal",
                    "cwd": main_system_cwd,
                    "python": python_path,
                    "env": {
                        "CONDA_DEFAULT_ENV": "AI2025",
                        "CONDA_PREFIX": conda_prefix_norm,
                        "PATH": path_string,
                        "PYTHONPATH": pythonpath_norm
                    },
                    "stopOnEntry": False,
                    "internalConsoleOptions": "neverOpen"
                },
                {
                    "name": "AI Environment: Test Components",
                    "type": "python",
                    "request": "launch",
                    "program": main_system_program,
                    "args": ["test"],
                    "console": "integratedTerminal",
                    "cwd": main_system_cwd,
                    "python": python_path,
                    "env": {
                        "CONDA_DEFAULT_ENV": "AI2025",
                        "CONDA_PREFIX": conda_prefix_norm,
                        "PYTHONPATH": pythonpath_norm
                    }
                }
            ]
        }
        
        launch_file = vscode_dir / "launch.json"
        with open(launch_file, 'w', encoding='utf-8') as f:
            json.dump(launch_config, f, indent=2)

    def _create_tasks_json(self, vscode_dir):
        """Create enhanced tasks.json configuration"""
        # Pre-process paths for tasks
        python_path = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025" / "python.exe")
        main_system_program = self._normalize_path(self.ai_env_path / "activate_ai_env.py")
        main_system_cwd = self._normalize_path(self.ai_env_path)
        conda_prefix_norm = self._normalize_path(self.ai_env_path / "Miniconda" / "envs" / "AI2025")
        pythonpath_norm = self._normalize_path(self.ai_env_path / "src")
        path_string = self._build_path_string()
        
        tasks_config = {
            "version": "2.0.0",
            "tasks": [
                {
                    "label": "AI Environment: Run Current File",
                    "type": "shell",
                    "command": python_path,
                    "args": ["${file}"],
                    "group": {
                        "kind": "build",
                        "isDefault": True
                    },
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": False,
                        "panel": "shared",
                        "showReuseMessage": True,
                        "clear": False
                    },
                    "options": {
                        "cwd": "${workspaceFolder}",
                        "env": {
                            "CONDA_DEFAULT_ENV": "AI2025",
                            "CONDA_PREFIX": conda_prefix_norm,
                            "PATH": path_string,
                            "PYTHONPATH": pythonpath_norm
                        }
                    },
                    "problemMatcher": []
                },
                {
                    "label": "AI Environment: Open Main Menu",
                    "type": "shell",
                    "command": python_path,
                    "args": [main_system_program],
                    "group": "build",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": True,
                        "panel": "new"
                    },
                    "options": {
                        "cwd": main_system_cwd,
                        "env": {
                            "CONDA_DEFAULT_ENV": "AI2025",
                            "CONDA_PREFIX": conda_prefix_norm
                        }
                    },
                    "problemMatcher": []
                },
                {
                    "label": "AI Environment: Test All Components",
                    "type": "shell",
                    "command": python_path,
                    "args": [main_system_program, "test"],
                    "group": "test",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": True,
                        "panel": "new"
                    },
                    "options": {
                        "cwd": main_system_cwd
                    },
                    "problemMatcher": []
                }
            ]
        }
        
        tasks_file = vscode_dir / "tasks.json"
        with open(tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks_config, f, indent=2)

    def _create_extensions_json(self, vscode_dir):
        """Create extensions.json configuration"""
        extensions_config = {
            "recommendations": [
                "ms-python.python",
                "ms-python.vscode-pylance",
                "ms-python.flake8",
                "ms-python.autopep8",
                "ms-toolsai.jupyter",
                "ms-toolsai.jupyter-keymap",
                "ms-toolsai.jupyter-renderers",
                "ms-vscode.vscode-json",
                "streetsidesoftware.code-spell-checker",
                "visualstudioexptteam.vscodeintellicode",
                "ms-vscode.powershell"
            ],
            "unwantedRecommendations": [
                "ms-python.pylint"
            ]
        }
        
        extensions_file = vscode_dir / "extensions.json"
        with open(extensions_file, 'w', encoding='utf-8') as f:
            json.dump(extensions_config, f, indent=2)

    def _create_env_file(self, project_path):
        """Create .env file for AI Environment system variables"""
        # Pre-process all paths for environment file
        conda_prefix = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025')
        pythonpath_base = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025')
        pythonpath_scripts = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'Scripts')
        pythonpath_site = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'Lib' / 'site-packages')
        
        ai_env_path_norm = self._normalize_path(self.ai_env_path)
        ai_src_path_norm = self._normalize_path(self.ai_env_path / 'src')
        ai_help_path_norm = self._normalize_path(self.ai_env_path / 'help')
        
        python_path_norm = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'python.exe')
        pip_path_norm = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'Scripts' / 'pip.exe')
        conda_path_norm = self._normalize_path(self.ai_env_path / 'Miniconda' / 'Scripts' / 'conda.exe')
        
        project_root_norm = self._normalize_path(self.ai_env_path / 'Projects')
        jupyter_config_norm = self._normalize_path(self.ai_env_path / 'Projects' / '.jupyter')
        
        ollama_path_norm = self._normalize_path(self.ai_env_path / 'Ollama' / 'ollama.exe')
        
        # Build PATH components
        path_ai2025 = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025')
        path_scripts = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'Scripts')
        path_lib_bin = self._normalize_path(self.ai_env_path / 'Miniconda' / 'envs' / 'AI2025' / 'Library' / 'bin')
        path_ai_env = self._normalize_path(self.ai_env_path)
        path_src = self._normalize_path(self.ai_env_path / 'src')

        env_content = f"""# AI Environment Python System v3.0.26 - Environment Variables
# This file aligns with the AI Environment system structure

# AI2025 Conda Environment
CONDA_DEFAULT_ENV=AI2025
CONDA_PREFIX={conda_prefix}
PYTHONPATH={pythonpath_base};{pythonpath_scripts};{pythonpath_site}

# AI Environment System Paths
AI_ENV_PATH={ai_env_path_norm}
AI_SRC_PATH={ai_src_path_norm}
AI_HELP_PATH={ai_help_path_norm}

# Python Configuration
PYTHON_PATH={python_path_norm}
PIP_PATH={pip_path_norm}
CONDA_PATH={conda_path_norm}

# Project and Working Directories (AI Environment Standard)
PROJECT_ROOT={project_root_norm}
JUPYTER_CONFIG_DIR={jupyter_config_norm}
JUPYTER_DATA_DIR={jupyter_config_norm}

# Ollama AI Integration
OLLAMA_PATH={ollama_path_norm}

# Python Runtime Settings
PYTHONUNBUFFERED=1
PYTHONIOENCODING=utf-8

# PATH for AI Environment Integration
PATH={path_ai2025};{path_scripts};{path_lib_bin};{path_ai_env};{path_src}
"""
        
        env_file = project_path / ".env"
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)

    def create_enhanced_vscode_config(self, project_path):
        """Create enhanced VS Code configuration aligned with AI Environment v3.0.26"""
        try:
            # Create .vscode directory
            vscode_dir = project_path / ".vscode"
            vscode_dir.mkdir(exist_ok=True)
            
            # Create all configuration files
            self._create_settings_json(vscode_dir)
            self._create_launch_json(vscode_dir)
            self._create_tasks_json(vscode_dir)
            self._create_extensions_json(vscode_dir)
            self._create_env_file(project_path)
                
            self.print_success("Enhanced VS Code workspace configured with AI Environment v3.0.26 integration")
            self.print_info("Features enabled:")
            self.print_info("  ✓ AI2025 Python interpreter auto-detection")
            self.print_info("  ✓ [AI2025-Terminal] terminal profile")
            self.print_info("  ✓ AI Environment system integration")
            self.print_info("  ✓ Background process coordination")
            self.print_info("  ✓ Direct access to AI Environment menu")
            
        except Exception as e:
            self.print_error(f"Failed to setup enhanced VS Code workspace: {e}")

    def create_enhanced_main_py(self, main_py_path):
        """Create enhanced main.py with AI Environment integration"""
        content = '''"""
AI Environment Integration Example
Demonstrates integration with AI Environment Python System v3.0.26

This example shows how to:
1. Access AI Environment modules
2. Use Ollama AI models
3. Access background process management
4. Connect to Jupyter Lab
"""

import sys
import os
from pathlib import Path

# Add AI Environment src to path for module imports
# Try environment variable first, then search all drives
ai_env_path = None
if 'AI_ENV_PATH' in os.environ:
    ai_env_path = Path(os.environ['AI_ENV_PATH'])
else:
    # Search all drives for AI_Environment
    import string
    for letter in string.ascii_uppercase:
        drive_path = Path(f"{letter}:\\\\")
        if not drive_path.exists():
            continue
        # Check AI_Lab\\AI_Environment (external drives)
        ai_lab_path = drive_path / "AI_Lab" / "AI_Environment"
        if ai_lab_path.exists() and (ai_lab_path / "Ollama").exists():
            ai_env_path = ai_lab_path
            break
        # Check Drive:\\AI_Environment (internal drives)
        ai_env_direct = drive_path / "AI_Environment"
        if ai_env_direct.exists() and (ai_env_direct / "Ollama").exists():
            ai_env_path = ai_env_direct
            break

    if not ai_env_path:
        print("ERROR: AI_Environment not found on any drive!")
        sys.exit(1)

sys.path.insert(0, str(ai_env_path / "src"))

import requests
import json

def test_ai_environment_integration():
    """Test AI Environment system integration"""
    print("🔧 AI Environment Integration Test")
    print("=" * 50)
    
    # Test environment variables
    print(f"✓ AI Environment Path: {os.environ.get('AI_ENV_PATH', 'Not set')}")
    print(f"✓ Conda Environment: {os.environ.get('CONDA_DEFAULT_ENV', 'Not set')}")
    print(f"✓ Python Path: {os.environ.get('PYTHON_PATH', 'Not set')}")
    
    # Test AI Environment module access
    try:
        from ai_process_manager import BackgroundProcessManager
        print("✓ AI Environment modules accessible")
        
        # Test background process access
        process_manager = BackgroundProcessManager(ai_env_path)
        process_count = process_manager.get_process_count()
        print(f"✓ Background processes: {process_count} running")
        
    except ImportError as e:
        print(f"✗ AI Environment modules not accessible: {e}")
    
    print()

def query_ollama(prompt, model="phi:2.7b", host="127.0.0.1", port=11434):
    """Query Ollama AI with integration to AI Environment system"""
    url = f"http://{host}:{port}/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "No response received")
        
    except requests.exceptions.RequestException as e:
        return f"Error: {e}\\nMake sure Ollama server is running (AI Environment Menu → Option 6)"

def test_ollama_connection():
    """Test Ollama connection through AI Environment system"""
    print("🤖 Ollama AI Integration Test")
    print("=" * 50)
    
    # Check if Ollama server is accessible
    try:
        response = requests.get("http://127.0.0.1:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            print(f"✓ Ollama server is running")
            print(f"✓ Available models: {len(models)}")
            for model in models:
                print(f"  - {model.get('name', 'Unknown')}")
        else:
            print("✗ Ollama server not responding correctly")
            return False
    except requests.exceptions.RequestException:
        print("✗ Ollama server not accessible")
        print("  Start it from AI Environment Menu → Option 6: Setup Ollama Server")
        return False
    
    # Test AI query
    if models:
        print("\\n🧠 Testing AI Query...")
        model_name = models[0].get('name', 'phi:2.7b')
        prompt = "Explain what artificial intelligence is in one sentence."
        print(f"Question: {prompt}")
        print("Thinking...")
        
        response = query_ollama(prompt, model=model_name)
        print(f"AI Response: {response}")
    
    print()
    return True

def access_ai_environment_menu():
    """Show how to access AI Environment main menu"""
    print("🎛️ AI Environment Menu Access")
    print("=" * 50)
    print("From VS Code, you can access the AI Environment menu in several ways:")
    print()
    print("1. Terminal Command:")
    print("   python activate_ai_env.py")
    print()
    print("2. VS Code Task (Ctrl+Shift+P → Tasks: Run Task):")
    print("   'AI Environment: Open Main Menu'")
    print()
    print("3. Debug Configuration (F5):")
    print("   'AI Environment: Main System'")
    print()
    print("4. From Python code:")
    try:
        from ai_menu_system import MenuSystem
        from ai_action_handlers import ActionHandlers
        print("   ✓ AI Environment modules ready for programmatic access")
    except ImportError:
        print("   ✗ AI Environment modules not accessible")
    print()

def main():
    """Main function demonstrating AI Environment integration"""
    print("🚀 AI Environment Python System v3.0.26")
    print("    VS Code Integration Example")
    print("=" * 60)
    print()
    
    # Test integrations
    test_ai_environment_integration()
    test_ollama_connection()
    access_ai_environment_menu()
    
    print("💡 Next Steps:")
    print("  - Use F5 to debug this file with AI2025 interpreter")
    print("  - Open terminal (Ctrl+`) to access [AI2025-Terminal]")
    print("  - Run 'python activate_ai_env.py' to access main menu")
    print("  - Create your own AI projects in this workspace")
    print()
    print("📚 For more examples, check the help/ directory in AI Environment")

if __name__ == "__main__":
    main()
'''
        
        try:
            with open(main_py_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.print_success("Enhanced main.py created with AI Environment v3.0.26 integration")
        except Exception as e:
            self.print_error(f"Failed to create enhanced main.py: {e}")