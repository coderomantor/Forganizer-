import os
import sys
import winreg as reg

cwd = os.getcwd()
python_exe = sys.executable

hidden_terminal = '\\'.join(python_exe.split('\\')[:-1]) + "\\pythonw.exe"
key_path = r'Directory\\Background\\shell\\Forganiser\\'  # Change 'Forganiser' to the name of your project
icon_path = f'{cwd}\\icon.ico'  # Update this path to your icon file location
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Frganiser by Roman')  # Change 'Frganise folder' to the function of your script
reg.SetValueEx(key, 'Icon', 0, reg.REG_SZ, icon_path)  # Assign the icon path to the menu entry
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\file_organiser.py"')  # Change 'file_organiser.py' to the name of your script
