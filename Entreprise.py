from compte import CompteBancaire


class CompteEntreprise(CompteBancaire):
    def __init__(self, numero, entreprise, solde=0.0):
        super().__init__(numero, solde)
        self.entreprise = entreprise
        with open("users.txt", "a") as f:
            f.write(f"Entreprise: {self.entreprise}, Compte: {self.get_numero()}\n")

    def afficher_infos(self):
        return f"Compte: {self.get_numero()} - Entreprise: {self.entreprise} - Solde: {self.get_solde()} €"
