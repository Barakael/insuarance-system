from tkinter import ttk
import tkinter as tk
from .base_page import BasePage

class PoliciesPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True)
        self.build_layout()

    def build_layout(self):
        toolbar = tk.Frame(self.frame, bg="#ffffff", pady=20)
        toolbar.pack(fill="x", padx=30)

        tk.Label(toolbar, text="Insurance Policies", font=("Helvetica", 18, "bold"), 
                 bg="#ffffff", fg="#1a237e").pack(side="left")

        # Table for Policies
        style = ttk.Style()
        style.configure("Treeview", rowheight=35)
        
        columns = ("Policy ID", "Holder", "Type", "Status", "Premium")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=30, pady=10)
        
        # Mock Data Entry
        self.tree.insert("", "end", values=("POL-9901", "John Doe", "Auto", "Active", "$120/mo"))
        self.tree.insert("", "end", values=("POL-8821", "Jane Smith", "Life", "Pending", "$300/mo"))