#!/usr/bin/env python3
"""
AI Environment Module v3.0.26
Date: 2025-08-14
Time: 10:30

AI Environment - Individual Application Launchers
Handles launching of specific applications (Jupyter, Streamlit, etc.)
"""

import webbrowser
import time
from pathlib import Path

try:
    from colorama import Fore, Style
except ImportError:
    class Fore:
        GREEN = RED = YELLOW = CYAN = BLUE = MAGENTA = ""
    class Style:
        RESET_ALL = ""

class AppLaunchers:
    """Handles launching of individual applications"""
    
    def __init__(self, ai_env_path, process_manager):
        self.ai_env_path = Path(ai_env_path)
        self.process_manager = process_manager
        
    def print_info(self, message):
        """Print info message"""
        print(f"{Fore.YELLOW}[INFO] {message}{Style.RESET_ALL}")
        
    def print_success(self, message):
        """Print success message"""
        print(f"{Fore.GREEN}[OK] {message}{Style.RESET_ALL}")
        
    def print_error(self, message):
        """Print error message"""
        print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}")
        
    def print_warning(self, message):
        """Print warning message"""
        print(f"{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}")

    def launch_jupyter(self):
        """Launch Jupyter Lab"""
        print(f"\n{Fore.BLUE}📊 Launching Jupyter Lab...{Style.RESET_ALL}")
        
        success = self.process_manager.launch_jupyter()
        if success:
            self.print_info("Jupyter Lab is now running in background")
            self.print_info("Use 'Background Processes' menu to manage it")
            
            # Ask if user wants to open browser
            try:
                open_browser = input(f"\n{Fore.CYAN}Open Jupyter Lab in browser? (y/n): {Style.RESET_ALL}").lower()
                if open_browser in ['y', 'yes']:
                    time.sleep(3)  # Wait for server to start
                    webbrowser.open('http://localhost:8888')
                    self.print_success("Jupyter Lab opened in browser")
            except:
                pass
                
        return success
        
    def launch_streamlit_demo(self):
        """Launch Streamlit demo application"""
        print(f"\n{Fore.BLUE}🌟 Launching Streamlit Demo...{Style.RESET_ALL}")
        
        success = self.process_manager.launch_streamlit_demo()
        if success:
            self.print_info("Streamlit demo is now running in background")
            self.print_info("Use 'Background Processes' menu to manage it")
            
            # Ask if user wants to open browser
            try:
                open_browser = input(f"\n{Fore.CYAN}Open Streamlit demo in browser? (y/n): {Style.RESET_ALL}").lower()
                if open_browser in ['y', 'yes']:
                    time.sleep(3)  # Wait for server to start
                    webbrowser.open('http://localhost:8501')
                    self.print_success("Streamlit demo opened in browser")
            except:
                pass
                
        return success
        
    def launch_python_repl(self):
        """Launch Python REPL in new terminal"""
        print(f"\n{Fore.BLUE}🐍 Launching Python REPL...{Style.RESET_ALL}")
        
        try:
            # Launch Python in a new command prompt window
            cmd = f'start "Python REPL - AI Environment" cmd /k "python"'
            
            success = self.process_manager.launch_custom_command(
                cmd, 
                "Python REPL",
                self.ai_env_path
            )
            
            if success:
                self.print_success("Python REPL launched in new terminal window")
                self.print_info("Use 'Background Processes' menu to manage it")
            return success
            
        except Exception as e:
            self.print_error(f"Failed to launch Python REPL: {e}")
            return False
            
    def launch_conda_prompt(self):
        """Launch Conda prompt in new terminal"""
        print(f"\n{Fore.BLUE}🔧 Launching Conda Prompt...{Style.RESET_ALL}")
        
        try:
            # Activate conda environment and open prompt
            conda_exe = self.ai_env_path / "Miniconda" / "Scripts" / "conda.exe"
            cmd = f'start "Conda Prompt - AI2025" cmd /k "{conda_exe} activate AI2025"'
            
            success = self.process_manager.launch_custom_command(
                cmd,
                "Conda Prompt", 
                self.ai_env_path
            )
            
            if success:
                self.print_success("Conda prompt launched in new terminal window")
                self.print_info("Use 'Background Processes' menu to manage it")
            return success
            
        except Exception as e:
            self.print_error(f"Failed to launch Conda prompt: {e}")
            return False
            
    def launch_file_explorer(self):
        """Launch File Explorer in AI Environment directory"""
        print(f"\n{Fore.BLUE}📁 Opening File Explorer...{Style.RESET_ALL}")
        
        try:
            cmd = f'explorer "{self.ai_env_path}"'
            
            success = self.process_manager.launch_custom_command(
                cmd,
                "File Explorer",
                self.ai_env_path
            )
            
            if success:
                self.print_success("File Explorer opened")
                self.print_info("Use 'Background Processes' menu to manage it")
            return success
            
        except Exception as e:
            self.print_error(f"Failed to open File Explorer: {e}")
            return False
            
    def launch_tensorboard(self, log_dir=None):
        """Launch TensorBoard"""
        print(f"\n{Fore.BLUE}📈 Launching TensorBoard...{Style.RESET_ALL}")
        
        if log_dir is None:
            log_dir = self.ai_env_path / "Projects" / "logs"
            log_dir.mkdir(parents=True, exist_ok=True)
            
        try:
            cmd = f'tensorboard --logdir="{log_dir}" --port=6006'
            
            success = self.process_manager.launch_custom_command(
                cmd,
                "TensorBoard",
                self.ai_env_path
            )
            
            if success:
                self.print_success("TensorBoard launched successfully")
                self.print_info("Access TensorBoard at: http://localhost:6006")
                self.print_info("Use 'Background Processes' menu to manage it")
                
                # Ask if user wants to open browser
                try:
                    open_browser = input(f"\n{Fore.CYAN}Open TensorBoard in browser? (y/n): {Style.RESET_ALL}").lower()
                    if open_browser in ['y', 'yes']:
                        time.sleep(3)  # Wait for server to start
                        webbrowser.open('http://localhost:6006')
                        self.print_success("TensorBoard opened in browser")
                except:
                    pass
                    
            return success
            
        except Exception as e:
            self.print_error(f"Failed to launch TensorBoard: {e}")
            return False
            
    def launch_mlflow_ui(self):
        """Launch MLflow UI"""
        print(f"\n{Fore.BLUE}🔬 Launching MLflow UI...{Style.RESET_ALL}")
        
        try:
            # Set MLflow tracking directory
            mlflow_dir = self.ai_env_path / "Projects" / "mlruns"
            mlflow_dir.mkdir(parents=True, exist_ok=True)
            
            cmd = f'mlflow ui --backend-store-uri "file:///{mlflow_dir}" --port=5000'
            
            success = self.process_manager.launch_custom_command(
                cmd,
                "MLflow UI",
                self.ai_env_path
            )
            
            if success:
                self.print_success("MLflow UI launched successfully")
                self.print_info("Access MLflow UI at: http://localhost:5000")
                self.print_info("Use 'Background Processes' menu to manage it")
                
                # Ask if user wants to open browser
                try:
                    open_browser = input(f"\n{Fore.CYAN}Open MLflow UI in browser? (y/n): {Style.RESET_ALL}").lower()
                    if open_browser in ['y', 'yes']:
                        time.sleep(3)  # Wait for server to start
                        webbrowser.open('http://localhost:5000')
                        self.print_success("MLflow UI opened in browser")
                except:
                    pass
                    
            return success
            
        except Exception as e:
            self.print_error(f"Failed to launch MLflow UI: {e}")
            return False