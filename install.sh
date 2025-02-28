#!/bin/bash
# fsort installation script - Global installation

set -e  # Exit on error

INSTALL_DIR="/usr/local/fsort"
FSORT_BIN="/usr/local/bin/fsort"
FSORT_UNINSTALL="/usr/local/bin/fsort-uninstall"

# Ensure script is run from the project root
if [[ ! -f "src/main.sh" ]]; then
    echo "[ERROR] Run this script from the project root directory."
    exit 1
fi

# Clean previous installation if exists
if [[ -d "$INSTALL_DIR" ]]; then
    echo "[INFO] Removing previous installation..."
    sudo rm -rf "$INSTALL_DIR"
fi

# Copy necessary files to /usr/local/fsort
sudo mkdir -p "$INSTALL_DIR"
sudo cp -r src "$INSTALL_DIR"
sudo cp version "$INSTALL_DIR"

# Create the fsort command
sudo bash -c "cat > $FSORT_BIN" <<EOF
#!/bin/bash

# Execute the main.sh script from the installation directory
exec bash $INSTALL_DIR/src/main.sh "\$@"
EOF

# Create the fsort-uninstall command
sudo bash -c "cat > $FSORT_UNINSTALL" <<EOF
#!/bin/bash

echo "[INFO] Uninstalling fsort..."

sudo rm -rf "$INSTALL_DIR"
sudo rm -f "$FSORT_BIN"
sudo rm -f "$FSORT_UNINSTALL"

echo "[SUCCESS] fsort has been uninstalled."
EOF

# Make the commands executable
sudo chmod +x "$FSORT_BIN" "$FSORT_UNINSTALL"

# Success message
echo "[SUCCESS] fsort installed globally. You can run it anywhere using 'fsort'."
echo "[INFO] To uninstall, use the command 'fsort-uninstall'."

# Verify installation
fsort version || echo "[ERROR] Installation verification failed."
