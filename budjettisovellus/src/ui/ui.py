from ui.login import LogIn
from ui.create_new_user import CreateNew
from ui.budget_window import BudgetView

class Ui:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login()

    def _show_login(self):
        self._hide_current_view()

        self._current_view = LogIn(self._root, self._budget_window, self._create_window)
        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _create_window(self):
        self._hide_current_view()

        self._current_view = CreateNew(self._root, self._show_login)
        self._current_view.pack()

    def _budget_window(self):
        self._hide_current_view()
        
        self._current_view = BudgetView(self._root)