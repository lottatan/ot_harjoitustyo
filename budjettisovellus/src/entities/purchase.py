class Purchase:
    """Luokka, joka kuvaa yhtä ostosta.

        Attribuutes:
            purchase = kuvaa ostoksen tyyppiä esim. kaupan nimeä tai tuotteen nimeä
            price = ostoksen hinta
            category = ostoksen kategoria
            username = sisäänkirjautuneen käyttäjän käyttäjänimi.
    """
    def __init__(self, purchase: str, price: int, category: str, username: str):
        """Konstruktori, joka luo uuden ostoksen.

        Args:
            ostos = str eli merkkijono
            hinta = int eli numero
            kategoria = str eli merkkijono
            sisäänkirjautuneen käyttäjän käyttäjänimi = str eli merkkijono.
        """
        self.purchase = purchase
        self.price = price
        self.category = category
        self.username = username
