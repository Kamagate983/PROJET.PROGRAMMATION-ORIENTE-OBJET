class Transaction:
    def __init__(self, transaction_id, client_id, montant, date, statut):
        self.transaction_id = transaction_id
        self.client_id = client_id
        self.montant = montant
        self.date = date
        self.statut = statut

    def __str__(self):
        return f"Transaction {self.transaction_id}: Client {self.client_id}, {self.montant} EUR, {self.date}, Statut: {self.statut}"


def charger_transactions(fichier):
    transactions = []
    with open(fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        for i in range(0, len(lignes), 6):  # 6 lignes par transaction (avec espaces)
            if i + 4 < len(lignes):
                transaction_id = int(lignes[i].split(": ")[1].strip())
                client_id = int(lignes[i + 1].split(": ")[1].strip())
                montant = float(lignes[i + 2].split(": ")[1].strip().split()[0])
                date = lignes[i + 3].split(": ")[1].strip()
                statut = lignes[i + 4].split(": ")[1].strip()
                transactions.append(Transaction(transaction_id, client_id, montant, date, statut))
    return transactions


def afficher_transactions(transactions):
    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    transactions = charger_transactions("transaction.txt")
    afficher_transactions(transactions)
