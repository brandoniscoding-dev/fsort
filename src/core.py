import os
import shutil
import json
import argparse
from pathlib import Path
from utils.logger import log_action

CONFIG_PATH = 'src/config/rules.json'

def load_rules(config_path):
    """
    Load sorting rules from a JSON configuration file.

    :param config_path: Path to the configuration file.
    :return: Dictionary containing the sorting rules.
    """
    config_file = Path(config_path)

    if not config_file.exists():
        print(f"Error: Configuration file '{config_path}' not found.")
        exit(1)

    with open(config_file, 'r') as f:
        try:
            rules = json.load(f)  
            if not rules or 'rules' not in rules:
                print("Error: Invalid or empty configuration file.")
                exit(1)
            return rules
        except json.JSONDecodeError as e:
            print(f"JSON Parsing Error: {e}")
            exit(1)

def process_rules(rules):
    """
    Apply sorting rules: move files to their target directories.

    :param rules: Dictionary containing the loaded rules.
    """
    for rule in rules.get('rules', []):
        rule_name = rule.get('name', 'Unnamed Rule')
        target_dir = Path(rule['target'])
        target_dir.mkdir(exist_ok=True, parents=True)

        for pattern in rule['patterns']:
            for path in Path('.').glob(pattern):
                if path.is_file():
                    dest = target_dir / path.name
                    try:
                        shutil.move(str(path), str(dest))
                        log_action(f"MOVED ({rule_name})", path, dest)
                    except Exception as e:
                        log_action(f"ERROR ({rule_name})", path, f"Move failed: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Automated file sorting system.")
    parser.add_argument('--action', required=True, choices=['sort'], help="Action to perform (e.g., sort).")
    parser.add_argument('--config', default=CONFIG_PATH, help="Path to the JSON configuration file.")
    args = parser.parse_args()

    if args.action == 'sort':
        rules = load_rules(args.config)
        process_rules(rules)