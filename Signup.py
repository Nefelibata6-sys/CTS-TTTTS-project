from Login import Login_win
import tkinter as tk
from tkinter import ttk


THEME_BG = "#2b2b2b"
THEME_FG = "#e8e8e8"
THEME_ACCENT = "#4a9eff"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#3c3c3c"
THEME_FONT = ("Verdana", 10)


def apply_theme(root):
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



class Signup_win:
    def __init__(self, master):
        root = tk.Toplevel(master)
        self.root = root
        root.title("Login")
        root.geometry("900x500")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 1000) // 2}"
            f"+{(root.winfo_screenheight() - 500) // 2}"
        )
        apply_theme(root)

        self.Welcome_Text = tk.Label(root, text="Welcome to TTTTTS (Trinidad and Tobago Taxi, Transit and Transport Service).", font=("Helvetica", 14))
        self.Welcome_Text.place(x=0, y=20, width=870, height=60)

        self.CreateAccPass = tk.Entry(root, show="*")
        self.CreateAccPass.place(x=45, y=380, width=230, height=30)

        self.Login_text = tk.Label(root, text="Please Create an account.", font=("Helvetica", 14))
        self.Login_text.place(x=280, y=100, width=340, height=30)

        self.CreateAccEmail = tk.Entry(root)
        self.CreateAccEmail.place(x=45, y=170, width=300, height=30)

        self.C_Email_text = tk.Label(root, text="E-mail", font=("Helvetica", 13))
        self.C_Email_text.place(x=30, y=144, width=90, height=26)

        self.C_Password_text = tk.Label(root, text="Password", font=("Helvetica", 13))
        self.C_Password_text.place(x=40, y=354, width=90, height=26)

        self.Loginin_But = tk.Button(root, text="Login", command=self.on_Loginin_But, bg="#2e3033", font=("Helvetica", 12))
        self.Loginin_But.place(x=420, y=450, width=120, height=30)

        self.AccountV_text = tk.Label(root, text="Already have an account?", font=("Helvetica", 13))
        self.AccountV_text.place(x=180, y=450, width=230, height=30)

        self.Signin = tk.Button(root, text="Sign in", command=self.on_Signin, bg="#2e3033", font=("Helvetica", 12))
        self.Signin.place(x=50, y=420, width=120, height=30)

        self.C_Phone_Text = tk.Label(root, text="Phone Number", font=("Helvetica", 12))
        self.C_Phone_Text.place(x=40, y=280, width=140, height=30)

        self.C_Phone = tk.Entry(root)
        self.C_Phone.place(x=45, y=310, width=240, height=30)

        self.w_C_User_Text = tk.Label(root, text="User Name", font=("Helvetica", 12))
        self.w_C_User_Text.place(x=35, y=210, width=120, height=30)

        self.C_Username = tk.Entry(root)
        self.C_Username.place(x=45, y=240, width=240, height=30)

    def on_Loginin_But(self):

        self.root.withdraw()
        self.login_window = Login_win(self.root)


    def on_Signin(self):
        email = self.CreateAccEmail.get()
        username = self.C_Username.get()
        password = self.CreateAccPass.get()
        phone = self.C_Phone.get()
        print("hi")



if __name__ == "__main__":
    root = tk.Tk()
    root.mainloop()
