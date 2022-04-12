from tkinter import Tk
from ui.budget_window import BudgetView
from ui.login import LogIn
from ui.create_new_user import CreateNew
from ui.ui import Ui


def main():
    window = Tk()
    window.title("BudgetApp")

    ui_view = Ui(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
