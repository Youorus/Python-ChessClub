import os

from View.menu_view import menu
from View.players_view import all_players_view
from View.tournaments_view import all_tournements_view


def rapport_menu():
    """
    Affiche le menu des rapports et gère la navigation utilisateur.

    Options disponibles :
    1. Liste des joueurs
    2. Liste des tournois
    3. Retour au menu principal
    """
    menu_options = ["Liste des joueurs", "Liste des tournois", "Retour"]

    while True:
        # Efface l'écran avant d'afficher le menu (compatibilité Windows/Linux/Mac)
        os.system("clear" if os.name == "posix" else "cls")

        print("\n=== Centre Échecs - Menu des Rapports ===\n")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choix = input("\nEntrez un choix (1-3) : ").strip()

        if choix == "1":
            all_players_view()  # Affiche la liste des joueurs
        elif choix == "2":
            all_tournements_view()  # Affiche la liste des tournois
        elif choix == "3":
            menu()  # Retour au menu principal
            break  # Arrête la boucle pour revenir au menu principal
        else:
            print("\n❌Entrée invalide. Veuillez entrer un nombre entre 1 et 3.")
            input("Appuyez sur Entrée pour continuer...")
