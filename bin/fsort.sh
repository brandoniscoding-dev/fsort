#!/bin/bash
# fsort - Main entry point for the file sorting system
# Usage:
#   ./fsort.sh <command> [args]
# Commands:
# sort      - Sort files using the specified or default configuration
# version   - Display usage information of fsort
# help      - Display usage information
# cleanup   - Clean up sorted files (e.g., remove old logs)
# stats     - Display statistics on moved files
# uninstall - Uninstall fsort from the system

FSORT_DIR="/usr/local/fsort"

ACTION=$1
CONFIG_PATH="${2:-$FSORT_DIR/fsort/rules.json}"  # Chemin corrigé vers rules.json

case "$ACTION" in
    "sort")
        python3 -m fsort.commands.sort --config "$CONFIG_PATH"  # Chemin corrigé
        ;;
    "version")
        python3 -m fsort.commands.version  # Chemin corrigé
        ;;
    "help")
        python3 -m fsort.commands.help  # Chemin corrigé
        ;;
    "cleanup")
        python3 -m fsort.commands.cleanup  # Chemin corrigé
        ;;
    "uninstall")
        python3 -m fsort.commands.uninstall  # Chemin corrigé
        ;;
    *)
        echo "[ERROR] Invalid command: $ACTION"
        echo "Run 'fsort help' for usage information"
        exit 1
        ;;
esac
