from tkinter import ttk
from login import LogIn
from create_new_user import CreateNew

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def _start(self):
        self._show_login_py()

    def _create_window(self):
        self._current_view = LogIn()

    def _budget_window(self):
        self._current_view = CreateNew()