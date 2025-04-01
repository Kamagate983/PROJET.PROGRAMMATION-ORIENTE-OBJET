class Morpion:
    def __init__(self):
        self.plateau = [[" " for _ in range(3)] for _ in range(3)]
        self.joueur_actuel = "X"

    def afficher_plateau(self):
        for ligne in self.plateau:
            print(" | ".join(ligne))
            print("-" * 9)

    def jouer(self, ligne, colonne):
        if self.plateau[ligne][colonne] == " ":
            self.plateau[ligne][colonne] = self.joueur_actuel
            if self.verifier_victoire():
                self.afficher_plateau()
                print(f"Le joueur {self.joueur_actuel} a gagné !")
                return True
            self.joueur_actuel = "O" if self.joueur_actuel == "X" else "X"
        else:
            print("Case déjà occupée, essayez encore !")
        return False

    def verifier_victoire(self):
        # Vérification des lignes et des colonnes
        for i in range(3):
            if all(self.plateau[i][j] == self.joueur_actuel for j in range(3)) or \
                    all(self.plateau[j][i] == self.joueur_actuel for j in range(3)):
                return True

        # Vérification des diagonales
        if all(self.plateau[i][i] == self.joueur_actuel for i in range(3)) or \
                all(self.plateau[i][2 - i] == self.joueur_actuel for i in range(3)):
            return True

        return False

    def jouer_partie(self):
        print("Bienvenue dans le jeu du Morpion !")
        self.afficher_plateau()
        for _ in range(9):
            try:
                ligne = int(input(f"Joueur {self.joueur_actuel}, entrez la ligne (0-2) : "))
                colonne = int(input(f"Joueur {self.joueur_actuel}, entrez la colonne (0-2) : "))
                if self.jouer(ligne, colonne):
                    break
            except (ValueError, IndexError):
                print("Entrée invalide, réessayez !")
        else:
            print("Match nul !")


# Lancer une partie
if __name__ == "__main__":
    jeu = Morpion()
    jeu.jouer_partie()
