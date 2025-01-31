def tournament_details_menu():
    """
    Menu permettant de voir les joueurs ou les rounds d'un tournoi spécifique.
    """
    tournament = select_tournament()
    if not tournament:
        return  # Annulation si aucun tournoi sélectionné

    menu_options = ["Voir les joueurs du tournoi", "Voir les rounds du tournoi", "Retour"]

    while True:
        print(f"\n=== Détails du Tournoi : {tournament.name} ===\n")
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

        choix = input("\nEntrez un choix (1-3) : ").strip()

        if choix == "1":
            show_tournament_players(tournament)
        elif choix == "2":
            show_tournament_rounds(tournament)
        elif choix == "3":
            return  # Retour au menu précédent
        else:
            print("❌ Entrée invalide. Essayez encore.")
            input("Appuyez sur Entrée pour continuer...")
