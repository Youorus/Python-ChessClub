import os

from Controller.Player_controller import PlayerController
from Validator.player_validation import (
    validate_national_id,
    validate_name,
    validate_dob,
)
from Execption.player_execption import (
    NationalIdInvalidException,
    NameInvalidException,
    FutureDateException,
    DateOfBirthInvalidException,
)


def add_player_form():
    """Affiche un formulaire en console pour créer un joueur avec validation."""
    os.system("clear" if os.name == "posix" else "cls")  # Nettoie l'écran
    print("\n♟️ Formulaire d'Ajout d'un Joueur\n")

    while True:
        try:
            national_id = validate_national_id(
                input("🆔 Entrez l'ID du joueur (ex: AB12345) : ").strip()
            )
            break
        except NationalIdInvalidException as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            last_name = validate_name(input("👤 Entrez le nom de famille : ").strip())
            break
        except NameInvalidException as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            first_name = validate_name(input("👤 Entrez le prénom : ").strip())
            break
        except NameInvalidException as e:
            print(f"❌ Erreur : {e}")

    while True:
        try:
            dob = validate_dob(
                input("📅 Entrez la date de naissance (JJ/MM/AAAA) : ").strip()
            )
            break
        except (FutureDateException, DateOfBirthInvalidException) as e:
            print(f"❌ Erreur : {e}")

    new_player = PlayerController.add_player(national_id, last_name, first_name, dob)

    # Nettoie l'écran après saisie
    os.system("clear" if os.name == "posix" else "cls")
    # Affiche les infos du joueur créé
    print(f"✅ Joueur ajouté avec succès : {new_player.__str__()} ")
    input("\n🔄 Appuyez sur Entrée pour revenir au menu...")
