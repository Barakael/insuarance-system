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
        self.user_service = UserService() # Encapsulated service
        
        # Color Palette
        self.NAVY = "#1a237e"
        self.SAGE = "#9dc183"
        self.BG_LIGHT = "#ffffff"
        self.INPUT_BG = "#f4f6f9"
        
        self.frame = tk.Frame(parent, bg=self.BG_LIGHT)
        self.frame.pack(fill="both", expand=True)
        
        self.build_layout()
        self.start_auto_refresh()

    def build_layout(self):
        """Implements the abstract method from BasePage"""
        # --- Toolbar ---
        toolbar = tk.Frame(self.frame, bg=self.BG_LIGHT, pady=20)
        toolbar.pack(fill="x", padx=30)

        tk.Label(
            toolbar, text="User Registry", 
            font=("Helvetica", 18, "bold"), 
            bg=self.BG_LIGHT, fg=self.NAVY
        ).pack(side="left")

        # Action Buttons Container
        btn_frame = tk.Frame(toolbar, bg=self.BG_LIGHT)
        btn_frame.pack(side="right")

        tk.Button(
            btn_frame, text="+ Add New User", 
            bg=self.SAGE, fg=self.NAVY,
            font=("Helvetica", 10, "bold"),
            relief="flat", padx=15, pady=8,
            command=self.open_add_user_popup,
            cursor="hand2"
        ).pack(side="right")

        # --- Table Styling ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        foreground="black", 
                        background="white", 
                        rowheight=35, 
                        fieldbackground="white")
        style.configure("Treeview.Heading", 
                        background="#f8f9fa", 
                        foreground=self.NAVY, 
                        font=('Helvetica', 10, 'bold'))

        # --- Table Implementation ---
        columns = ("ID", "Username", "Role")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

    def load_users(self):
        """Fetches fresh data from DB"""
        # Check if widget still exists to prevent TclError
        if not self.tree.winfo_exists():
            return

        for row in self.tree.get_children():
            self.tree.delete(row)
            
        db = SessionLocal()
        try:
            users = db.query(User).all()
            for u in users:
                self.tree.insert("", "end", values=(u.id, u.username, u.role))
        finally:
            db.close()

    def start_auto_refresh(self):
        """Background loop for live syncing"""
        if self.frame.winfo_exists():
            self.load_users()
            # Save the after_id so we could cancel it if needed
            self.frame.after(5000, self.start_auto_refresh)

    def open_add_user_popup(self):
        """Modal Popup with fixed text visibility for macOS"""
        popup = tk.Toplevel(self.frame)
        popup.title("New User Account")
        popup.geometry("400x480")
        popup.configure(bg="white")
        popup.transient(self.frame) # Keeps popup on top of main window
        popup.grab_set()           # Prevents interaction with main window

        tk.Label(
            popup, text="Create Account", 
            font=("Helvetica", 14, "bold"), 
            bg="white", fg=self.NAVY
        ).pack(pady=20)

        # Reusable helper for visible inputs
        def create_input(label_text, is_password=False):
            tk.Label(popup, text=label_text, bg="white", fg="black", 
                     font=("Helvetica", 10, "bold")).pack(anchor="w", padx=50)
            
            entry = tk.Entry(
                popup, 
                bg=self.INPUT_BG, 
                fg="black",               # Force black text
                insertbackground="black",  # Force black cursor
                relief="flat", 
                font=("Helvetica", 12),
                show="*" if is_password else ""
            )
            entry.pack(pady=(5, 15), padx=50, fill="x", ipady=5)
            return entry

        u_entry = create_input("Username")
        p_entry = create_input("Password", is_password=True)

        tk.Label(popup, text="Role Selection", bg="white", fg="black", 
                 font=("Helvetica", 10, "bold")).pack(anchor="w", padx=50)
        
        r_combo = ttk.Combobox(popup, values=["admin", "staff"], state="readonly")
        r_combo.pack(pady=5, padx=50, fill="x")
        r_combo.set("staff")

        def handle_submit():
            username = u_entry.get().strip()
            password = p_entry.get().strip()
            role = r_combo.get()

            if not username or not password:
                messagebox.showwarning("Input Error", "Please fill in all fields.")
                return

            if self.user_service.create_user(username, password, role):
                popup.destroy()
                self.load_users()
                messagebox.showinfo("Success", f"User '{username}' created.")
            else:
                messagebox.showerror("Error", "Username already exists or database error.")

        tk.Button(
            popup, text="CREATE USER", 
            bg=self.SAGE, fg=self.NAVY,
            font=("Helvetica", 10, "bold"), 
            command=handle_submit, 
            relief="flat", pady=12,
            cursor="hand2"
        ).pack(pady=30, padx=50, fill="x")