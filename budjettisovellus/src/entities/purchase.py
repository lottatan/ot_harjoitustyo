#Tätä kautta voi luoda uuden ostoksen

# purchase_type on ostoksen tunniste, esim. "Kauppalasku" tai "Bussilippu"
# value on ostoksesta maksettu hinta

class Purchase:
    def __init__(self, purchase_type: str, value: float, user):
        self.purchase_type = purchase_type
        self.value = value
        self.user = user
        self.id = 0