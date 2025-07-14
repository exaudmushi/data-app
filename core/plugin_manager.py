import os
import sys
import importlib
import subprocess
import pluggy
from core.hookspec import DataLabSpecs
import time

class PluginManager:
    def __init__(self):
        self.pm = pluggy.PluginManager("datalab")
        self.pm.add_hookspecs(DataLabSpecs)

    def compile_plugins(self, setup_script="setup.py"):
        """Compiles .pyx files using the provided setup.py script."""
        if os.path.exists(setup_script):
            print("🔧 Compiling plugins with setup.py...")
            result = subprocess.run(
                [sys.executable, setup_script, "build_ext", "--inplace"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print("✅ Plugins compiled successfully")
            else:
                print("❌ Compilation failed")
                print(result.stdout)
                print(result.stderr)
        else:
            print(f"⚠️ No setup.py found at: {setup_script}")

    def load_compiled_plugins(self, plugin_folder):
        """Loads compiled plugins (.pyd files) from specified folder."""
        sys.path.append(plugin_folder)
        for file in os.listdir(plugin_folder):
            module_name = file[:]
            try:
                if module_name == "setup.py":
                    plugin_src_path = 'plugins_src'
                    filename = "setup.py"
                    filepath = os.path.join(plugin_src_path, "setup.py")
                    if os.path.isfile(filepath): # Skip directories 
                        stat = os.stat(filepath)
                        size = stat.st_size 
                        mtime = time.ctime(stat.st_mtime) 
                        print(f"{filepath} {filename:20} {size:8} bytes modified {mtime}") 
                       
                        PluginManager.compile_plugins(self, setup_script=filepath)
                        # plugin = importlib.import_module(module_name)
                        # self.pm.register(plugin)
                        # print(f"✅ Loaded plugin: {module_name}")
            except Exception as e:
                    print(f"❌ Error loading {module_name}: {e}")
        

    def get_manager(self):
        return self.pm

    def get_plugins(self):
        return [plugin.__name__ for plugin in self.pm.get_plugins()]
