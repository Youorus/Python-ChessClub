import os

from Controller.Tournement_Controller import TournamentController
from Execption.tournement_execption import (
    InvalidNameException, InvalidDateException, PastEndDateException, InvalidRoundsTotalException
)
from Validator.tournement_validator import (
    validate_tournament_name, validate_date, validate_tournament_dates, validate_rounds_total
)


def add_tournament_form():
    """Affiche un formulaire en console pour créer un tournoi avec validation."""
    os.system("clear" if os.name == "posix" else "cls")  # Nettoie l'écran
    print("\n♟️ Formulaire de Création d'un Tournoi\n")

    while True:
        try:
            name = validate_tournament_name(
                input("🏆 Nom du tournoi : ").strip())
            break
        except InvalidNameException as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            location = input("📍 Lieu du tournoi : ").strip().capitalize()
            break
        except Exception as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            start_date = validate_date(
                input("📅 Date de début (JJ/MM/AAAA) : ").strip())
            break
        except InvalidDateException as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            end_date = validate_date(
                input("📅 Date de fin (JJ/MM/AAAA) : ").strip())
            start_date, end_date = validate_tournament_dates(
                start_date, end_date)
            break
        except (InvalidDateException, PastEndDateException) as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            rounds_total_input = input(
                "🔢 Nombre total de rounds (par défaut : 4) : ").strip()
            rounds_total = validate_rounds_total(rounds_total_input)
            break
        except (ValueError, InvalidRoundsTotalException) as e:
            print(f"❌ Erreur : {e}")

    description = input("📝 Description du tournoi (optionnel) : ").strip()
    if not description:
        description = "Aucune description fournie"

    tournament = TournamentController.add_tournament(
        name, location, start_date, end_date, rounds_total, description)

    # Nettoie l'écran après saisie
    os.system("clear" if os.name == "posix" else "cls")
    print(f"\n✅ Tournoi créé avec succès : {tournament.__str__()} \n")
    input("\n🔄 Appuyez sur Entrée pour revenir au menu...")
