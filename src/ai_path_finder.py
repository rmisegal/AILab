#!/usr/bin/env python3
"""
AI Path Finder - Finds AI_Environment across all drives
Shared utility for all AI Environment modules
"""

import string
from pathlib import Path
from typing import Optional


def find_ai_environment(verbose: bool = False) -> Optional[Path]:
    """
    Find AI_Environment installation across all drives.
    Searches for AI_Environment in both external (AI_Lab) and internal locations.

    Args:
        verbose: If True, print debug messages

    Returns:
        Path to AI_Environment or None if not found
    """
    # Search all drives for AI_Environment
    for letter in string.ascii_uppercase:
        drive_path = Path(f"{letter}:\\")

        if not drive_path.exists():
            continue

        # Check AI_Lab\AI_Environment (external drives)
        ai_lab_path = drive_path / "AI_Lab" / "AI_Environment"
        if ai_lab_path.exists() and ai_lab_path.is_dir():
            if (ai_lab_path / "Ollama").exists() or (ai_lab_path / "Miniconda").exists():
                if verbose:
                    print(f"[VERBOSE] Found AI_Environment at: {ai_lab_path}")
                return ai_lab_path

        # Check Drive:\AI_Environment (internal drives)
        ai_env_path = drive_path / "AI_Environment"
        if ai_env_path.exists() and ai_env_path.is_dir():
            if (ai_env_path / "Ollama").exists() or (ai_env_path / "Miniconda").exists():
                if verbose:
                    print(f"[VERBOSE] Found AI_Environment at: {ai_env_path}")
                return ai_env_path

    if verbose:
        print("[VERBOSE] AI_Environment not found on any drive")
    return None


def main():
    """Test path finder"""
    print("Searching for AI_Environment...")
    ai_env_path = find_ai_environment(verbose=True)

    if ai_env_path:
        print(f"\nFound: {ai_env_path}")
    else:
        print("\nNot found")


if __name__ == "__main__":
    main()
