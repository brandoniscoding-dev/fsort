# src/commands/uninstall.py

import os
import shutil

def uninstall_command():
    INSTALL_DIR = "/usr/local/fsort"
    if os.path.exists(INSTALL_DIR):
        shutil.rmtree(INSTALL_DIR)
        print("[INFO] fsort has been uninstalled.")
    else:
        print("[ERROR] fsort is not installed.")

if __name__ == "__main__":
    uninstall_command()
