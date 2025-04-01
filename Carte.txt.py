class CompteBancaire:
    def __init__(self, numero, solde=0.0):
        self.__numero = numero  # Attribut privé
        self.__solde = solde  # Attribut privé
        self.carte_bancaire = None  # Aucune carte par défaut

    def associer_carte(self, carte_bancaire):
        self.carte_bancaire = carte_bancaire

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Dépot de {montant} effectué. Nouveau solde: {self.__solde}")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.__solde}")
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde

    def get_numero(self):
        return self.__numero
