import tkinter as tk
from tkinter import ttk, messagebox
from .base_page import BasePage
from services.claim_service import ClaimService

class ClaimsPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.service = ClaimService()
        self.NAVY = "#1a237e"
        self.SAGE = "#9dc183"
        
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True)
        
        self.build_layout()
        self.load_claims()

    def build_layout(self):
        # --- Toolbar ---
        toolbar = tk.Frame(self.frame, bg="#ffffff", pady=20)
        toolbar.pack(fill="x", padx=30)

        tk.Label(toolbar, text="Claims Workflow", font=("Helvetica", 18, "bold"), 
                 bg="#ffffff", fg=self.NAVY).pack(side="left")

        # Action Buttons
        btn_frame = tk.Frame(toolbar, bg="#ffffff")
        btn_frame.pack(side="right")

        tk.Button(btn_frame, text="+ File Claim", bg=self.SAGE, fg=self.NAVY, 
                  font=("Helvetica", 10, "bold"), relief="flat", padx=15, pady=8,
                  command=self.open_add_popup).pack(side="right", padx=5)
        
        tk.Button(btn_frame, text="Update Status", bg="#f0f0f0", fg=self.NAVY, 
                  font=("Helvetica", 10), relief="flat", padx=15, pady=8,
                  command=self.open_status_popup).pack(side="right", padx=5)

        # --- Table ---
        columns = ("ID", "Policy ID", "Amount", "Status", "Date")
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=30)

        # Bottom Actions
        bottom_bar = tk.Frame(self.frame, bg="#ffffff", pady=10)
        bottom_bar.pack(fill="x", padx=30)
        
        tk.Button(bottom_bar, text="🗑 Delete Selected", fg="#d32f2f", bg="#ffffff",
                  relief="flat", command=self.handle_delete).pack(side="left")

    def load_claims(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        claims = self.service.get_all_claims()
        for c in claims:
            # Format the date properly
            date_str = c.date_filed.strftime("%Y-%m-%d") if c.date_filed else "N/A"
            self.tree.insert("", "end", values=(c.id, c.policy_id, f"${c.amount}", c.status, date_str))

    def open_add_popup(self):
        popup = tk.Toplevel(self.frame)
        popup.title("File New Claim")
        popup.geometry("400x550")
        popup.configure(bg="white")
        popup.grab_set()

        # Header - Added fg=self.NAVY
        tk.Label(popup, text="Claim Information", font=("Helvetica", 14, "bold"), 
                 bg="white", fg=self.NAVY).pack(pady=20)

        # Policy ID Input - Added fg="black" to Label and Entry
        tk.Label(popup, text="Policy ID (e.g., 1)", bg="white", fg="black", font=("Helvetica", 10, "bold")).pack(anchor="w", padx=45)
        p_id_entry = tk.Entry(popup, bg="#f0f0f0", fg="black", insertbackground="black", relief="flat")
        p_id_entry.pack(fill="x", padx=45, pady=10, ipady=5)

        # Amount Input - Added fg="black" to Label and Entry
        tk.Label(popup, text="Claim Amount ($)", bg="white", fg="black", font=("Helvetica", 10, "bold")).pack(anchor="w", padx=45)
        amt_entry = tk.Entry(popup, bg="#f0f0f0", fg="black", insertbackground="black", relief="flat")
        amt_entry.pack(fill="x", padx=45, pady=10, ipady=5)

        # Description - Added fg="black" to Label and Text
        tk.Label(popup, text="Description of Incident", bg="white", fg="black", font=("Helvetica", 10, "bold")).pack(anchor="w", padx=45)
        desc_text = tk.Text(popup, bg="#f0f0f0", fg="black", insertbackground="black", height=4, relief="flat", font=("Helvetica", 11))
        desc_text.pack(fill="x", padx=45, pady=10)

        def submit():
            if self.service.create_claim(p_id_entry.get(), amt_entry.get(), desc_text.get("1.0", "end-1c")):
                popup.destroy()
                self.load_claims()
                messagebox.showinfo("Success", "Claim filed successfully.")
            else:
                messagebox.showerror("Error", "Could not file claim. Check Policy ID.")

        tk.Button(popup, text="SUBMIT CLAIM", bg=self.SAGE, fg=self.NAVY, font=("Helvetica", 10, "bold"),
                  command=submit, relief="flat", pady=10).pack(fill="x", padx=45, pady=20)

    def open_status_popup(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a claim first.")
            return
        
        claim_id = self.tree.item(selected[0])['values'][0]
        
        popup = tk.Toplevel(self.frame)
        popup.title("Update Status")
        popup.geometry("300x250")
        popup.configure(bg="white")
        popup.grab_set()

        # Added fg=self.NAVY
        tk.Label(popup, text="Transition Stage", font=("Helvetica", 12, "bold"), bg="white", fg=self.NAVY).pack(pady=20)
        
        stages = ["Submitted", "Under Review", "Approved", "Rejected", "Paid"]
        stage_cb = ttk.Combobox(popup, values=stages, state="readonly")
        stage_cb.pack(pady=10, padx=40, fill="x")

        def update():
            if self.service.update_status(claim_id, stage_cb.get()):
                popup.destroy()
                self.load_claims()
            else:
                messagebox.showerror("Error", "Update failed.")

        tk.Button(popup, text="UPDATE STATUS", bg=self.NAVY, fg="white", command=update, pady=10).pack(pady=20, padx=40, fill="x")

    def handle_delete(self):
        selected = self.tree.selection()
        if not selected: return
        
        claim_id = self.tree.item(selected[0])['values'][0]
        if messagebox.askyesno("Confirm", f"Delete Claim ID {claim_id}?"):
            if self.service.delete_claim(claim_id):
                self.load_claims()