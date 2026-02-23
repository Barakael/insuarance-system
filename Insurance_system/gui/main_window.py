import tkinter as tk
from .base_page import BasePage
from database.session import SessionLocal
from models.user import User

class MainWindow(BasePage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # === THEME SYSTEM ===
        self.NAVY = "#1a237e"
        self.NAVY_LIGHT = "#283593"
        self.SAGE = "#9dc183"
        self.WHITE = "#ffffff"
        self.LIGHT_GRAY = "#f8f9fa"
        self.TEXT_DARK = "#1f2937"
        
        self.root.title("Insurance Management System")
        self.root.geometry("1200x850")
        self.root.configure(bg=self.LIGHT_GRAY)

        # State management for auto-refresh
        self.refresh_id = None
        self.nav_buttons = {}
        
        self.build_layout()

    def build_layout(self):
        # ===== SIDEBAR =====
        self.sidebar = tk.Frame(self.root, bg=self.NAVY, width=260)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Branding
        tk.Label(
            self.sidebar, text="🛡️ SAFEGUARD", 
            bg=self.NAVY, fg=self.SAGE,
            font=("Helvetica", 18, "bold"), pady=40
        ).pack()

        # Navigation Menu Items
        menu_items = [
            ("Dashboard", "📊"),
            ("Users", "👥"),
            ("Policies", "📜"),
            ("Claims", "💰")
        ]

        for text, icon in menu_items:
            if text == "Users" and self.user.role.lower() != "admin":
                continue
            self.create_nav_item(text, icon)

        # ===== MAIN CONTENT AREA =====
        self.main_container = tk.Frame(self.root, bg=self.LIGHT_GRAY)
        self.main_container.pack(side="right", expand=True, fill="both")

        # Top Header
        self.header = tk.Frame(self.main_container, bg=self.WHITE, height=70)
        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        self.title_label = tk.Label(
            self.header, text="Dashboard", bg=self.WHITE, fg=self.NAVY,
            font=("Helvetica", 20, "bold")
        )
        self.title_label.pack(side="left", padx=40)

        # Logout Button
        tk.Button(
            self.header, text="Logout 🚪", bg=self.WHITE, fg="#d32f2f",
            font=("Helvetica", 10, "bold"), relief="flat", 
            command=self.logout, cursor="hand2"
        ).pack(side="right", padx=40)

        # The Stage where pages are rendered
        self.content_stage = tk.Frame(self.main_container, bg=self.LIGHT_GRAY)
        self.content_stage.pack(expand=True, fill="both", padx=40, pady=40)

        # Default start page
        self.show_page("Dashboard")

    def create_nav_item(self, text, icon):
        btn = tk.Button(
            self.sidebar, text=f"  {icon}  {text}",
            bg=self.NAVY, fg=self.WHITE, font=("Helvetica", 11),
            relief="flat", anchor="w", padx=30, pady=15,
            borderwidth=0, cursor="hand2",
            command=lambda t=text: self.show_page(t)
        )
        btn.pack(fill="x")
        
        btn.bind("<Enter>", lambda e: btn.config(bg=self.NAVY_LIGHT))
        btn.bind("<Leave>", lambda e: self.update_nav_selection(text))
        self.nav_buttons[text] = btn

    def update_nav_selection(self, current_page):
        for name, btn in self.nav_buttons.items():
            if name == current_page:
                btn.config(bg=self.SAGE, fg=self.NAVY)
            else:
                btn.config(bg=self.NAVY, fg=self.WHITE)

    def show_page(self, page_name):
        # 1. Kill any existing refresh loop to save resources
        if self.refresh_id:
            self.root.after_cancel(self.refresh_id)
            self.refresh_id = None

        self.title_label.config(text=page_name)
        self.update_nav_selection(page_name)

        # 2. Clear content stage
        for widget in self.content_stage.winfo_children():
            widget.destroy()

        # 3. Create the Page Card
        self.page_card = tk.Frame(
            self.content_stage, bg=self.WHITE,
            highlightthickness=1, highlightbackground="#e0e0e0"
        )
        self.page_card.pack(expand=True, fill="both")

        # 4. Route to specific page logic
        if page_name == "Users":
            self.setup_users_view()
        else:
            tk.Label(self.page_card, text=f"{page_name} coming soon...", 
                     bg=self.WHITE, font=("Helvetica", 12)).pack(expand=True)

    # ================= REFRESH LOGIC =================

    def setup_users_view(self):
        """Builds the table structure and starts the loop"""
        toolbar = tk.Frame(self.page_card, bg=self.WHITE, pady=20, padx=20)
        toolbar.pack(fill="x")

        tk.Label(toolbar, text="User Registry", font=("Helvetica", 14, "bold"),
                 bg=self.WHITE, fg=self.NAVY).pack(side="left")

        # Visual indicator that the page is 'Live'
        self.status_indicator = tk.Label(toolbar, text="● Syncing...", 
                                        fg=self.SAGE, bg=self.WHITE, font=("Helvetica", 9))
        self.status_indicator.pack(side="left", padx=20)

        # Frame where the actual data rows go
        self.table_body = tk.Frame(self.page_card, bg=self.WHITE)
        self.table_body.pack(fill="both", expand=True, padx=20)

        # Start the recursive refresh loop
        self.refresh_users_loop()

    def refresh_users_loop(self):
        """Polls DB and updates the UI every 5 seconds"""
        # Clear rows
        for widget in self.table_body.winfo_children():
            widget.destroy()

        # Re-build Header
        header = tk.Frame(self.table_body, bg=self.LIGHT_GRAY)
        header.pack(fill="x")
        for col in ["ID", "Username", "Role", "Status"]:
            tk.Label(header, text=col, font=("Helvetica", 10, "bold"), 
                     bg=self.LIGHT_GRAY, width=15).pack(side="left", pady=10)

        # Fetch Data
        db = SessionLocal()
        try:
            users = db.query(User).all()
            for user in users:
                row = tk.Frame(self.table_body, bg=self.WHITE)
                row.pack(fill="x", pady=2)
                tk.Label(row, text=user.id, bg=self.WHITE, width=15).pack(side="left")
                tk.Label(row, text=user.username, bg=self.WHITE, width=15).pack(side="left")
                tk.Label(row, text=user.role, bg=self.WHITE, width=15).pack(side="left")
                tk.Label(row, text="Active", fg="green", bg=self.WHITE, width=15).pack(side="left")
        finally:
            db.close()

        # Schedule next run in 5000ms (5 seconds)
        self.refresh_id = self.root.after(5000, self.refresh_users_loop)

    def logout(self):
        if self.refresh_id:
            self.root.after_cancel(self.refresh_id)
        self.root.destroy()
        # Trigger your login window here...