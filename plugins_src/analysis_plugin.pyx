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

