import os
import sys
import winreg as reg
import ctypes
from pathlib import Path

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def setup_context_menu():
    if not is_admin():
        print("Please run this script as an Administrator to add the context menu item.")
        # Only pause if not running as an executable so they see the message
        input("Press Enter to exit...")
        sys.exit(1)

    # Determine paths based on whether running as a PyInstaller executable or a Python script
    if getattr(sys, 'frozen', False):
        # Running as compiled PyInstaller executable
        cwd = Path(sys.executable).parent
        # Assuming the generated file_organiser is in the same directory and named file_organiser.exe
        target_exe = cwd / "file_organiser.exe"
        if not target_exe.exists():
             print(f"Error: Could not find {target_exe}. Please ensure both executables are in the same folder.")
             input("Press Enter to exit...")
             sys.exit(1)
        command_string = f'"{target_exe}"'
        
        # Icon could be the executable itself or bundled icon
        icon_path = cwd / "icon.ico"
        if not icon_path.exists():
            icon_path = target_exe # fallback to using the exe's embedded icon
    else:
        # Running as a normal Python script
        cwd = Path(__file__).parent.resolve()
        python_exe = Path(sys.executable)
        # Use pythonw.exe to run silently without a console window
        pythonw_exe = python_exe.parent / "pythonw.exe"
        script_path = cwd / "file_organiser.py"
        command_string = f'"{pythonw_exe}" "{script_path}"'
        icon_path = cwd / "icon.ico"

    key_path = r'Directory\\Background\\shell\\Forganizer\\'

    try:
        key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
        reg.SetValue(key, '', reg.REG_SZ, '&Forganizer by Roman') 
        reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, str(icon_path)) 
        
        key1 = reg.CreateKey(key, r"command")
        reg.SetValue(key1, '', reg.REG_SZ, command_string)
        
        print("Successfully added Forganizer to the right-click menu!")
    except Exception as e:
        print(f"Failed to add registry keys: {e}")
        
    input("Press Enter to exit...")

if __name__ == "__main__":
    setup_context_menu()
