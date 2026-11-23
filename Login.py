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


class Login_win:
    def __init__(self, master):
        root = tk.Toplevel(master)
        self.root = root
        root.title("Login")
        root.geometry("700x380")
        apply_theme(root)

        self.Login_Text = tk.Label(root, text="Login", font=("Helvetica", 19))
        self.Login_Text.place(x=185, y=10, width=330, height=60)

        self.Log_pg_Button = tk.Button(root, text="Login", command=self.on_Log_pg_Button, bg="#2e3033", font=("Helvetica", 17))
        self.Log_pg_Button.place(x=260, y=230, width=140, height=40)

        self.Admin_Text = tk.Label(root, text="Admin? Click this", font=("Helvetica", 13))
        self.Admin_Text.place(x=100, y=330, width=240, height=30)

        self.Admin_Testing = tk.Button(root, text="Testing", command=self.on_Admin_Testing, bg="#2e3033", font=("Helvetica", 13))
        self.Admin_Testing.place(x=310, y=330, width=110, height=30)

        self.Log_Email = tk.Entry(root)
        self.Log_Email.place(x=185, y=106, width=330, height=30)

        self.Log_Pass = tk.Entry(root)
        self.Log_Pass.place(x=185, y=175, width=330, height=30)

        self.Log_Email_text = tk.Label(root, text="Email", font=("Helvetica", 14))
        self.Log_Email_text.place(x=160, y=70, width=120, height=30)

        self.Log_pass_text = tk.Label(root, text="Password", font=("Helvetica", 14))
        self.Log_pass_text.place(x=170, y=145, width=120, height=30)

    def on_Log_pg_Button(self):
        pass

    def on_Admin_Testing(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
