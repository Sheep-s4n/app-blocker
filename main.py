import win32gui
import ctypes
from time import sleep
from dragonfly import Window


apps_to_block = ["epic" , "fornite"]
pop_up = "Get back to work !!!!!!!"

# Callback function to handle window events
def window_callback(hwnd, lParam):
    window_title = win32gui.GetWindowText(hwnd)
    process_name = win32gui.GetClassName(hwnd)  # You can use other methods to get process name

    # Check if the window title or process name matches the apps to block
    if any(app.lower() in window_title.lower() or app.lower() in process_name.lower() for app in apps_to_block):
        print(f"Detected {process_name} window with title: {window_title}")
        window = Window.get_matching_windows(title=window_title)[0]
        Window.close(window)
        ctypes.windll.user32.MessageBoxW(0, pop_up, 'Alert!', 0x0001030)

# Register the callback function for window events
while True:
    win32gui.EnumWindows(window_callback, 0)
    sleep(2)