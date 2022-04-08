from tkinter import ttk, constants

class CreateNew():
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._create()

    def pack(self):
        self._frame.pack(fill= constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create(self):
        create_label = ttk.Label(master=self._root, text= "Create new user")
        create_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label = ttk.Label(master=self._root, text= "Enter new username: ")
        self._username_entry = ttk.Entry(master=self._root)
        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=7, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self._root, text= "Enter password: ")
        self._password_entry = ttk.Entry(master=self._root)
        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=8, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        create = ttk.Button(master=self._root, text= "Create user")
        create.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)