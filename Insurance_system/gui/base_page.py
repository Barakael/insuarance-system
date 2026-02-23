from abc import ABC, abstractmethod
import tkinter as tk

class BasePage(ABC):
    SAGE = "#9CAF88"
    NAVY = "#001F3F"
    WHITE = "#FFFFFF"

    def __init__(self, root, user):
        self.root = root
        self.user = user

    @abstractmethod
    def build_layout(self):
        pass