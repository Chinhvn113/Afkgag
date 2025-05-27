
# 🎮 Roblox Auto-Clicker (Cross-Platform: Windows & Linux)

This is a cross-platform Python script that automatically:
- Detects whether you're running on **Windows** or **Linux** (Ubuntu/Mint),
- Searches for a **Roblox** window every 18 minutes,
- Brings it to the front,
- Simulates two center-screen mouse clicks,
- Returns to the previously active window,
- Prevents system sleep on **Windows**.

## 🧩 Features

✅ Cross-platform (Windows/Linux)  
✅ Simulates Roblox interaction to prevent AFK kick  
✅ Restores your original window after clicking  
✅ Preserves mouse position  
✅ Prevents sleep on Windows  
✅ X11-compatible (Linux Mint, Ubuntu)  
✅ Lightweight — no GUI required

## 🖥️ Requirements

### 🔹 Windows

Install dependencies via `pip`:

```bash
pip install pyautogui pywin32
```

### 🔹 Linux (Ubuntu / Linux Mint)

Install system dependencies:

```bash
sudo apt update
sudo apt install xdotool wmctrl x11-utils
```

Install Python package:

```bash
pip install pyautogui
```

## 🚀 How to Use

1. Make sure **Roblox is running** and visible.
2. Run the script:

```bash
python3 roblox_autoclicker.py
```

3. Leave it running in the background — it will click Roblox every **18 minutes** and return to your current window.

## 🔐 Prevent Sleep (Linux Only)

To stop your system from going idle while this script runs:

```bash
systemd-inhibit --what=idle python3 afk.py
```

Or manually disable sleep:

```bash
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

To re-enable:

```bash
sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target
```

## 🛠 Configuration

To change the click interval, edit this line in the script:

```python
INTERVAL_MINUTES = 18
```

## ❗ Known Limitations

- **Wayland is not supported**. Script works only under **X11** (default for Linux Mint and most Ubuntu setups).
- Roblox window **must contain the word "Roblox"** in its title.
- No click animation; it sends synthetic mouse clicks silently.

## 📄 License

MIT License — free to use, modify, and distribute.
