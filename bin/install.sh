#!/bin/bash
# fsort installation script - Global installation

set -e  # Exit on error

INSTALL_DIR="/usr/local/fsort"
FSORT_BIN="/usr/local/bin/fsort"
FSORT_UNINSTALL="/usr/local/bin/fsort-uninstall"

# ASCII Art Header with colors
echo -e "\e[1;34m********************************************************\e[0m"
echo -e "\e[1;32m*     Welcome to the fsort Installation!               *\e[0m"
echo -e "\e[1;32m*     Sorting files made easy. Let's get started!      *\e[0m"
echo -e "\e[1;34m********************************************************\e[0m"
echo

# ASCII Art for fsort
echo -e "\
                                               ___     
  .--.,                                      ,--.'|_   
,--.'  \                 ,---.     __  ,-.   |  | :,'  
|  | /\/   .--.--.      '   ,'\  ,' ,'/ /|   :  : ' :  
:  : :    /  /    '    /   /   | '  | |' | .;__,'  /   
:  | |-, |  :  /\`./   .   ; ,. : |  |   ,' |  |   |    
|  : :/| |  :  ;_     '   | |: : '  :  /   :__,'| :    
|  |  .'  \  \    \`.  '   | .; : |  | '      '  : |__  
'  : '     \`----.   \ |   :    | ;  : |      |  | '.'| 
|  | |    /  /\`--'  /  \   \  /  |  , ;      ;  :    ; 
|  : \   '--'.     /    \`----'    ---'       |  ,   /  
|  |,'     \`--'---'                           ---\`-'   
\`--'    "
echo

echo -e "\e[1;33mInstalling fsort... Please wait.\e[0m"

# Ensure script is run from the project root
if [[ ! -f "bin/fsort.sh" ]]; then
    echo "[ERROR] Please run this script from the project root directory."
    exit 1
fi

# Clean previous installation if exists
if [[ -d "$INSTALL_DIR" ]]; then
    echo "[INFO] Cleaning previous installation..."
    sudo rm -rf "$INSTALL_DIR"
fi

# Create the installation directory
echo "[INFO] Creating installation directory at $INSTALL_DIR..."
sudo mkdir -p "$INSTALL_DIR"

# Copy necessary files to /usr/local/fsort
echo "[INFO] Copying necessary files to $INSTALL_DIR..."
sudo cp -r . "$INSTALL_DIR"

# Create the fsort command
echo "[INFO] Creating the 'fsort' command at $FSORT_BIN..."
sudo bash -c "cat > $FSORT_BIN" <<EOF
#!/bin/bash

# Set PYTHONPATH to include the src directory and execute the fsort.sh script
export PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR/src
exec bash $INSTALL_DIR/bin/fsort.sh "\$@"
EOF

# Make the fsort command executable
sudo chmod +x "$FSORT_BIN"

# Create the fsort-uninstall command
echo "[INFO] Creating the uninstall command at $FSORT_UNINSTALL..."
sudo bash -c "cat > $FSORT_UNINSTALL" <<EOF
#!/bin/bash

# Uninstall script for fsort
echo "[INFO] Uninstalling fsort..."
sudo rm -rf "$INSTALL_DIR"
sudo rm -f "$FSORT_BIN"
sudo rm -f "$FSORT_UNINSTALL"

echo "[SUCCESS] fsort has been uninstalled."
EOF

# Make the uninstall command executable
sudo chmod +x "$FSORT_UNINSTALL"

# Success message with ASCII Art and colors
echo
echo -e "\e[1;34m*******************************************************\e[0m"
echo -e "\e[1;32m*               Installation Complete!                *\e[0m"
echo -e "\e[1;32m*                                                     *\e[0m"
echo -e "\e[1;32m*      fsort is now installed globally. You can run   *\e[0m"
echo -e "\e[1;32m*      it anywhere using the command:                 *\e[0m"
echo -e "\e[1;32m*                                                     *\e[0m"
echo -e "\e[1;32m*                 'fsort'                             *\e[0m"
echo -e "\e[1;32m*                                                     *\e[0m"
echo -e "\e[1;32m*      To uninstall, simply run:                      *\e[0m"
echo -e "\e[1;32m*                                                     *\e[0m"
echo -e "\e[1;32m*               'fsort uninstall'                     *\e[0m"
echo -e "\e[1;34m*******************************************************\e[0m"
echo

# Verify installation
fsort version || echo "[ERROR] Installation verification failed."

# Optional: ASCII art separator for visual appeal
echo -e "\e[1;34m********************************************************\e[0m"
