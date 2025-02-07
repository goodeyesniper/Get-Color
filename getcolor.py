import tkinter as tk
from PIL import ImageGrab
import pyautogui

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Get Color")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        self.hex_label = tk.Label(root, text="Hex: #FFFFFF", font=("Arial", 14))
        self.hex_label.pack(pady=10)

        self.rgba_label = tk.Label(root, text="RGBA: (255, 255, 255, 255)", font=("Arial", 14))
        self.rgba_label.pack(pady=10)

        self.color_display = tk.Label(root, bg="#FFFFFF", width=30, height=2)
        self.color_display.pack(pady=10)

        self.update_color()

    def update_color(self):
        x, y = pyautogui.position()

        screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
        color = screen.getpixel((0, 0))

        hex_color = "#{:02x}{:02x}{:02x}".format(color[0], color[1], color[2]).upper()
        rgba_color = f"RGBA({color[0]}, {color[1]}, {color[2]}, {color[3] if len(color) > 3 else 255})"

        self.hex_label.config(text=f"Hex: {hex_color}")
        self.rgba_label.config(text=f"RGBA: {rgba_color}")
        self.color_display.config(bg=hex_color)

        self.root.after(100, self.update_color)

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
