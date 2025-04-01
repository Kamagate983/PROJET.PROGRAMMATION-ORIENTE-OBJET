class CompteBancaire:
    def __init__(self, numero, solde=0.0):
        self.__numero = numero
        self.__solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            with open("transactions.txt", "a") as f:
                f.write(f"Dépôt: {montant} sur {self.__numero}\n")
            return f"Dépôt de {montant} effectué. Nouveau solde: {self.__solde}"
        return "Montant invalide."

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            with open("transactions.txt", "a") as f:
                f.write(f"Retrait: {montant} sur {self.__numero}\n")
            return f"Retrait de {montant} effectué. Nouveau solde: {self.__solde}"
        return "Fonds insuffisants ou montant invalide."

    def get_solde(self):
        return self.__solde

    def get_numero(self):
        return self.__numero