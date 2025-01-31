import os

from View.add_player_view import add_player_form
from View.add_tournement_view import add_tournament_form
from View.rapport_menu_view import rapport_menu


def menu():
    """
    Affiche le menu principal et gère la navigation utilisateur.

    Options disponibles :
    1. Créer un tournoi
    2. Ajouter un joueur
    3. Accéder aux rapports
    4. Quitter le programme
    """
    menu_options = ["Créer un tournoi", "Ajouter un joueur", "Rapport", "Quitter"]

    while True:
        # Efface l'écran avant d'afficher le menu (compatibilité Windows/Linux/Mac)
        os.system("clear" if os.name == "posix" else "cls")

        print("\n=== Centre Échecs - Menu Principal ===\n")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choix = input("\nEntrez un choix (1-4) : ").strip()

        if choix == "1":
            add_tournament_form()  # Ajoute un tournoi
        elif choix == "2":
            add_player_form()  # Affiche le formulaire de création de joueur
        elif choix == "3":
            rapport_menu()  # Affiche le menu des rapports
        elif choix == "4":
            print("\nMerci d'avoir utilisé le programme. À bientôt ! 👋")
            break  # Quitte la boucle et termine le programme
        else:
            print("\n❌Entrée invalide. Veuillez entrer un nombre entre 1 et 4.")
            input("Appuyez sur Entrée pour continuer...")
