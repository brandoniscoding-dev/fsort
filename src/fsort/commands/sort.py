# src/commands/sort.py

import argparse
from fsort.config import RULES_FILE
from fsort.core.config_loader import load_config
from fsort.core.rules_parser import validate_rules
from fsort.core.file_sorter import sort_files

def sort_command(config_path):
    rules = load_config(config_path)
    
    if validate_rules(rules):
        sort_files(rules)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort files based on rules.")
    parser.add_argument('--config', default=RULES_FILE, help="Path to the JSON configuration file.")
    args = parser.parse_args()

    sort_command(args.config)