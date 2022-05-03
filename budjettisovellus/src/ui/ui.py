from ui.login import LogIn
from ui.create_new_user import CreateNew
from ui.budget_window import BudgetView, PurchasesView


class Ui:
    """Luokka, joka vastaa sovelluksen käyttöliittymästä
    """

    def __init__(self, root):
        """Konstruktori, joka luo luokan

        Args:
            root (Tkinter elementti): alustaa käyttöliittymän
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Kutsuu sisäänkirjautumisikkunaa
        """
        self._login_window()

    def _login_window(self):
        """Näyttää sisäänkirjautumisikkunan
        """
        self._hide_current_view()

        self._current_view = LogIn(
            self._root, self._budget_window, self._create_window)
        self._current_view.pack()

    def _hide_current_view(self):
        """Rikkoo nykyisen ikkunan
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _create_window(self):
        """Näyttää käyttäjänluonti-ikkunan
        """
        self._hide_current_view()

        self._current_view = CreateNew(self._root, self._login_window)
        self._current_view.pack()

    def _budget_window(self):
        """Näyttää budjetti-infoikkunan
        """
        self._hide_current_view()

        self._current_view = BudgetView(
            self._root, self._login_window, self._purchases_view)
        self._current_view.pack()

    def _purchases_view(self):
        """Näyttää ostostietoikkunan
        """
        self._hide_current_view()

        self._current_view = PurchasesView(
            self._root, self._budget_window, self._handle_new_purchase)
        self._current_view.pack()

    def _handle_new_purchase(self):
        """Hoitaa reaaliaikaisen päivitysen ostosinfoikkunassa
        """
        self._purchases_view()
