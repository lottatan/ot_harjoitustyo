from tkinter import ttk, constants

class BudgetView():
    def __init__(self, root, handle_logout, purchases_list):
        self._root = root 
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_purchases_list_view = purchases_list

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

        delete_user_button = ttk.Button(master= self._frame, text= "Delete user")
        delete_user_button.grid(row= 1, column= 5, padx= 5, pady= 5, sticky= constants.EW)

        self._budget_label = ttk.Label(master= self._frame, text= "Your budget: ")
        self._budget_label.grid(row= 3, column= 0, padx= 5, pady= 5, sticky= constants.EW)

        self._spent_label = ttk.Label(master= self._frame, text= "Amount spent: ")
        self._spent_label.grid(row= 4, column= 0, padx= 5, pady= 5, sticky= constants.EW)

        self._remaining_label = ttk.Label(master= self._frame, text= "Remaining amount: ")
        self._remaining_label.grid(row= 5, column= 0, padx= 5, pady= 5, sticky= constants.EW)

        self._editview_label = ttk.Label(master= self._frame, text= "Edit and view purchases: ")
        self._editview_label.grid(row= 7, column= 0, padx= 5, pady= 5, sticky= constants.EW)

        editview_button = ttk.Button(master= self._frame, text= "Edit and view", command= self._handle_purchases_list_view)
        editview_button.grid(row= 7, column= 1, padx= 5, pady= 5, sticky= constants.EW)



class PurchasesView():
    def __init__(self, root, go_back):
        self._root = root
        self._frame = None
        self._handle_return = go_back

        self.purchases_view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def purchases_view(self):
        self._frame = ttk.Frame(master= self._root)

        back_button = ttk.Button(master= self._frame, text= "Back", command= self._handle_return)
        back_button.grid(row= 0, column= 0, padx= 5, pady= 5)

        self._add_purchase_label = ttk.Label(master=self._frame, text= "Add purchase: ")
        self._add_purchase_label.grid(row= 2, column= 0, padx= 5, pady= 5)

        self._add_price_label = ttk.Label(master= self._frame, text= "Add price: ")
        self._add_price_label.grid(row= 3, column= 0, padx= 5, pady= 5)

        self._add_purchase_entry = ttk.Entry(master= self._frame)
        self._add_purchase_entry.grid(row= 2, column= 1, padx= 5, pady= 5, sticky= constants.EW)

        self._add_price_entry = ttk.Entry(master= self._frame)
        self._add_price_entry.grid(row= 3, column= 1, padx= 5, pady= 5, sticky= constants.EW)

        add_purchase_button = ttk.Button(master= self._frame, text= "Add")
        add_purchase_button.grid(row= 3, column= 2, padx= 5, pady= 5, sticky= constants.EW)

        self._delete_purchase_label = ttk.Label(master=self._frame, text= "Delete purchase: ")
        self._delete_purchase_label.grid(row= 5, column= 0, padx= 5, pady= 5)

        self._delete_purchase_entry = ttk.Entry(master= self._frame)
        self._delete_purchase_entry.grid(row= 5, column= 1, padx= 5, pady= 5, sticky= constants.EW)

        delete_purchase_button = ttk.Button(master= self._frame, text= "Delete")
        delete_purchase_button.grid(row= 5, column= 2, padx= 5, pady= 5, sticky= constants.EW)