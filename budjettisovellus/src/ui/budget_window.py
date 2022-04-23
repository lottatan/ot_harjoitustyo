from tkinter import ttk, constants, StringVar, Listbox, Scrollbar
from services.budget_services import budget_services
from repositories.purchase_repository import purchase_repository


class BudgetView():
    def __init__(self, root, handle_logout, purchases_view):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_purchases_view = purchases_view

        self.budget_view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def budget_view(self):
        self._frame = ttk.Frame(master=self._root)

        self._window_label = ttk.Label(
            master=self._frame, text="Your budget information")
        self._window_label.grid(row=0, column=0, padx=5, pady=5)

        logout_button = ttk.Button(
            master=self._frame, text="Log out", command=self._handle_logout)
        logout_button.grid(row=0, column=5, padx=5,
                           pady=5, sticky=constants.EW)

        delete_user_button = ttk.Button(master=self._frame, text="Delete user", command= self.delete_process)
        delete_user_button.grid(row=1, column=5, padx=5,
                                pady=5, sticky=constants.EW)

        self._budget_label = ttk.Label(
            master=self._frame, text="Your budget: ")
        self._budget_label.grid(row=3, column=0, padx=5,
                                pady=5, sticky=constants.EW)

        self._spent_label = ttk.Label(
            master=self._frame, text="Amount spent: ")
        self._spent_label.grid(row=4, column=0, padx=5,
                               pady=5, sticky=constants.EW)

        self._remaining_label = ttk.Label(
            master=self._frame, text="Remaining amount: ")
        self._remaining_label.grid(
            row=5, column=0, padx=5, pady=5, sticky=constants.EW)

        self._editview_label = ttk.Label(
            master=self._frame, text="Edit and view purchases: ")
        self._editview_label.grid(
            row=7, column=0, padx=5, pady=5, sticky=constants.EW)

        editview_button = ttk.Button(
            master=self._frame, text="Edit and view", command=self._handle_purchases_view)
        editview_button.grid(row=7, column=1, padx=5,
                             pady=5, sticky=constants.EW)

    def delete_process(self):
        user = budget_services.get_current_user()
        budget_services.delete_user(user.username)
        
        self._handle_logout()


class PurchasesView():
    def __init__(self, root, go_back):
        self._root = root
        self._frame = None
        self._handle_return = go_back
        self._categories = ("Appointments", "Bills", "Eating / drinking out", "Groceries", "Leisure", "Necessities", "Shopping", "Subscriptions", "Other")
        self._purchase_entry = None
        self._price_entry = None
        self._variable = None
        self._error_variable = None
        self._error_label = None
        self._username = budget_services.get_current_user().username

        self.purchases_view()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def purchases_view(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(master=self._frame)
        self._error_label = ttk.Label(
            master=self._frame, textvariable=self._error_variable)
        self._error_label.grid(padx=5, pady=5)

        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._handle_return)
        back_button.grid(row=0, column=0, padx=5, pady=5)

        self._add_purchase_label = ttk.Label(
            master=self._frame, text="Add purchase:")
        self._add_purchase_label.grid(row=2, column=0, padx=5, pady=5)

        self._choose_category_label = ttk.Label(
            master=self._frame, text= "Choose category:")
        self._choose_category_label.grid(row=3, column=0)

        self._variable = StringVar(self._frame)
        self._variable.set(self._categories[0])
        
        self._category_entry = ttk.OptionMenu(self._frame, self._variable, self._categories[0], *self._categories)

        self._category_entry.grid(row= 3, column= 1, sticky=constants.W, padx= 5)

        self._purchase_label = ttk.Label(
            master= self._frame, text= "Purchase:")
        self._purchase_label.grid(row= 4, column= 0, padx= 5, pady=5)

        self._purchase_entry = ttk.Entry(master=self._frame)
        self._purchase_entry.grid(
            row=4, column= 1, columnspan= 1, padx=5, sticky= constants.W)

        self._add_price_label = ttk.Label(
            master=self._frame, text="Price:")
        self._add_price_label.grid(row=5, column=0, padx=5, pady=5)

        self._price_entry = ttk.Entry(master=self._frame)
        self._price_entry.grid(
            row=5, column= 1, columnspan=1, padx=5, sticky= constants.W)

        add_purchase_button = ttk.Button(master=self._frame, text="Add", command= self._add_process)
        add_purchase_button.grid(
            row=6, column= 1, columnspan=1, padx= 5, sticky= constants.W)

        self._your_purchases_label = ttk.Label(
            master=self._frame, text= "Your purchases")
        self._your_purchases_label.grid(row=7, column=0, padx=5, pady=5)

        purchases_list = Listbox(master= self._frame)
        purchases_list.grid(row= 8, column= 0, padx= 5, pady= 5, sticky= constants.EW)

        purchases_scrollbar = Scrollbar(master= self._frame)
        purchases_scrollbar.grid(row= 8, column= 1, padx= 5, pady= 5, sticky= (constants.NS, constants.W))


        for i in range(1, 101):
            purchases_list.insert("end", i)

        purchases_list.config(yscrollcommand= purchases_scrollbar.set)
        purchases_scrollbar.config(command= purchases_list.yview)

        delete_purchases_button = ttk.Button(master=self._frame, text="Delete purchases")
        delete_purchases_button.grid(
            row=9, column=0, padx=5, pady=5, sticky=constants.EW)

        
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        self._hide_error()

    def _select_category(self, category):
        category = self._variable.get()
        return category

    def _add_process(self):
        category = self._select_category(category=None)
        purchase = self._purchase_entry.get()
        price = self._price_entry.get()

        if len(purchase) == 0:
            self._show_error("Enter purchase!")
            return
        if len(price) == 0:
            self._show_error("Enter price!")
            return

        budget_services.add_purchase(purchase, price, category, self._username)

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=7, column=0, padx=5, pady=5)

    def _hide_error(self):
        self._error_label.grid_remove()