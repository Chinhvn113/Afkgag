import time
import platform
import pyautogui

# Shared Settings
INTERVAL_MINUTES = 18
INTERVAL_SECONDS = INTERVAL_MINUTES * 60
screen_width, screen_height = pyautogui.size()
mid_x, mid_y = screen_width // 2, screen_height // 2

# Determine OS
IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"

if IS_WINDOWS:
    import ctypes
    import win32gui
    import win32con
    import win32api

    # Prevent sleep
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    )

    def get_roblox_hwnd():
        def enum_callback(hwnd, result):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if "Roblox" in title:
                    result.append(hwnd)
        hwnds = []
        win32gui.EnumWindows(enum_callback, hwnds)
        return hwnds[0] if hwnds else None

    def bring_window_to_front(hwnd):
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)  # ALT down
        win32gui.SetForegroundWindow(hwnd)
        win32api.keybd_event(win32con.VK_MENU, 0, win32con.KEYEVENTF_KEYUP, 0)  # ALT up

elif IS_LINUX:
    import subprocess

    def get_roblox_window_id():
        try:
            output = subprocess.check_output(['wmctrl', '-l']).decode()
            for line in output.splitlines():
                if "Roblox" in line:
                    return line.split()[0]
        except subprocess.CalledProcessError:
            return None
        return None

    def get_active_window_id():
        try:
            return subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
        except subprocess.CalledProcessError:
            return None

    def bring_window_to_front(window_id):
        subprocess.run(['xdotool', 'windowactivate', '--sync', window_id])

else:
    print("Unsupported OS.")
    exit(1)

def click_center():
    pyautogui.click(mid_x, mid_y)
    time.sleep(0.3)
    pyautogui.click(mid_x, mid_y)

print(f"Running on {'Windows' if IS_WINDOWS else 'Linux'}")
print(f"Will click Roblox every {INTERVAL_MINUTES} minutes.")
print("Press Ctrl+C to stop.")

try:
    while True:
        if IS_WINDOWS:
            prev_hwnd = win32gui.GetForegroundWindow()
            roblox_hwnd = get_roblox_hwnd()

            if roblox_hwnd:
                bring_window_to_front(roblox_hwnd)
                print("[+] Switched to Roblox")
                time.sleep(0.5)

                orig_x, orig_y = pyautogui.position()
                click_center()
                pyautogui.moveTo(orig_x, orig_y)

                if prev_hwnd != roblox_hwnd and win32gui.IsWindow(prev_hwnd):
                    bring_window_to_front(prev_hwnd)
                    print("[+] Returned to previous window.")
            else:
                print("[-] Roblox window not found.")

        elif IS_LINUX:
            prev_window = get_active_window_id()
            roblox_window = get_roblox_window_id()

            if roblox_window:
                bring_window_to_front(roblox_window)
                print("[+] Switched to Roblox")
                time.sleep(0.5)

                orig_x, orig_y = pyautogui.position()
                click_center()
                pyautogui.moveTo(orig_x, orig_y)

                if prev_window and prev_window != roblox_window:
                    bring_window_to_front(prev_window)
                    print("[+] Returned to previous window.")
            else:
                print("[-] Roblox window not found.")

        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("[!] Script stopped by user.")
