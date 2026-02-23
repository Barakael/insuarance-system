import tkinter as tk
from .base_page import BasePage


class MainWindow(BasePage):
    def __init__(self, root, user):
        super().__init__(root, user)

        # === COLOR SYSTEM (Minimal & Clean) ===
        self.BG = "#f4f6f9"          # App background
        self.WHITE = "#ffffff"       # Cards / sidebar
        self.PRIMARY = "#2563eb"     # Accent blue
        self.TEXT_DARK = "#1f2937"   # Main text
        self.TEXT_LIGHT = "#6b7280"  # Secondary text
        self.BORDER = "#e5e7eb"      # Light border

        self.root.title("Insurance System")
        self.root.geometry("1200x800")
        self.root.configure(bg=self.BG)

        self.build_layout()

    # ================= LAYOUT =================
    def build_layout(self):

        # ===== SIDEBAR =====
        self.sidebar = tk.Frame(self.root, bg=self.WHITE, width=240)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Sidebar Title
        tk.Label(
            self.sidebar,
            text="Insurance",
            bg=self.WHITE,
            fg=self.PRIMARY,
            font=("Helvetica", 16, "bold")
        ).pack(pady=(30, 20))

        # User Info
        tk.Label(
            self.sidebar,
            text=self.user.username.upper(),
            bg=self.WHITE,
            fg=self.TEXT_DARK,
            font=("Helvetica", 11, "bold")
        ).pack(pady=(0, 30))

        # Navigation Menu
        menu_items = ["Dashboard", "Users", "Policies", "Claims", "Settings"]

        self.nav_buttons = {}

        for item in menu_items:
            if item == "Users" and self.user.role.lower() != "admin":
                continue
            self.create_nav_item(item)

        # ===== MAIN AREA =====
        self.main_container = tk.Frame(self.root, bg=self.BG)
        self.main_container.pack(side="right", expand=True, fill="both")

        # ===== TOP NAVBAR =====
        self.navbar = tk.Frame(self.main_container, bg=self.WHITE, height=60)
        self.navbar.pack(fill="x")
        self.navbar.pack_propagate(False)

        self.title_label = tk.Label(
            self.navbar,
            text="Dashboard",
            bg=self.WHITE,
            fg=self.TEXT_DARK,
            font=("Helvetica", 18, "bold")
        )
        self.title_label.pack(side="left", padx=30)

        # ===== CONTENT AREA =====
        self.content = tk.Frame(self.main_container, bg=self.BG)
        self.content.pack(expand=True, fill="both", padx=30, pady=30)

        self.content_card = tk.Frame(
            self.content,
            bg=self.WHITE,
            highlightbackground=self.BORDER,
            highlightthickness=1
        )
        self.content_card.pack(expand=True, fill="both")

        self.show_page("Dashboard")

    # ================= NAV ITEM =================
    def create_nav_item(self, text):

        btn = tk.Button(
            self.sidebar,
            text=text,
            bg=self.WHITE,
            fg=self.TEXT_LIGHT,
            font=("Helvetica", 11),
            relief="flat",
            anchor="w",
            padx=25,
            pady=12,
            borderwidth=0,
            cursor="hand2",
            command=lambda t=text: self.show_page(t)
        )

        btn.pack(fill="x")

        # Hover effect
        btn.bind("<Enter>", lambda e: btn.config(bg="#f3f4f6"))
        btn.bind("<Leave>", lambda e: self.reset_nav_colors())

        self.nav_buttons[text] = btn

    # ================= PAGE SWITCH =================
    def show_page(self, page_name):

        # Update title
        self.title_label.config(text=page_name)

        # Reset nav styles
        self.reset_nav_colors()

        # Highlight active
        active_btn = self.nav_buttons.get(page_name)
        if active_btn:
            active_btn.config(
                bg="#eff6ff",
                fg=self.PRIMARY
            )

        # Clear content
        for widget in self.content_card.winfo_children():
            widget.destroy()

        # Render pages
        if page_name == "Users":
            self.render_users_placeholder()
        else:
            tk.Label(
                self.content_card,
                text=f"{page_name} Module",
                font=("Helvetica", 14),
                bg=self.WHITE,
                fg=self.TEXT_DARK
            ).pack(expand=True)

    # ================= RESET NAV =================
    def reset_nav_colors(self):
        for btn in self.nav_buttons.values():
            btn.config(bg=self.WHITE, fg=self.TEXT_LIGHT)

    # ================= USERS TABLE MOCK =================
    def render_users_placeholder(self):

        header = tk.Frame(self.content_card, bg="#f9fafb", height=50)
        header.pack(fill="x")
        header.pack_propagate(False)

        columns = ["ID", "Username", "Role", "Status"]

        for col in columns:
            tk.Label(
                header,
                text=col,
                bg="#f9fafb",
                fg=self.TEXT_DARK,
                font=("Helvetica", 10, "bold"),
                width=15
            ).pack(side="left", padx=10)

        # Sample Row
        row = tk.Frame(self.content_card, bg=self.WHITE)
        row.pack(fill="x", pady=5)

        sample_data = ["1", "admin", "Admin", "Active"]

        for data in sample_data:
            tk.Label(
                row,
                text=data,
                bg=self.WHITE,
                fg=self.TEXT_LIGHT,
                font=("Helvetica", 10),
                width=15
            ).pack(side="left", padx=10)