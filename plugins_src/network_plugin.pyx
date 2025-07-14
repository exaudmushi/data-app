from pluggy import HookimplMarker
import urllib.request
import socket
import psutil
import json
import os
from tkinter import ttk

hookimpl = HookimplMarker("datalab")

@hookimpl
def plugin_check():
    return True

#loads configurations
def load_config():
    # Get current working directory
    cwd = os.getcwd()

    # Build full path to config file
    config_path = os.path.join(cwd, "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    return config

config = load_config["network"]
#Checks internet availability
def check_internet(host=config["host"], port=config["host"], timeout=5):
    try :
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(host,port)
        return True
    except socket.error:
        return False
#Checks test network interfaces
@hookimpl
def test_network_interfaces():
    results = {}
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    
    for iface in interfaces:
         if stats[iface].isup:
            # Check if it's Ethernet or Wi-Fi based on naming convention
            if "eth" in iface.lower() or "en" in iface.lower():
                label = "Ethernet"
            elif "wlan" in iface.lower() or "wi" in iface.lower():
                label = "Wi-Fi"
            else:
                label = "Other"

            results[label] = check_internet()
    
    return results


@hookimpl
def plugin_install(gui_context):
    gui_context.status_label.config(text="Installing Network Plugin...")
    # Simulate installation logic here
    progress = gui_context.install_progress = gui_context.install_progress or ttk.Progressbar(
    gui_context.root, orient="horizontal", length=300, mode="determinate"
    )
    progress.pack(pady=10)
    progress["maximum"] = 100
    progress["value"] = 0

    def simulate_step(step):
        progress["value"] = step
        if step < 100:
            gui_context.root.after(100, simulate_step, step + 10)
        else:
            gui_context.status_label.config(text="Network Plugin Installed ✔️")

    # Start simulation
    gui_context.root.after(500, simulate_step, 0)
