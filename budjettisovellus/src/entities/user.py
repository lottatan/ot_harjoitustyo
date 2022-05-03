class User:
    """Luokka, joka kuvaa käyttäjää

    Attributes:
        username = käytättäjänimi
        password = salasana
        budget = budjetti
    """

    def __init__(self, username: str, password: str, budget: int):
        """Konstruktori, joka luo käyttäjän

        Args:
            username (str): merkkijono, kuvaa käyttäjänimeä
            password (str): merkkijono, kuvaa salasanaa
            budget (int): luku, joka kuvaa käyttäjän budjettia (luomisvaiheessa 0, voi muuttaa myöhemmin)
        """
        self.username = username
        self.password = password
        self.budget = budget
