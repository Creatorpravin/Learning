import shutil
import subprocess
import os
import tkinter as tk
from tkinter import filedialog

def move_config_and_restart_openvpn(config_file_path):
    # Path to the OpenVPN folder
    openvpn_folder = "/etc/openvpn/"

    # Move the OpenVPN configuration file to the OpenVPN folder
    try:
        shutil.copy(config_file_path, openvpn_folder)
        print(f"Configuration file moved to {openvpn_folder}")
    except Exception as e:
        print(f"Error moving configuration file: {e}")
        return

    # Restart the OpenVPN service
    try:
        subprocess.run(["sudo", "systemctl", "restart", "openvpn"])
        print("OpenVPN service restarted")
    except Exception as e:
        print(f"Error restarting OpenVPN service: {e}")

def browse_file():
    file_path = filedialog.askopenfilename(title="Select OpenVPN Configuration File")
    if file_path:
        entry_var.set(file_path)

def on_submit():
    openvpn_conf_file_path = entry_var.get()
    if os.path.isfile(openvpn_conf_file_path):
        move_config_and_restart_openvpn(openvpn_conf_file_path)
        status_label.config(text="OpenVPN configured and restarted.")
    else:
        status_label.config(text="OpenVPN configuration file not found.")

# Create the main window
root = tk.Tk()
root.title("OpenVPN Configurator")

# Create and pack widgets
label = tk.Label(root, text="Select OpenVPN Configuration File:")
label.pack(pady=10)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=40)
entry.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Run the main loop
root.mainloop()
