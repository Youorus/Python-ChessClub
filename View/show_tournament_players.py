def show_tournament_players(tournament):
    """
    Affiche les joueurs du tournoi sélectionné.

    Args:
        tournament (Tournament): Tournoi sélectionné.
    """
    print(tournament.__str__())

    if not tournament.players:
        print("\nAucun joueur inscrit dans ce tournoi.")
        return

    print(f"\n=== Joueurs du Tournoi {tournament.name} ===\n")
    for i, player in enumerate(tournament.players, start=1):
        print(f"{i}. {player.__str__()})")

    input("\nAppuyez sur Entrée pour revenir au menu...")
