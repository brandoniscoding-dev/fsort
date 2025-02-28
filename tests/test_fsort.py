import unittest
import subprocess
import tempfile
import os
import json
import shutil
from pathlib import Path

FSORT_SCRIPT = os.path.abspath("./src/main.sh")
CONFIG_PATH = os.path.abspath("./src/config/rules.json")  

class TestFsort(unittest.TestCase):
    def setUp(self):
        """Set up an isolated test environment."""
        self.test_dir = tempfile.TemporaryDirectory()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir.name)

        # Copy core.py and its dependencies to the temporary directory
        shutil.copytree(
            os.path.join(self.original_cwd, "src"),
            os.path.join(self.test_dir.name, "src")
        )

        # Create a version file
        (Path(self.test_dir.name) / "version").write_text("fsort version 1.0.0\n")

        # Create test files
        (Path(self.test_dir.name) / "test.txt").touch()
        (Path(self.test_dir.name) / "image.jpg").touch()

    def tearDown(self):
        """Clean up the test environment."""
        os.chdir(self.original_cwd)
        self.test_dir.cleanup()

    def run_fsort(self, action, config_path=None):
        """Run fsort and return the result."""
        cmd = [FSORT_SCRIPT, action]
        if config_path:
            cmd.append(config_path)
        return subprocess.run(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, 
            text=True
        )

    def test_sort_valid_files(self):
        """Test file sorting based on rules."""
        # Create a test JSON configuration file
        test_config = Path(self.test_dir.name) / "test_rules.json"
        test_config.write_text(json.dumps({
            "rules": [
                {
                    "name": "Test Docs",
                    "target": "Documents",
                    "patterns": ["*.txt"]
                },
                {
                    "name": "Test Images",
                    "target": "Images",
                    "patterns": ["*.jpg"]
                }
            ]
        }))

        result = self.run_fsort("sort", str(test_config))
        
        # Verify file movement
        self.assertTrue((Path("Documents") / "test.txt").exists())
        self.assertTrue((Path("Images") / "image.jpg").exists())
        self.assertEqual(result.returncode, 0)

    def test_version_command(self):
        """Test the version command."""
        result = self.run_fsort("version")
        self.assertIn("fsort version 1.0.0", result.stdout)
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()