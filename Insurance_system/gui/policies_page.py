import tkinter as tk
from tkinter import ttk, messagebox
from .base_page import BasePage
from services.policy_service import PolicyService # Ensure this exists

class PoliciesPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.NAVY = "#1a237e"
        self.SAGE = "#9dc183"
        self.service = PolicyService()
        
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True)
        
        self.build_layout()
        self.load_data() # Initial data load

    def build_layout(self):
        toolbar = tk.Frame(self.frame, bg="#ffffff", pady=20)
        toolbar.pack(fill="x", padx=30)

        tk.Label(toolbar, text="Policy Management", font=("Helvetica", 18, "bold"), 
                 bg="#ffffff", fg=self.NAVY).pack(side="left")

        # Refresh Button (Manual override)
        tk.Button(toolbar, text="🔄 Refresh", bg="white", command=self.load_data).pack(side="right", padx=10)

        tk.Button(toolbar, text="+ New Policy", bg=self.SAGE, fg=self.NAVY, 
                  font=("Helvetica", 10, "bold"), relief="flat", padx=15, pady=8,
                  command=self.open_policy_form).pack(side="right")

        # Table
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Holder", "Type", "Status", "Premium"), show="headings")
        for col in ("ID", "Holder", "Type", "Status", "Premium"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=30, pady=10)

    def load_data(self):
        """Clears and reloads data from the database"""
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Fetch from service
        policies = self.service.get_all_policies()
        for p in policies:
            self.tree.insert("", "end", values=(p.id, p.holder, p.type, p.status, f"${p.premium}"))

    def open_policy_form(self):
        self.popup = tk.Toplevel(self.frame)
        self.popup.title("Add Policy")
        self.popup.geometry("400x500")
        self.popup.configure(bg="white")
        
        # Prevent UI Freeze by handling window close
        self.popup.transient(self.frame)
        self.popup.grab_set()

        tk.Label(self.popup, text="New Policy", font=("Helvetica", 14, "bold"), bg="white", fg=self.NAVY).pack(pady=20)

        self.holder_entry = self.create_input(self.popup, "Holder Name")
        self.premium_entry = self.create_input(self.popup, "Premium ($)")

        tk.Label(self.popup, text="Policy Type", bg="white", fg=self.NAVY).pack(anchor="w", padx=45)
        self.type_cb = ttk.Combobox(self.popup, values=["Auto", "Life", "Health", "Home"], state="readonly")
        self.type_cb.pack(fill="x", padx=45, pady=10)

        tk.Button(self.popup, text="SAVE", bg=self.SAGE, fg=self.NAVY, font=("Helvetica", 10, "bold"),
                  command=self.handle_submit).pack(pady=20, padx=45, fill="x")

    def create_input(self, parent, label):
        tk.Label(parent, text=label, bg="white", fg=self.NAVY).pack(anchor="w", padx=45)
        e = tk.Entry(parent, bg="#f0f0f0", fg="black", insertbackground="black", relief="flat")
        e.pack(fill="x", padx=45, pady=10, ipady=5)
        return e

    def handle_submit(self):
        holder = self.holder_entry.get()
        p_type = self.type_cb.get()
        premium = self.premium_entry.get()

        if not holder or not p_type or not premium:
            messagebox.showerror("Error", "All fields are required")
            return

        # 1. Call Service to Save to DB
        success = self.service.create_policy(holder, p_type, premium)
        
        if success:
            # 2. Release the UI grab and close popup
            self.popup.grab_release()
            self.popup.destroy()
            # 3. Trigger reload
            self.load_data()
            messagebox.showinfo("Success", "Policy Added Successfully")
        else:
            messagebox.showerror("Error", "Database save failed")