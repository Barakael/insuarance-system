import tkinter as tk
from tkinter import messagebox
from services.user_service import UserService
from gui.main_window import MainWindow


class LoginWindow:
    def __init__(self, root=None):
        self.root = root if root else tk.Tk()
        self.root.title("Insurance System - Login")
        self.root.geometry("350x250")

        # Username Label
        tk.Label(self.root, text="Username").pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        # Password Label
        tk.Label(self.root, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(self.root, text="Login", command=self.login).pack(pady=15)

        if not root:
            self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        service = UserService()
        user = service.authenticate_user(username, password)
        service.close_session()

        if user:
            self.root.destroy()
            new_root = tk.Tk()
            MainWindow(new_root, user)
            new_root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid Credentials")