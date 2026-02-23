import tkinter as tk
from tkinter import ttk, messagebox
from services.user_service import UserService
from database.session import SessionLocal
from models.user import User
from .base_page import BasePage


class UsersPage(BasePage):

    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.frame = tk.Frame(parent, bg=self.WHITE)
        self.frame.pack(fill="both", expand=True)

        self.build_ui()
        self.load_users()

    def build_ui(self):
        title = tk.Label(
            self.frame,
            text="User Management",
            font=("Arial", 16, "bold"),
            bg=self.WHITE
        )
        title.pack(pady=10)

        # ===== TABLE =====
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Username", "Role"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Role", text="Role")

        self.tree.pack(pady=10, fill="x")

        # ===== ADD USER SECTION =====
        form_frame = tk.Frame(self.frame, bg=self.WHITE)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Username", bg=self.WHITE).grid(row=0, column=0)
        self.username_entry = tk.Entry(form_frame)
        self.username_entry.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Password", bg=self.WHITE).grid(row=0, column=2)
        self.password_entry = tk.Entry(form_frame)
        self.password_entry.grid(row=0, column=3, padx=5)

        tk.Label(form_frame, text="Role", bg=self.WHITE).grid(row=0, column=4)
        self.role_combo = ttk.Combobox(form_frame, values=["admin", "staff"])
        self.role_combo.grid(row=0, column=5, padx=5)

        add_btn = tk.Button(
            self.frame,
            text="Add User",
            bg=self.SAGE,
            fg=self.NAVY,
            command=self.add_user
        )
        add_btn.pack(pady=5)

    def load_users(self):
        session = SessionLocal()
        users = session.query(User).all()
        session.close()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for user in users:
            self.tree.insert("", "end", values=(user.id, user.username, user.role))

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_combo.get()

        if not username or not password or not role:
            messagebox.showerror("Error", "All fields are required")
            return

        service = UserService()
        service.create_user(username, password, role)
        service.close_session()
        messagebox.showinfo("Success", "User added successfully")

        self.load_users()

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.role_combo.set("")