def show_tournament_rounds(tournament):
    """
    Affiche les rounds du tournoi sélectionné.

    Args:
        tournament (Tournament): Tournoi sélectionné.
    """
    if not tournament.rounds:
        print("\nAucun round enregistré pour ce tournoi.")
        return

    print(f"\n=== Rounds du Tournoi {tournament.name} ===\n")
    for round_ in tournament.rounds:
        print(round_.__str__())

    input("\nAppuyez sur Entrée pour revenir au menu...")
