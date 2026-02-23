class ClaimsPage(BasePage):
    def __init__(self, parent, user):
        super().__init__(parent, user)
        self.frame = tk.Frame(parent, bg="#ffffff")
        self.frame.pack(fill="both", expand=True)
        self.build_layout()

    def build_layout(self):
        header = tk.Frame(self.frame, bg="#ffffff", pady=20)
        header.pack(fill="x", padx=30)

        tk.Label(header, text="Claims Processing", font=("Helvetica", 18, "bold"), 
                 bg="#ffffff", fg="#1a237e").pack(side="left")

        # Stages Filter (Example of UI tracking stages)
        filter_frame = tk.Frame(self.frame, bg="#ffffff")
        filter_frame.pack(fill="x", padx=30, pady=10)
        
        stages = ["All", "Submitted", "Under Review", "Approved", "Rejected"]
        for stage in stages:
            tk.Button(filter_frame, text=stage, bg="#f0f0f0", relief="flat", padx=10).pack(side="left", padx=5)

        # Claims Table
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Policy", "Date", "Amount", "Stage"), show="headings")
        for col in ("ID", "Policy", "Date", "Amount", "Stage"):
            self.tree.heading(col, text=col)
        
        self.tree.pack(fill="both", expand=True, padx=30, pady=20)
        self.tree.insert("", "end", values=("CLM-001", "POL-9901", "2023-10-12", "$1,500", "Under Review"))