from Controller.Player_controller import PlayerController


def all_players_view():
    """
    Affiche la liste des joueurs triés par ordre alphabétique.

    Cette vue récupère la liste des joueurs via `PlayerController.display_players()` et l'affiche.
    """
    players = PlayerController.get_all_players()

    if not players:
        print("\nAucun joueur enregistré.")
        return

    print("\n=== Liste des Joueurs (triée) ===\n")
    for i, player in enumerate(players, start=1):
        print(f"{i}. {player.__str__()}")

    input("\nAppuyez sur Entrée pour revenir au menu...")