# src/commands/version.py

from fsort.config import VERSION_FILE
def version_command():
    try:
        with open(VERSION_FILE, 'r') as version_file:
            version = version_file.read().strip()
            print(f"fsort version: {version}")
    except FileNotFoundError:
        print("[ERROR] Version file not found.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    version_command()
