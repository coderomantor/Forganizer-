import sys
import winreg as reg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def remove_context_menu():
    if not is_admin():
        print("Please run this script as an Administrator to remove the context menu item.")
        input("Press Enter to exit...")
        sys.exit(1)

    key_path = r'Directory\\Background\\shell\\Forganizer\\'
    old_key_path = r'Directory\\Background\\shell\\Forganiser\\'

    try:
        # We need to delete subkeys before deleting the parent key
        try:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path + r"command")
        except FileNotFoundError:
            pass
        
        try:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
            print("Successfully removed 'Forganizer by Roman' from the right-click menu!")
        except FileNotFoundError:
            pass

        # Try removing the old typo'd key too just in case
        try:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, old_key_path + r"command")
        except FileNotFoundError:
            pass
            
        try:
            reg.DeleteKey(reg.HKEY_CLASSES_ROOT, old_key_path)
            print("Successfully removed the older 'Frganiser by Roman' from the right-click menu!")
        except FileNotFoundError:
            pass
            
    except Exception as e:
        print(f"Failed to remove registry keys: {e}")
        
    input("Press Enter to exit...")

if __name__ == "__main__":
    remove_context_menu()
