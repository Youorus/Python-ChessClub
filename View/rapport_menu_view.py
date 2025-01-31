import os

from Controller.Tournement_Controller import TournamentController
from View.all_players_view import all_players_view
from View.all_tournement_view import display_all_tournaments, select_tournament
from View.tournement_menu_view import tournament_details_menu


def rapport_menu():
    """
    Affiche le menu des rapports et gère la navigation utilisateur.
    """
    menu_options = [
        "Liste des joueurs",
        "Liste des tournois",
        "Voir les détails d'un tournoi",
        "Retour",
    ]

    while True:
        os.system("clear" if os.name == "posix" else "cls")

        print("\n=== Centre Échecs - Menu des Rapports ===\n")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choix = input("\nEntrez un choix (1-4) : ").strip()

        if choix == "1":
            all_players_view()  # Afficher la liste des joueurs
        elif choix == "2":
            display_all_tournaments(
                TournamentController.get_all_tournaments()
            )  # Afficher les tournois
        elif choix == "3":
            tournament = select_tournament()  # Sélectionner un tournoi
            if tournament:  # ✅ Si un tournoi est sélectionné, on affiche ses détails
                tournament_details_menu(tournament)
        elif choix == "4":
            return  # Retour au menu principal
        else:
            print("❌ Entrée invalide. Veuillez entrer un nombre entre 1 et 4.")
            input("Appuyez sur Entrée pour continuer...")
