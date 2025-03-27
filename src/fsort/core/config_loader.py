# src/core/config_loader.py

import json
from pathlib import Path

def load_config(config_path):
    config_file = Path(config_path)
    
    if not config_file.exists():
        print(f"Erreur : le fichier de configuration '{config_path}' est introuvable.")
        exit(1)

    with open(config_file, 'r') as f:
        try:
            rules = json.load(f)
            if not rules or 'rules' not in rules:
                print("Erreur : fichier de configuration invalide ou vide.")
                exit(1)
            return rules
        except json.JSONDecodeError as e:
            print(f"Erreur de parsing JSON : {e}")
            exit(1)
