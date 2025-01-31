from Controller.Tournement_Controller import TournamentController

def select_tournament():
    """
    Permet de sélectionner un tournoi par son numéro.

    Returns:
        Tournament | None: Retourne le tournoi sélectionné ou None si aucun tournoi n'existe.
    """
    tournaments = TournamentController.get_all_tournaments()  # Chargement unique

    if not tournaments:
        print("\nAucun tournoi enregistré.")
        return None

    display_all_tournaments(tournaments)  # Réutilisation sans recharger

    while True:
        try:
            choix = int(input("\nEntrez le numéro du tournoi (ou 0 pour annuler) : ").strip())
            if choix == 0:
                return None
            if 1 <= choix <= len(tournaments):
                return tournaments[choix - 1]  # Retourne le tournoi sélectionné
            print("❌ Numéro invalide. Essayez encore.")
        except ValueError:
            print("❌ Entrée invalide. Entrez un numéro valide.")



def display_all_tournaments(tournaments):
    """
      Affiche la liste des tournois enregistrés.

      Args:
          tournaments (List[Tournament]): Liste des tournois.
      """
    if not tournaments:
        print("\nAucun tournoi enregistré.")
        return

    print("\n=== Liste des Tournois ===\n")
    for i, tournament in enumerate(tournaments, start=1):
        print(f"{i} - {tournament.__str__()}")
