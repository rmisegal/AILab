#!/usr/bin/env python3
"""
AI2025 Terminal Functionality Tests
Tests all features of the AI2025 Enhanced Terminal

Run this script in the AI2025 Terminal to verify everything works:
    python test_ai2025_terminal.py
"""

import sys
import os
import subprocess
from pathlib import Path

class TerminalTester:
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0
        self.test_results = []

    def print_header(self):
        print("\n" + "="*70)
        print("🧪 AI2025 Terminal Functionality Tests")
        print("="*70 + "\n")

    def print_test(self, test_name, status, message=""):
        icon = "✅" if status else "❌"
        result_text = "PASS" if status else "FAIL"
        print(f"{icon} Test {len(self.test_results) + 1}: {test_name} ... {result_text}")
        if message:
            print(f"   ℹ️  {message}")

        self.test_results.append({
            'name': test_name,
            'passed': status,
            'message': message
        })

        if status:
            self.tests_passed += 1
        else:
            self.tests_failed += 1

    def test_conda_environment(self):
        """Test if AI2025 conda environment is active"""
        try:
            conda_env = os.environ.get('CONDA_DEFAULT_ENV', '')
            passed = conda_env == 'AI2025'
            self.print_test(
                "Conda Environment Active",
                passed,
                f"Current environment: {conda_env}" if conda_env else "No conda environment detected"
            )
            return passed
        except Exception as e:
            self.print_test("Conda Environment Active", False, f"Error: {e}")
            return False

    def test_python_version(self):
        """Test Python version"""
        try:
            version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
            passed = sys.version_info.major == 3 and sys.version_info.minor >= 10
            self.print_test(
                "Python Version",
                passed,
                f"Python {version} (expected 3.10+)"
            )
            return passed
        except Exception as e:
            self.print_test("Python Version", False, f"Error: {e}")
            return False

    def test_working_directory(self):
        """Test if working directory is correct"""
        try:
            cwd = Path.cwd()
            ai_env_path = os.environ.get('AI_ENV_PATH', '')
            # Check if we're in AI_Lab or a subdirectory
            passed = 'AI_Lab' in str(cwd) or 'AI_Environment' in str(cwd)
            self.print_test(
                "Working Directory",
                passed,
                f"Current: {cwd}"
            )
            return passed
        except Exception as e:
            self.print_test("Working Directory", False, f"Error: {e}")
            return False

    def test_critical_packages(self):
        """Test if critical AI packages are available"""
        packages_to_test = [
            ('langchain', 'LangChain'),
            ('streamlit', 'Streamlit'),
            ('fastapi', 'FastAPI'),
            ('pandas', 'Pandas'),
            ('numpy', 'NumPy'),
            ('torch', 'PyTorch'),
            ('tensorboard', 'TensorBoard'),
            ('mlflow', 'MLflow'),
        ]

        all_passed = True
        missing_packages = []

        for package_name, display_name in packages_to_test:
            try:
                __import__(package_name)
            except ImportError:
                all_passed = False
                missing_packages.append(display_name)

        self.print_test(
            "Critical AI Packages",
            all_passed,
            f"Missing packages: {', '.join(missing_packages)}" if missing_packages else "All packages available"
        )
        return all_passed

    def test_package_imports(self):
        """Test importing specific critical packages"""
        test_cases = [
            ('tensorboard', 'TensorBoard'),
            ('mlflow', 'MLflow'),
        ]

        for package_name, display_name in test_cases:
            try:
                module = __import__(package_name)
                version = getattr(module, '__version__', 'unknown')
                self.print_test(
                    f"Import {display_name}",
                    True,
                    f"Version: {version}"
                )
            except ImportError as e:
                self.print_test(
                    f"Import {display_name}",
                    False,
                    f"Import failed: {e}"
                )

    def test_pip_command(self):
        """Test if pip is available and working"""
        try:
            result = subprocess.run(
                ['pip', '--version'],
                capture_output=True,
                text=True,
                timeout=10
            )
            passed = result.returncode == 0
            self.print_test(
                "Pip Command Available",
                passed,
                result.stdout.strip() if passed else result.stderr.strip()
            )
            return passed
        except Exception as e:
            self.print_test("Pip Command Available", False, f"Error: {e}")
            return False

    def test_conda_command(self):
        """Test if conda command is available"""
        try:
            result = subprocess.run(
                ['conda', '--version'],
                capture_output=True,
                text=True,
                timeout=10
            )
            passed = result.returncode == 0
            self.print_test(
                "Conda Command Available",
                passed,
                result.stdout.strip() if passed else result.stderr.strip()
            )
            return passed
        except Exception as e:
            self.print_test("Conda Command Available", False, f"Error: {e}")
            return False

    def test_environment_variables(self):
        """Test if important environment variables are set"""
        try:
            ai_env_path = os.environ.get('AI_ENV_PATH', '')
            conda_path = os.environ.get('CONDA_PATH', '')

            passed = bool(ai_env_path)
            self.print_test(
                "Environment Variables Set",
                passed,
                f"AI_ENV_PATH: {ai_env_path if ai_env_path else 'Not set'}"
            )
            return passed
        except Exception as e:
            self.print_test("Environment Variables Set", False, f"Error: {e}")
            return False

    def test_prompt_customization(self):
        """Test if custom prompt is set"""
        try:
            prompt = os.environ.get('PROMPT', '')
            passed = 'AI2025-Terminal' in prompt
            self.print_test(
                "Custom Prompt Set",
                passed,
                f"Prompt: {prompt[:50]}..." if len(prompt) > 50 else f"Prompt: {prompt}"
            )
            return passed
        except Exception as e:
            self.print_test("Custom Prompt Set", False, f"Error: {e}")
            return False

    def test_return_command_exists(self):
        """Test if return_to_menu command exists"""
        try:
            temp_path = Path(os.environ.get('TEMP', ''))
            return_script = temp_path / "return_to_menu.bat"
            passed = return_script.exists()
            self.print_test(
                "Return Command Available",
                passed,
                f"Script location: {return_script}" if passed else "return_to_menu.bat not found in TEMP"
            )
            return passed
        except Exception as e:
            self.print_test("Return Command Available", False, f"Error: {e}")
            return False

    def print_summary(self):
        """Print test summary"""
        print("\n" + "="*70)
        print("📊 Test Summary")
        print("="*70)
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_failed}")
        print(f"📈 Success Rate: {(self.tests_passed / (self.tests_passed + self.tests_failed) * 100):.1f}%")
        print("="*70 + "\n")

        if self.tests_failed == 0:
            print("🎉 All tests passed! AI2025 Terminal is fully functional!")
        else:
            print("⚠️  Some tests failed. Please review the results above.")
            print("\nFailed Tests:")
            for result in self.test_results:
                if not result['passed']:
                    print(f"  • {result['name']}: {result['message']}")
        print()

    def run_all_tests(self):
        """Run all tests"""
        self.print_header()

        print("🔍 Running Environment Tests...")
        print("-" * 70)
        self.test_conda_environment()
        self.test_python_version()
        self.test_working_directory()
        self.test_environment_variables()
        self.test_prompt_customization()

        print("\n🔍 Running Command Tests...")
        print("-" * 70)
        self.test_pip_command()
        self.test_conda_command()
        self.test_return_command_exists()

        print("\n🔍 Running Package Tests...")
        print("-" * 70)
        self.test_critical_packages()
        self.test_package_imports()

        self.print_summary()

        return self.tests_failed == 0

def main():
    """Main test runner"""
    tester = TerminalTester()
    success = tester.run_all_tests()

    # Return exit code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
