from pathlib import Path

# Remonter à la vraie racine du projet
PROJECT_ROOT = Path(__file__).resolve().parents[2]  

# Fichiers de configuration
VERSION_FILE = PROJECT_ROOT / 'version'
RULES_FILE = PROJECT_ROOT / 'src' / 'config' / 'rules.json'  # Correction ici
