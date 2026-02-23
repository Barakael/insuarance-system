import tkinter as tk
from tkinter import ttk, messagebox
from services.user_service import UserService
from database.session import SessionLocal
from models.user import User
from .base_page import BasePage

class UsersPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        # Using the theme colors defined in MainWindow
        self.NAVY = "#1a237e"
        self.SAGE = "#9dc183"
        self.WHITE = "#ffffff"
        self.TEXT_DARK = "#1f2937"
        self.BORDER = "#e5e7eb"

        self.frame = tk.Frame(parent, bg=self.WHITE)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.build_ui()
        self.load_users()

    def build_ui(self):
        # Header Section
        header_frame = tk.Frame(self.frame, bg=self.WHITE)
        header_frame.pack(fill="x", pady=(0, 20))

        tk.Label(
            header_frame,
            text="User Management",
            font=("Helvetica", 18, "bold"),
            bg=self.WHITE,
            fg=self.NAVY  # Adoption of Navy for headers
        ).pack(side="left")

        # Modern "Add User" Button (Matches sidebar accent)
        add_btn = tk.Button(
            header_frame,
            text="+ Add New User",
            bg=self.SAGE,
            fg=self.NAVY,
            font=("Helvetica", 10, "bold"),
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.open_add_user_popup # Trigger the popup
        )
        add_btn.pack(side="right")

        # ===== STYLED TREEVIEW =====
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        background=self.WHITE, 
                        foreground=self.TEXT_DARK, 
                        rowheight=35, 
                        fieldbackground=self.WHITE,
                        bordercolor=self.BORDER,
                        borderwidth=1)
        style.configure("Treeview.Heading", 
                        background="#f8f9fa", 
                        foreground=self.NAVY, 
                        font=("Helvetica", 10, "bold"))
        style.map("Treeview", background=[('selected', self.SAGE)], foreground=[('selected', self.NAVY)])

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Username", "Role"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="USERNAME")
        self.tree.heading("Role", text="ROLE")
        
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Username", width=300, anchor="w")
        self.tree.column("Role", width=200, anchor="center")

        self.tree.pack(fill="both", expand=True)

    def load_users(self):
        session = SessionLocal()
        try:
            users = session.query(User).all()
            for row in self.tree.get_children():
                self.tree.delete(row)
            for user in users:
                self.tree.insert("", "end", values=(user.id, user.username, user.role))
        finally:
            session.close()

    # ================= POPUP SECTION =================
    def open_add_user_popup(self):
        # Create a new top-level window (The Popup)
        self.popup = tk.Toplevel(self.frame)
        self.popup.title("Create New User")
        self.popup.geometry("400x450")
        self.popup.configure(bg=self.WHITE)
        self.popup.resizable(False, False)
        
        # Make it modal (Locks the main window)
        self.popup.transient(self.frame)
        self.popup.grab_set()

        # Center the popup relative to the main window
        x = self.frame.winfo_rootx() + (self.frame.winfo_width() // 2) - 200
        y = self.frame.winfo_rooty() + (self.frame.winfo_height() // 2) - 225
        self.popup.geometry(f"+{x}+{y}")

        # UI inside Popup
        tk.Label(self.popup, text="Add New User", font=("Helvetica", 14, "bold"), 
                 bg=self.WHITE, fg=self.NAVY).pack(pady=20)

        # Username Field
        tk.Label(self.popup, text="Username", bg=self.WHITE, fg=self.NAVY, font=("Helvetica", 10)).pack(anchor="w", padx=50)
        self.new_username = tk.Entry(self.popup, font=("Helvetica", 12), bg="#f4f6f9", relief="flat")
        self.new_username.pack(fill="x", padx=50, pady=(5, 15))

        # Password Field
        tk.Label(self.popup, text="Password", bg=self.WHITE, fg=self.NAVY, font=("Helvetica", 10)).pack(anchor="w", padx=50)
        self.new_password = tk.Entry(self.popup, font=("Helvetica", 12), bg="#f4f6f9", relief="flat", show="*")
        self.new_password.pack(fill="x", padx=50, pady=(5, 15))

        # Role Field
        tk.Label(self.popup, text="Role", bg=self.WHITE, fg=self.NAVY, font=("Helvetica", 10)).pack(anchor="w", padx=50)
        self.new_role = ttk.Combobox(self.popup, values=["admin", "staff"], state="readonly")
        self.new_role.pack(fill="x", padx=50, pady=(5, 30))

        # Action Buttons
        save_btn = tk.Button(self.popup, text="Create User", bg=self.SAGE, fg=self.NAVY, 
                             font=("Helvetica", 11, "bold"), relief="flat", pady=10,
                             command=self.submit_new_user)
        save_btn.pack(fill="x", padx=50)

    def submit_new_user(self):
        username = self.new_username.get()
        password = self.new_password.get()
        role = self.new_role.get()

        if not username or not password or not role:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            service = UserService()
            # Ensure your UserService has a create_user method
            service.create_user(username, password, role)
            messagebox.showinfo("Success", f"User {username} created!")
            self.popup.destroy() # Close popup
            self.load_users()    # Refresh table
        except Exception as e:
            messagebox.showerror("Database Error", str(e))