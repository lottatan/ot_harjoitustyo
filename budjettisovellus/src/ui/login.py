from tkinter import Tk, ttk, constants

class LogIn():
    def __init__(self, root):
        self._root = root

    def login(self):
        login_label = ttk.Label(master=self._root, text= "Login")

        username_label = ttk.Label(master=self._root, text= "username: ")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text= "password: ")
        password_entry = ttk.Entry(master=self._root)

        enter = ttk.Button(master=self._root, text= "Enter")

        create_label = ttk.Label(master=self._root, text= "Create new user")
        create_user = ttk.Button(master=self._root, text= "Create")


        login_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        enter.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        create_label.grid(columnspan= 2, sticky=constants.W, padx=5, pady=5)
        create_user.grid(columnspan= 2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

window = Tk()
window.title = "Login"

ui = LogIn(window)