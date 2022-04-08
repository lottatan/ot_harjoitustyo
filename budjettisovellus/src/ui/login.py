from tkinter import Tk, ttk, constants

class LogIn():
    def __init__(self, root, create_user, budget_window):
        self._root = root
        self._handle_create_user = create_user
        self._handle_budget_window = budget_window
        self._frame = None
        self._username_entry = None
        self._username_entry = None

        self._login()

    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()

    def _login(self):
        self._frame = ttk.Frame(master= self._root)

        login_label = ttk.Label(master=self._root, text= "Login")
        login_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(master=self._root, text= "username: ")
        self._username_entry = ttk.Entry(master=self._root)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._root, text= "password: ")
        self._password_entry = ttk.Entry(master=self._root)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        enter = ttk.Button(master=self._root, text= "Enter")
        enter.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_label = ttk.Label(master=self._root, text= "Create new user")
        
        create_label.grid(columnspan= 2, sticky=constants.W, padx=5, pady=5)


        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        create_user_button = ttk.Button(master=self._root, text= "Create", command= self._handle_create_user)
        create_user_button.grid(columnspan= 2, sticky=(constants.E, constants.W), padx=5, pady=5)