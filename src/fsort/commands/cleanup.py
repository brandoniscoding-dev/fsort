# src/commands/cleanup.py

import os

def cleanup_command():
    target_dir = "sorted_files_logs"
    if os.path.exists(target_dir):
        for file in os.listdir(target_dir):
            if file.endswith(".log"):
                os.remove(os.path.join(target_dir, file))
        print(f"Cleaned up .log files in {target_dir}")
    else:
        print(f"No logs found in {target_dir}")

if __name__ == "__main__":
    cleanup_command()
