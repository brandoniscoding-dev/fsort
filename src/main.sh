#!/bin/bash
# fsort - Main entry point for the file sorting system
# Usage:
#   ./main.sh <action> [config_path]
#
# Actions:
#   sort      - Sort files using the specified or default configuration
#   version   - Display the current version of fsort
#
# Example:
#   ./main.sh sort                # Use the default config (./src/config/rules.json)
#   ./main.sh sort ./myrules.json # Use a custom config
#   ./main.sh version             # Display the fsort version

FSORT_DIR="/usr/local/fsort"

ACTION=$1
CONFIG_PATH="${2:-$FSORT_DIR/src/config/rules.json}"

case "$ACTION" in 
    "sort")
        python3 "$FSORT_DIR/src/core.py" --action sort --config "$CONFIG_PATH"
        ;;
    "version")
        cat "$FSORT_DIR/version"
        ;;
    *)
        echo "[ERROR] Invalid command: $ACTION"
        echo "Usage: $0 {sort|version} [config_path]"
        exit 1
        ;;
esac
