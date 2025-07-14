import os
import sys
from .plugin_manager import PluginManager

def start_app():
    try:
        # Get the absolute path to the current script
        plugin_src_path = 'plugins_src'

        if os.path.exists(plugin_src_path):
            full_path = os.path.abspath(plugin_src_path)
            manager = PluginManager()  # ✅ Auto-compiles plugins here
            manager.load_compiled_plugins(full_path)

    except Exception as e:
        print("Error:", e)
        input("Press Enter to exit...")
 
    # manager = PluginManager()  # ✅ Auto-compiles plugins here
    # manager.load_compiled_plugins("resources/plugin")

    # gui = DataLabGUI(manager.get_manager())
    # gui.run()
