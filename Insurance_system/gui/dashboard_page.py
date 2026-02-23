import tkinter as tk
from .base_page import BasePage
from services.dashboard_service import DashboardService

class DashboardPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.service = DashboardService()
        self.NAVY = "#1a237e"
        
        self.frame = tk.Frame(parent, bg="#f4f6f9")
        self.frame.pack(fill="both", expand=True)
        
        # This triggers the abstract method implementation
        self.build_layout() 
        self.refresh_data()

    def build_layout(self):  # CHANGED FROM setup_ui
        # Header
        header = tk.Frame(self.frame, bg="#f4f6f9", pady=20)
        header.pack(fill="x", padx=30)
        tk.Label(header, text=f"System Overview", 
                 font=("Helvetica", 18, "bold"), bg="#f4f6f9", fg=self.NAVY).pack(side="left")

        # Stats Container
        self.stats_frame = tk.Frame(self.frame, bg="#f4f6f9")
        self.stats_frame.pack(fill="x", padx=30, pady=20)

        # Create Stat Cards
        self.policy_card = self.create_stat_card("Total Policies", "0", 0)
        self.claim_card = self.create_stat_card("Active Claims", "0", 1)
        self.revenue_card = self.create_stat_card("Total Revenue", "$0.00", 2)
        self.payout_card = self.create_stat_card("Total Payouts", "$0.00", 3)

    def create_stat_card(self, title, value, col):
        card = tk.Frame(self.stats_frame, bg="white", padx=20, pady=20, 
                        highlightthickness=1, highlightbackground="#e0e0e0")
        card.grid(row=0, column=col, padx=10, sticky="nsew")
        self.stats_frame.columnconfigure(col, weight=1)

        tk.Label(card, text=title, font=("Helvetica", 10), bg="white", fg="#757575").pack()
        val_label = tk.Label(card, text=value, font=("Helvetica", 16, "bold"), bg="white", fg=self.NAVY)
        val_label.pack(pady=5)
        return val_label

    def refresh_data(self):
        try:
            data = self.service.get_stats()
            self.policy_card.config(text=data["policies"])
            self.claim_card.config(text=data["claims"])
            self.revenue_card.config(text=data["revenue"])
            self.payout_card.config(text=data["payouts"])
        except Exception as e:
            print(f"Dashboard refresh error: {e}")

        # Refresh every 30 seconds
        self.frame.after(30000, self.refresh_data)