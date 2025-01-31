import os

from View.add_player_view import add_player_form
from View.add_tournement_view import add_tournament_form


def afficher_menu():
    """Affiche le menu principal et gère la navigation."""
    menu_options = ["Créer un tournoi",
                    "Voir les tournois", "Ajouter un joueur", "Quitter"]

    while True:
        # Efface l'écran avant d'afficher le menu
        os.system("clear" if os.name == "posix" else "cls")
        print("\n♟️ Centre Échecs - Menu\n")
        print(" | ".join(
            f"[{option}]" if i == 0 else option for i, option in enumerate(menu_options)))

        choix = input("\n👉 Utilisez 1-4 pour choisir une option : ")

        if choix == "1":
            add_tournament_form()  # 📌 Ajoute le tournoi
        elif choix == "2":
            print("\n📂 Affichage de la liste des tournois...\n")
            input("\n🔄 Appuyez sur Entrée pour revenir au menu...")
        elif choix == "3":
            add_player_form()  # Affiche le formulaire de création de joueur
        elif choix == "4":
            print("\n👋 Au revoir !")
            break
        else:
            print("❌ Entrée invalide. Essayez encore !")
            input("\n🔄 Appuyez sur Entrée pour réessayer...")


afficher_menu()
