from Estore.CardType import CardType
class CreditCardInformation:
    def __init__(self,cvv, expiration_year_and_month, number, name, card_type:CardType):
        self.cvv = cvv
        self.expirationYearAndMonth = expiration_year_and_month
        self.number = number
        self.name = name
        self.type = card_type
