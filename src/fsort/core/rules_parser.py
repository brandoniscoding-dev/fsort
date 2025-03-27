# src/core/rules_parser.py

def validate_rules(rules):
    for rule in rules.get('rules', []):
        if not rule.get('name') or not rule.get('target') or not rule.get('patterns'):
            print(f"Erreur : La règle {rule.get('name', 'Unnamed')} est invalide.")
            return False
    return True
