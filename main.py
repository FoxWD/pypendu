import random


def getRandomWord():
    """Choisit un mot aléatoire dans une liste prédéfinie."""
    mots = [
        "python",
        "programmation",
        "ordinateur",
        "algorithmique",
        "developpement",
        "intelligence",
        "application",
        "interface",
        "variable",
        "fonction",
    ]
    return random.choice(mots)


def display_gameState(erreurs):
    """Affiche l'état actuel du pendu en fonction du nombre d'erreurs."""
    etapes = [
        """
        -----
        |   |
        |
        |
        |
        |
        ---------
        """,
        """
        -----
        |   |
        |   O
        |
        |
        |
        ---------
        """,
        """
        -----
        |   |
        |   O
        |   |
        |
        |
        ---------
        """,
        """
        -----
        |   |
        |   O
        |  /|
        |
        |
        ---------
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |
        |
        ---------
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |  /
        |
        ---------
        """,
        """
        -----
        |   |
        |   O
        |  /|\\
        |  / \\
        |
        ---------
        """,
    ]
    return etapes[min(erreurs, len(etapes) - 1)]


def play():
    """Fonction principale du jeu."""
    # Initialisation
    mot = getRandomWord()
    letters_found = set()
    proposed_letters = set()
    nb_errors = 0
    max_errors = 6

    print("Bienvenue au jeu du Pendu!")

    # Boucle principale
    while nb_errors < max_errors:
        #  Affichage de l'état actuel du pendu
        print(display_gameState(nb_errors))

        # Afficher le mot avec les lettres trouvées
        display_word = ""
        for letter in mot:
            if letter in letters_found:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Mot: ", display_word)
        print(f"Erreur: {nb_errors}/{max_errors}")
        print("Lettres proposées: ", ", ".join(sorted(proposed_letters)))

        #  Vérifier si le mot est trouvé
        if all(letter in letters_found for letter in mot):
            print("Bravo! Vous avez trouvé le mot!", mot)
            return

        # Demander une lettre à l'utilisateur
        letter = input("Proposez une lettre: ").strip().lower()

        # Vérifier si la lettre est valide
        if len(letter) != 1 or not letter.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue

        # Vérifier si la lettre a déjà été proposée
        if letter in proposed_letters:
            print("Vous avez déjà proposé cette lettre.")
            continue

        # Ajouter la lettre aux lettres proposées
        proposed_letters.add(letter)

        # Vérifier si la lettre est dans le mot
        if letter in mot:
            print("Bonne réponse!")
            letters_found.add(letter)
        else:
            print("Mauvaise réponse!")
            nb_errors += 1

    # Si on sort de la boucle, c'est que le joueur a perdu
    print(display_gameState(nb_errors))
    print(f"Dommage, vous avez perdu!!! \nLe mot était: {mot}")


# Lancer le jeu
if __name__ == "__main__":
    play()
    # Demander si le joueur veut rejouer
    while input("Voulez-vous rejouer? (o/n): ").lower() == "o":
        play()

    print("Merci d'avoir joué!")
