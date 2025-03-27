# src/core/file_sorter.py

import shutil
from pathlib import Path
from utils.logger import log_action

def sort_files(rules):
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
