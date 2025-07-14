import tkinter as tk
from tkinter import ttk, messagebox

class DataLabGUI:
    def __init__(self, plugin_manager):
        self.root = tk.Tk()
        self.root.title("DataLab")
        self.root.geometry("1920x1080")
        self.plugin_manager = plugin_manager

        self.status_label = ttk.Label(self.root, text="Checking plugins...")
        self.status_label.pack(pady=10)

        self.check_plugins()

    def check_plugins(self):
        results = self.plugin_manager.hook.plugin_check()
        if all(results):
            messagebox.showinfo("Plugins", "All plugins are available.")
        else:
            messagebox.showwarning("Plugins", "Some plugins are missing.")

    def run(self):
        self.root.mainloop()
