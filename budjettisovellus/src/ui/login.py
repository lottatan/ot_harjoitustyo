from tkinter import ttk, constants, StringVar
from services.budget_services import budget_services, InvalidUsernameOrPasswordError


class LogIn():
    """Luokka, joka vastaa sisäänkirjautumisikkunasta
    """

    def __init__(self, root, handle_login, create_user):
        """Konstruktori, joka luo ikkunan

        Args:
            root (Tkinter-elementti): alusta ikkunalle
            handle_login (metodikutsu): hoitaa sisäänkirjautumisprosessin
            create_user (metodikutsu): hoitaa ikkunanvaihdoksen käyttäjänluonti-ikkunaan
        """
        self._root = root
        self._handle_create_user = create_user
        self._handle_login = handle_login
        self._frame = None
        self._username_entry = None
        self._username_entry = None
        self._error_variable = None
        self._error_label = None

        self._login()

    def pack(self):
        """Paketoi ikkunan
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Rikkoo ikkunan
        """
        self._frame.destroy()

    def _login(self):
        """Ikkuna luodaan tässä metodissa
        """
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(master=self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable)
        self._error_label.grid(padx=5, pady=5)

        login_label = ttk.Label(master=self._frame, text="Log in")
        login_label.grid(row=0, column=0, sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text="username:")
        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry = ttk.Entry(master=self._frame)
        self._username_entry.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text="password:")
        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._password_entry = ttk.Entry(master=self._frame)
        self._password_entry.grid(row=4, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        enter = ttk.Button(master=self._frame, text="Enter",
                           command=self._login_process)
        enter.grid(row=5, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_label = ttk.Label(master=self._frame, text="Create new user")
        create_label.grid(row=7, column=0, sticky=constants.W, padx=5, pady=5)

        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        create_user_button = ttk.Button(
            master=self._frame, text="Create", command=self._handle_create_user)
        create_user_button.grid(row=8, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._hide_error()

    def _login_process(self):
        """Hoitaa sisäänkirjautumisprosessin
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0:
            self._show_error("Enter username!")
            return

        if len(password) == 0:
            self._show_error("Enter password!")
            return

        try:
            budget_services.login(username, password)
            self._handle_login()

        except InvalidUsernameOrPasswordError:
            self._show_error("Incorrect username or password")

    def _show_error(self, message):
        """Näyttää virheilmoituksen

        Args:
            message (str): virheviesti
        """
        self._error_variable.set(message)
        self._error_label.grid(row=0, column=1, padx=5, pady=5)

    def _hide_error(self):
        """Piilottaa virheviestin
        """
        self._error_label.grid_remove()
