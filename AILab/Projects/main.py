"""
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
ai_env_path = Path(os.environ.get('AI_ENV_PATH', 'D:/AI_Environment'))
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
        return f"Error: {e}\nMake sure Ollama server is running (AI Environment Menu → Option 6)"

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
        print("\n🧠 Testing AI Query...")
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
