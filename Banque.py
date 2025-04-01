class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []  # Liste pour stocker les comptes bancaires

    def ajouter_compte(self, compte):
        self.comptes.append(compte)  # Ajoute un compte à la liste des comptes

    def afficher_comptes(self):
        # Affiche les informations de tous les comptes dans la banque
        for compte in self.comptes:
            print(compte.afficher_infos())  # Utilise print pour afficher les infos

