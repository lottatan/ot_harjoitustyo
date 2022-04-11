from tkinter import Tk, ttk, constants

class BudgetView():
    def __init__(self, root, handle_logout):
        self._root = root 
        self._frame = None
        self._handle_logout = handle_logout

        self.budget_view()
    
    def pack(self):
        self._frame.pack(fill= constants.X)

    def destroy(self):
        self._frame.destroy()

    def budget_view(self):
        self._frame = ttk.Frame(master= self._root)

        self._window_label = ttk.Label(master= self._frame, text= "Your budget information")
        self._window_label.grid(row= 0, column= 0, padx= 5, pady= 5)

        logout_button = ttk.Button(master= self._frame, text= "Log out", command= self._handle_logout)
        logout_button.grid(row= 0, column= 5, padx= 5, pady= 5, sticky= constants.EW)

        self._add_purchase_label = ttk.Label(master=self._frame, text= "Add purchase: ")
        self._add_price_label = ttk.Label(master= self._frame, text= "Add price: ")
        self._add_purchase_entry = ttk.Entry(master= self._frame)
        self._add_price_entry = ttk.Entry(master= self._frame)
        add_purchase_button = ttk.Button(master= self._frame, text= "Add")

        self._add_purchase_label.grid(row= 1, column= 0, padx= 5, pady= 5)
        self._add_purchase_entry.grid(row= 1, column= 1, padx= 5, pady= 5, sticky= constants.EW)
        self._add_price_label.grid(row= 2, column= 0, padx= 5, pady= 5)
        self._add_price_entry.grid(row= 2, column= 1, padx= 5, pady= 5, sticky= constants.EW)
        add_purchase_button.grid(row= 2, column= 2, padx= 5, pady= 5, sticky= constants.EW)

        self._delete_purchase_label = ttk.Label(master=self._frame, text= "Delete purchase: ")
        self._delete_purchase_entry = ttk.Entry(master= self._frame)
        delete_purchase_button = ttk.Button(master= self._frame, text= "Delete")

        self._delete_purchase_label.grid(row= 5, column= 0, padx= 5, pady= 5)
        self._delete_purchase_entry.grid(row= 5, column= 1, padx= 5, pady= 5, sticky= constants.EW)
        delete_purchase_button.grid(row= 5, column= 2, padx= 5, pady= 5, sticky= constants.EW)


class PurchasesList():
    def __init__(self, root, purchases):
        self._root = root
        self._purchases = purchases   