import random
import tkinter as tk

# Create a window object
window = tk.Tk()

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char + " hi")

def return_key(event):
    print(event.char + " return key pressed")

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
window.bind("<Return>", return_key)
# Run the event loop
window.mainloop()