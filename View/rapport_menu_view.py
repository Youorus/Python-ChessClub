import os
from View.players_view import all_players_view
from View.tournaments_view import all_tournaments_view, tournament_details_menu
from View.menu_view import menu

def rapport_menu():
    """
    Affiche le menu des rapports et gère la navigation utilisateur.
    """
    menu_options = ["Liste des joueurs", "Liste des tournois", "Voir les détails d'un tournoi", "Retour"]

    while True:
        os.system("clear" if os.name == "posix" else "cls")

        print("\n=== Centre Échecs - Menu des Rapports ===\n")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choix = input("\nEntrez un choix (1-4) : ").strip()

        if choix == "1":
            all_players_view()  # Vue pour afficher les joueurs
        elif choix == "2":
            all_tournaments_view()  # Vue pour afficher les tournois
        elif choix == "3":
            tournament_details_menu()  # Afficher les joueurs et rounds d'un tournoi
        elif choix == "4":
            menu()  # Retour au menu principal
            break
        else:
            print("❌ Entrée invalide. Veuillez entrer un nombre entre 1 et 4.")
            input("Appuyez sur Entrée pour continuer...")
