from tkinter import ttk, constants, StringVar
from services.budget_services import BudgetServices, UsernameError

class CreateNew():
    def __init__(self, root, login):
        self._root = root
        self._frame = None
        self._login = login
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._create()

    def pack(self):
        self._frame.pack(fill= constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create(self):
        self._frame = ttk.Frame(master= self._root)

        self._error_variable = StringVar(master= self._frame)
        self._error_label = ttk.Label(master= self._frame, textvariable= self._error_variable)
        self._error_label.grid(padx= 5, pady= 5)

        back = ttk.Button(master= self._frame, text= "Back", command= self._login)
        back.grid(row = 0, columnspan= 1, sticky=(constants.E, constants.W), padx= 5, pady= 5)

        create_label = ttk.Label(master=self._frame, text= "Create new user")
        create_label.grid(row= 1, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text= "Enter new username: ")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row= 2, column= 0, padx=5, pady=5)
        self._username_entry.grid(row= 2, column= 1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text= "Enter password: ")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row= 3, column= 0, padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create = ttk.Button(master=self._frame, text= "Create user", command= self._create_process)
        create.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()

    def _create_process(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        
        try:
            BudgetServices.create_user(username, password)
            self._login()
        except UsernameError:
            self._show_error("Incorrect username or password")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()