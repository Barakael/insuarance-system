import tkinter as tk
from tkinter import ttk, messagebox
from services.user_service import UserService
from database.session import SessionLocal
from models.user import User
from .base_page import BasePage

class UsersPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.parent = parent 
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True)
        
        self.refresh_id = None 
        self.build_layout() # MUST be named this to satisfy BasePage
        self.start_auto_refresh()

    def build_layout(self):
        """Builds the table and the '+ Add User' button"""
        toolbar = tk.Frame(self.frame, bg="#ffffff", pady=20)
        toolbar.pack(fill="x", padx=30)

        tk.Label(
            toolbar, text="User Registry", 
            font=("Helvetica", 18, "bold"), 
            bg="#ffffff", fg="#1a237e"
        ).pack(side="left")

        # Live Indicator
        tk.Label(toolbar, text="● Live Syncing", fg="#9dc183", bg="#ffffff", font=("Helvetica", 9)).pack(side="left", padx=15)

        # Add Button
        add_btn = tk.Button(
            toolbar, text="+ Add New User", 
            bg="#9dc183", fg="#1a237e",
            font=("Helvetica", 10, "bold"),
            relief="flat", padx=15, pady=8,
            command=self.open_add_user_popup,
            cursor="hand2"
        )
        add_btn.pack(side="right")

        # Table Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", foreground="black", background="white", rowheight=35, fieldbackground="white")
        style.configure("Treeview.Heading", background="#f8f9fa", foreground="#1a237e", font=('Helvetica', 10, 'bold'))

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Username", "Role"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Role", text="Role")
        
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

    def start_auto_refresh(self):
        """Updates data every 5 seconds"""
        self.load_users()
        # Use root window for the timer to ensure it persists correctly
        self.refresh_id = self.parent.after(5000, self.start_auto_refresh)

    def load_users(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        db = SessionLocal()
        try:
            users = db.query(User).all()
            for u in users:
                self.tree.insert("", "end", values=(u.id, u.username, u.role))
        finally:
            db.close()

    def open_add_user_popup(self):
        """Modal Popup with Focused UI"""
        self.popup = tk.Toplevel(self.frame)
        self.popup.title("New User")
        self.popup.geometry("400x450")
        self.popup.configure(bg="white")
        self.popup.transient(self.frame)
        self.popup.grab_set() # Lock background

        tk.Label(self.popup, text="Create Account", font=("Helvetica", 14, "bold"), bg="white", fg="#1a237e").pack(pady=20)

        # Inputs
        tk.Label(self.popup, text="Username", bg="white", fg="#1a237e").pack(anchor="w", padx=50)
        self.u_entry = tk.Entry(self.popup, bg="#f4f6f9", relief="flat", font=("Helvetica", 12))
        self.u_entry.pack(pady=5, padx=50, fill="x")

        tk.Label(self.popup, text="Password", bg="white", fg="#1a237e").pack(anchor="w", padx=50, pady=(10,0))
        self.p_entry = tk.Entry(self.popup, bg="#f4f6f9", relief="flat", font=("Helvetica", 12), show="*")
        self.p_entry.pack(pady=5, padx=50, fill="x")

        tk.Label(self.popup, text="Role", bg="white", fg="#1a237e").pack(anchor="w", padx=50, pady=(10,0))
        self.r_combo = ttk.Combobox(self.popup, values=["admin", "staff"], state="readonly")
        self.r_combo.pack(pady=5, padx=50, fill="x")

        tk.Button(
            self.popup, text="CREATE USER", bg="#9dc183", fg="#1a237e",
            font=("Helvetica", 10, "bold"), command=self.submit_user, relief="flat", pady=12
        ).pack(pady=30, padx=50, fill="x")

    def submit_user(self):
        u = self.u_entry.get()
        p = self.p_entry.get()
        r = self.r_combo.get()
        if u and p and r:
            service = UserService()
            service.create_user(u, p, r)
            self.popup.destroy()
            self.load_users()