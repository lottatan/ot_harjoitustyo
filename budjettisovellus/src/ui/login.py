from tkinter import ttk, constants

class LogIn():
    def __init__(self, root, create_user):
        self._root = root
        self._handle_create_user = create_user
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

        login_label = ttk.Label(master=self._frame, text= "Log in")
        login_label.grid(row= 0, column= 0, sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(master=self._frame, text= "username:")
        self._username_entry = ttk.Entry(master=self._frame)
        username_label.grid(row= 1, column= 0, padx=5, pady=5)
        self._username_entry.grid(row= 2, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._frame, text= "password:")
        self._password_entry = ttk.Entry(master=self._frame)
        password_label.grid(row= 3, column= 0, padx=5, pady=5)
        self._password_entry.grid(row=4, column=0, sticky=(constants.E, constants.W), padx=5, pady=5)

        enter = ttk.Button(master=self._frame, text= "Enter")
        enter.grid(row= 5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_label = ttk.Label(master=self._frame, text= "Create new user")
        
        create_label.grid(row= 7, column= 0, sticky=constants.W, padx=5, pady=5)


        self._frame.grid_columnconfigure(0, weight=1, minsize=300)

        create_user_button = ttk.Button(master=self._frame, text= "Create", command= self._handle_create_user)
        create_user_button.grid(row= 8, columnspan= 2, sticky=(constants.E, constants.W), padx=5, pady=5)