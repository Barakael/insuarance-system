import tkinter as tk
from .base_page import BasePage
# Note: UsersPage is imported inside show_page to prevent circular import issues

class MainWindow(BasePage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # === THEME SYSTEM (Navy & Sage) ===
        self.NAVY = "#1a237e"
        self.NAVY_HOVER = "#0d1442"  # Darker Navy for hover contrast
        self.SAGE = "#9dc183"        # Soft Green for accents
        self.WHITE = "#ffffff"
        self.LIGHT_GRAY = "#f8f9fa"
        self.TEXT_DARK = "#1f2937"
        
        self.root.title("Insurance Management System")
        self.root.geometry("1200x850")
        self.root.configure(bg=self.LIGHT_GRAY)

        self.nav_buttons = {}
        self.current_page_obj = None 
        
        self.build_layout()

    def build_layout(self):
        # ===== SIDEBAR (Solid Navy) =====
        self.sidebar = tk.Frame(self.root, bg=self.NAVY, width=260)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Branding
        tk.Label(
            self.sidebar, text="🛡️ SAFEGUARD", 
            bg=self.NAVY, fg=self.SAGE,
            font=("Helvetica", 18, "bold"), pady=40
        ).pack()

        # Navigation
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

        # Dynamic Content Card
        self.content_stage = tk.Frame(self.main_container, bg=self.LIGHT_GRAY)
        self.content_stage.pack(expand=True, fill="both", padx=40, pady=40)

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
        
        btn.bind("<Enter>", lambda e: btn.config(bg=self.NAVY_HOVER))
        btn.bind("<Leave>", lambda e: self.update_nav_selection(text))
        self.nav_buttons[text] = btn

    def update_nav_selection(self, current_page):
        for name, btn in self.nav_buttons.items():
            if name == current_page:
                btn.config(bg=self.SAGE, fg=self.NAVY)
            else:
                btn.config(bg=self.NAVY, fg=self.WHITE)

    def show_page(self, page_name):
        # 1. Stop any active auto-refresh timer from the current page
        if self.current_page_obj and hasattr(self.current_page_obj, 'refresh_id'):
            if self.current_page_obj.refresh_id:
                self.root.after_cancel(self.current_page_obj.refresh_id)

        self.title_label.config(text=page_name)
        self.update_nav_selection(page_name)

        # 2. Clear current content
        for widget in self.content_stage.winfo_children():
            widget.destroy()

        # 3. Routing Logic (The Switchboard)
        if page_name == "Dashboard":
            from .dashboard_page import DashboardPage
            self.current_page_obj = DashboardPage(self.content_stage, self.user)
            
        elif page_name == "Users":
            from .users_page import UsersPage
            self.current_page_obj = UsersPage(self.content_stage, self.user)
            
        elif page_name == "Policies":
            from .policies_page import PoliciesPage
            self.current_page_obj = PoliciesPage(self.content_stage, self.user)
            
        elif page_name == "Claims":
            from .claims_page import ClaimsPage
            self.current_page_obj = ClaimsPage(self.content_stage, self.user)
    def logout(self):
        self.root.destroy()