class CarteBancaire:
    def __init__(self, numero, titulaire, type_carte, date_expiration):
        self.numero = numero  # Numéro de la carte
        self.titulaire = titulaire  # Titulaire de la carte
        self.type_carte = type_carte  # Type de carte (ex: "Crédit", "Débit")
        self.date_expiration = date_expiration  # Date d'expiration de la carte

    def afficher_infos(self):
        return (f"Numéro de carte: {self.numero} - Titulaire: {self.titulaire} - "
                f"Type: {self.type_carte} - Expiration: {self.date_expiration}")


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


class CompteUtilisateur(CompteBancaire):
    def __init__(self, numero, proprietaire, solde=0.0):
        super().__init__(numero, solde)
        self.proprietaire = proprietaire

    def afficher_infos(self):
        infos = f"Compte: {self.get_numero()} - Propriétaire: {self.proprietaire} - Solde: {self.get_solde()} FCFA"
        if self.carte_bancaire:
            infos += f" - {self.carte_bancaire.afficher_infos()}"
        return infos


class CompteEntreprise(CompteBancaire):
    def __init__(self, numero, entreprise, solde=0.0):
        super().__init__(numero, solde)
        self.entreprise = entreprise

    def afficher_infos(self):
        infos = f"Compte: {self.get_numero()} - Entreprise: {self.entreprise} - Solde: {self.get_solde()} FCFA"
        if self.carte_bancaire:
            infos += f" - {self.carte_bancaire.afficher_infos()}"
        return infos


class Banque:
    def __init__(self, nom):
        self.nom = nom
        self.comptes = []  # Agrégation : une banque contient plusieurs comptes

    def ajouter_compte(self, compte):
        self.comptes.append(compte)

    def afficher_comptes(self):
        print(f"Banque: {self.nom} - Liste des comptes:")
        for compte in self.comptes:
            print(compte.afficher_infos())

    def enregistrer_comptes_dans_fichier(self, filename="carte.txt"):
        with open(filename, "w") as file:
            file.write(f"Banque: {self.nom}\n")
            file.write(f"Liste des comptes:\n")
            for compte in self.comptes:
                file.write(compte.afficher_infos() + "\n")


def entrer_informations_compte():
    print("Création d'un compte bancaire")

    # Entrée des informations de base du compte
    numero = input("Entrez le numéro du compte : ")
    proprietaire_ou_entreprise = input("Entrez le propriétaire du compte (ou l'entreprise) : ")

    # Demande du solde initial
    solde_input = input("Entrez le solde initial du compte : ")

    # Retirer les caractères non numériques, ici "FCFA"
    solde = float(solde_input.replace("FCFA", "").strip())  # Supprimer "FCFA" et les espaces

    # Choisir entre un compte utilisateur ou entreprise
    type_compte = input("Voulez-vous créer un compte pour un utilisateur ou une entreprise ? (u/e) : ").lower()

    # Créer le compte
    if type_compte == "u":
        compte = CompteUtilisateur(numero, proprietaire_ou_entreprise, solde)
    elif type_compte == "e":
        compte = CompteEntreprise(numero, proprietaire_ou_entreprise, solde)
    else:
        print("Type de compte invalide.")
        return None

    # Entrée des informations de carte bancaire
    associer_carte = input("Souhaitez-vous associer une carte bancaire à ce compte ? (o/n) : ").lower()
    if associer_carte == "o":
        numero_carte = input("Entrez le numéro de la carte : ")
        titulaire_carte = input("Entrez le titulaire de la carte : ")
        type_carte = input("Entrez le type de carte (Crédit/Débit) : ")
        date_expiration = input("Entrez la date d'expiration (MM/AA) : ")

        carte = CarteBancaire(numero_carte, titulaire_carte, type_carte, date_expiration)
        compte.associer_carte(carte)

    return compte


# Exemple d'utilisation
banque = Banque("Banque Centrale")

# Créer plusieurs comptes
nombre_de_comptes = int(input("Combien de comptes souhaitez-vous créer ? "))
for _ in range(nombre_de_comptes):
    compte = entrer_informations_compte()
    if compte:
        banque.ajouter_compte(compte)

# Afficher les comptes et informations des cartes bancaires
banque.afficher_comptes()

# Enregistrer les informations dans un fichier
banque.enregistrer_comptes_dans_fichier("carte.txt")
