from Controller.Tournement_Controller import TournamentController


def all_tournaments_view():
    """
    Affiche la liste des tournois enregistrés.
    """
    tournaments = TournamentController.get_all_tournaments()

    if not tournaments:
        print("\nAucun tournoi enregistré.")
        return

    print("\n=== Liste des Tournois ===\n")
    for i, tournament in enumerate(tournaments, start=1):
        print(f"{i} - {tournament.__str__()}")

    print("\n")
    input("Appuyez sur Entrée pour revenir au menu...")
