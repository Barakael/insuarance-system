import tkinter as tk
from .base_page import BasePage  # Essential Import

class DashboardPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True)
        self.build_layout()

    def build_layout(self):
        # Header
        tk.Label(self.frame, text="System Overview", font=("Helvetica", 20, "bold"), 
                 bg="#ffffff", fg="#1a237e").pack(anchor="w", padx=40, pady=30)

        # Stats Grid
        stats_container = tk.Frame(self.frame, bg="#ffffff")
        stats_container.pack(fill="x", padx=40)

        self.create_stat_card(stats_container, "Active Policies", "1,284", "#1a237e", 0)
        self.create_stat_card(stats_container, "Pending Claims", "42", "#9dc183", 1)
        self.create_stat_card(stats_container, "Total Premiums", "$4.2M", "#1a237e", 2)

    def create_stat_card(self, parent, title, value, color, col):
        card = tk.Frame(parent, bg="#f8f9fa", highlightthickness=1, highlightbackground="#e5e7eb", padx=20, pady=20)
        card.grid(row=0, column=col, padx=10, sticky="nsew")
        parent.columnconfigure(col, weight=1)

        tk.Label(card, text=title, font=("Helvetica", 10), bg="#f8f9fa", fg="#6b7280").pack(anchor="w")
        tk.Label(card, text=value, font=("Helvetica", 18, "bold"), bg="#f8f9fa", fg=color).pack(anchor="w", pady=(5, 0))