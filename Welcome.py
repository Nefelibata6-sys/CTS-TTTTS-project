
from Signup import Signup_win
import tkinter as tk
from tkinter import ttk


THEME_BG = "#2b2b2b"
THEME_FG = "#e8e8e8"
THEME_ACCENT = "#4a9eff"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT = ("Verdana", 10)


def apply_theme(root):
    """Apply the project theme as defaults; per-widget options override these."""
    root.configure(bg=THEME_BG)
    root.option_add("*background", THEME_BG)
    root.option_add("*foreground", THEME_FG)
    root.option_add("*font", THEME_FONT)
    root.option_add("*Entry.background", THEME_FIELD_BG)
    root.option_add("*Text.background", THEME_FIELD_BG)
    root.option_add("*Listbox.background", THEME_FIELD_BG)
    root.option_add("*Button.background", THEME_ACCENT)
    root.option_add("*Button.foreground", THEME_ACCENT_FG)
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
    style.configure(".", background=THEME_BG, foreground=THEME_FG, fieldbackground=THEME_FIELD_BG, font=THEME_FONT)


class TheAbyss:
    def __init__(self, root):
        self.root = root
        root.title("The Abyss")
        root.geometry("571x272")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 571) // 2}"
            f"+{(root.winfo_screenheight() - 272) // 2}"
        )
        apply_theme(root)

        self.label1 = tk.Label(root, text="Welcome to TTTTTS (Trinidad and Tobago Taxi, Transit and Transport Service).", font=("Helvetica", 15))
        self.label1.place(x=45, y=15, width=480, height=100)

        self.button2 = tk.Button(root, text="Begin?", command=self.open_login, bg="#2e3033", font=("Helvetica", 12))
        self.button2.place(x=225, y=130, width=120, height=30)

    def open_login(self):
        
        self.root.withdraw()
        self.Signup_window = Signup_win(self.root)
    



if __name__ == "__main__":
    root = tk.Tk()
    app = TheAbyss(root)
    root.mainloop()
