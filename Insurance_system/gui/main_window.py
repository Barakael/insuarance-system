import tkinter as tk
from .base_page import BasePage


class MainWindow(BasePage):

    def __init__(self, root, user):
        super().__init__(root, user)
        self.root.title("Insurance Policy Management System")
        self.root.geometry("900x600")
        self.build_layout()

    def build_layout(self):

        # ===== LEFT SIDEBAR =====
        self.sidebar = tk.Frame(self.root, bg=self.NAVY, width=200)
        self.sidebar.pack(side="left", fill="y")

        # ===== MAIN CONTENT =====
        self.content = tk.Frame(self.root, bg=self.WHITE)
        self.content.pack(side="right", expand=True, fill="both")

        # ===== USER INFO =====
        user_label = tk.Label(
            self.sidebar,
            text=f"Logged in as:\n{self.user.username}\n({self.user.role})",
            bg=self.NAVY,
            fg=self.WHITE,
            font=("Arial", 10, "bold")
        )
        user_label.pack(pady=20)

        # ===== MENU BUTTONS =====
        self.create_sidebar_button("Dashboard")
        if self.user.role.lower() == "admin":
           self.create_sidebar_button("Users")
        self.create_sidebar_button("Policies")
        self.create_sidebar_button("Claims")
        self.create_sidebar_button("Reports")

        tk.Button(
            self.sidebar,
            text="Logout",
            bg=self.SAGE,
            fg=self.NAVY,
            command=self.logout
        ).pack(side="bottom", pady=20)

    def create_sidebar_button(self, text):
        btn = tk.Button(
            self.sidebar,
            text=text,
            bg=self.SAGE,
            fg=self.WHITE,
            width=20,
            relief="flat",
            command=lambda: self.show_page(text)
        )
        btn.pack(pady=5)

    def logout(self):
        self.root.destroy()

        import tkinter as tk
        from gui.login_window import LoginWindow

        new_root = tk.Tk()
        LoginWindow(new_root)
        new_root.mainloop()
    
    
    def show_page(self, page_name):

    # Clear current content
     for widget in self.content.winfo_children():
        widget.destroy()

     if page_name == "Users":
        from gui.users_page import UsersPage
        UsersPage(self.content, self.user)

     else:
        label = tk.Label(
            self.content,
            text=f"{page_name} Page",
            font=("Arial", 18),
            bg=self.WHITE
        )
        label.pack(pady=50)