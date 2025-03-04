# 📂 fsort - Automated File Organizer

**fsort** is a robust and efficient tool crafted in **Bash** and **Python** that automatically organizes your files into directories based on customizable rules. Designed to simplify file management and streamline your workflow.

---

## 🚀 Main Features

- ✅ **Automatic Sorting**: Categorizes files by extensions, types, or user-defined rules.
- 🌐 **Global Installation**: Accessible from any directory system-wide.
- ⚙️ **Highly Customizable**: Define your own sorting rules via a JSON configuration.
- 🗑️ **Easy Uninstallation**: Remove the tool completely with a single command.

---

## 📋 Requirements

- **Operating System**: Linux (tested on Ubuntu)
- **Dependencies**: `bash`, `python3`

Check the prerequisites with:

```bash
bash --version
python3 --version
```

---

## 🛠️ Installation (For Developers)

1. Clone the repository:

```bash
git clone https://github.com/brandoniscoding-dev/fsort.git
cd fsort
```

2. Run the installation script:

```bash
sudo bash install.sh
```

✅ **fsort** is now globally available!

---

## 📦 Installation (For Users)

You can download and install **fsort** using the `.deb` package or the compressed archive:

1. **Using the `.deb` package** (Recommended for Ubuntu/Debian-based systems):

```bash
wget https://github.com/brandoniscoding-dev/fsort/releases/download/v1.0.0/fsort_1.0.0.deb
sudo dpkg -i fsort_1.0.0.deb
```

2. **Using the `.tar.gz` archive** (Manual installation):

```bash
wget https://github.com/brandoniscoding-dev/fsort/releases/download/v1.0.0/fsort-1.0.0.tar.gz
sudo tar -xzf fsort-1.0.0.tar.gz -C /usr/local/bin
```

---

## 📖 Usage

### 1. Sort Files

To execute the sorting process with the default configuration:

```bash
fsort sort
```

To specify a custom configuration file:

```bash
fsort sort /path/to/your_config.json
```

### 2. Display Version

```bash
fsort version
```

### 3. Uninstall the Tool

```bash
fsort-uninstall
```

---

## 📐 Example Configuration

Customize sorting rules by modifying a JSON file. Here is an example:

```json
{
  "rules": [
    {
      "name": "Images",
      "target": "~/Images",
      "patterns": ["*.jpg", "*.png"]
    },
    {
      "name": "Documents",
      "target": "~/Documents",
      "patterns": ["*.pdf", "*.docx"]
    }
  ]
}
```

---

## 📚 Contribute

We welcome contributions to improve **fsort**!

1. Fork the repository and create a new branch:

```bash
git checkout -b feature/your_feature_name
```

2. Implement and test your changes thoroughly.

3. Submit a **pull request** to the `dev` branch.

---

## 📜 License

This project is licensed under the **MIT** License. See the `LICENSE` file for full details.

---

## 🧑‍💻 Author

Built with passion by [@brandoniscoding](https://github.com/brandoniscoding) - **TechSurgeon** simplifying your workflow. Contributions and feedback are always welcome!
