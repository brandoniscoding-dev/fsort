# src/commands/help.py

def help_command():
    help_text = """
    Usage:
      fsort sort <config_path>
      fsort version
      fsort help
      fsort cleanup
      fsort uninstall

    Commands:
      sort      - Sort files using the specified or default configuration
      version   - Display the current version of fsort
      help      - Display this help message
      cleanup   - Clean up sorted files (e.g., remove old logs)
      uninstall - Uninstall fsort from the system
    """
    print(help_text)

if __name__ == "__main__":
    help_command()
