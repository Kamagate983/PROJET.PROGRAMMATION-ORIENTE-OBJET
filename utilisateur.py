from compte import CompteBancaire


class CompteUtilisateur(CompteBancaire):
    def __init__(self, numero, proprietaire, solde=0.0):
        super().__init__(numero, solde)
        self.proprietaire = proprietaire
        with open("users.txt", "a") as f:
            f.write(f"Utilisateur: {self.proprietaire}, Compte: {self.get_numero()}\n")

    def afficher_infos(self):
        return f"Compte: {self.get_numero()} - Propriétaire: {self.proprietaire} - Solde: {self.get_solde()} €"
