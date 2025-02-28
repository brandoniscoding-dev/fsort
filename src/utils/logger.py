from pathlib import Path
from datetime import datetime

LOG_FILE = Path("logs/fsort.log")

def setup_logger():
    """
    Ensure the log directory exists and return the log file in append mode.

    :return: File object opened in append mode.
    """
    LOG_FILE.parent.mkdir(exist_ok=True, parents=True)
    return LOG_FILE.open("a")

def log_action(action, src, dest):
    """
    Record an action in the log file.

    :param action: Type of action (e.g., 'MOVED', 'ERROR').
    :param src: Source path of the file.
    :param dest: Destination path or error message.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with setup_logger() as log_file:
        log_file.write(f"{timestamp} | {action} | {src} | {dest}\n")
