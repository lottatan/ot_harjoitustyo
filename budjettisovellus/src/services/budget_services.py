from entities.user import User
from entities.purchase import Purchase
from repositories.user_repository import user_repository as default_user_repository
from repositories.purchase_repository import purchase_repository as default_purchase_repository


class UsernameError(Exception):
    pass


class InvalidUsernameOrPasswordError(Exception):
    pass


class BudgetServices:
    """Luokka, joka vastaa sovelluksen käyttäjän tekemistä tehtävistä
    """

    def __init__(
            self,
            user_repository=default_user_repository,
            purchase_repository=default_purchase_repository):
        """Konstruktori, jonka attribuutteina on tietokannat ja käyttäjä
        """

        self._user = None
        self._user_repository = user_repository
        self._purchase_repository = purchase_repository

    def login(self, username, password):
        """Vastaa sisäänkirjautumisesta

        Args:
            username (str): käyttäjänimi
            password (str): salasana

        Raises:
            InvalidUsernameOrPasswordError: jos tietokannassa oleva käyttäjänimi+salasana yhdistelmä ei vastaa käyttäjän syöttämiä merkkijonoarvoja

        Returns:
            User: käyttäjä
        """
        user = self._user_repository.find_user(username)
        if not user or user.password != password:
            raise InvalidUsernameOrPasswordError(
                "Incorrect username or password")

        self._user = user

        return user

    def create_user(self, username, password):
        """Luo uuden käyttäjän

        Args:
            username (str): käyttäjänimi
            password (str): salasana

        Raises:
            UsernameError: Käyttäjänimi on jo käytössä

        Returns:
            User: käyttäjä
        """
        existing = self._user_repository.find_user(username)
        if existing:
            raise UsernameError("Username taken")

        starting_budget = 0
        user = self._user_repository.create_user(
            User(username, password, starting_budget))
        return user

    def get_current_user(self):
        """Palauttaa sisäänkirjautuneen käyttäjän

        Returns:
            User: käyttäjä
        """
        return self._user

    def delete_user(self, username):
        """Poistaa käyttäjän

        Args:
            username (str): käyttäjänimi
        """
        self._user_repository.delete_user(username)

    def add_purchase(self, purchase, price, category, username):
        """Luo uuden ostoksen

        Args:
            purchase (str): ostoksen tyyppi
            price (int): ostoksen hinta
            category (str): ostoksen kategoria
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi
        """
        self._purchase_repository.add_purchase(
            Purchase(purchase, price, category, username))

    def show_all_purchases(self):
        """Näyttää kaikki sisäänkirjautuneen käyttäjän ostokset
        """
        username = self.get_current_user().username
        self._purchase_repository.show_all_purchases(Purchase(username))

    def set_new_budget(self, budget, username):
        """Asettaa käyttäjälle uuden budjetin

        Args:
            budget (int): uuden budjetin koko
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi
        """
        self._user_repository.set_new_budget(budget, username)
        self._user.budget = budget

    def delete_all_purchases(self, username):
        """Poistaa käyttäjän kaikki ostokset

        Args:
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi
        """
        self._purchase_repository.delete_all_purchases(username)


budget_services = BudgetServices()
