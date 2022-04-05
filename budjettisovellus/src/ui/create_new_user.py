from tkinter import Tk, ttk, constants

class CreateNew():
    def __init__(self, root):
        self._root = root

    def create(self):
        create_label = ttk.Label(master=self._root, text= "Create new user")

        username_label = ttk.Label(master=self._root, text= "Enter new username: ")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text= "Enter password: ")
        password_entry = ttk.Entry(master=self._root)

        create = ttk.Button(master=self._root, text= "Create user")

        create_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

window = Tk()
window.title = "Create new user"

ui = CreateNew(window)