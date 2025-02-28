# 📂 fsort - Automated File Organizer

**fsort** is a powerful tool written in **Bash** and **Python** that automatically organizes your files into directories based on defined rules. It is designed to simplify file management and optimize your workspace.

## 🚀 Main Features

- **Automatic Sorting**: Organizes your files by extensions, types, or custom rules.
- **Global Installation**: Usable from any directory.
- **Customizable**: Configure your own rules through a JSON file.
- **Easy Uninstallation**: Complete removal with a single command.

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

## 🛠️ Installation

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

1. Create a new branch:

```bash
git checkout -b feature/your_feature_name
```

2. Make your changes and test them thoroughly.

3. Submit a **pull request** to the `dev` branch.

---

## 📜 License

This project is licensed under the **MIT** License. See the `LICENSE` file for more details.

---

## 🧑‍💻 Author

Built with passion by @brandoniscoding - TechSurgeon to simplify your workflow. Contributions are always welcome!

