import os
import time

from View.home_view import welcome
from View.menu_view import menu


def main():
    """
    Point d'entrée principal de l'application.
    - Affiche un message de bienvenue.
    - Charge le menu principal.
    - Gère les erreurs potentielles pour éviter les crashs.
    """

    # Nettoie l'écran avant d'afficher le message de bienvenue
    os.system("clear" if os.name == "posix" else "cls")

    # Afficher l'écran de bienvenue
    welcome()

    # Pause de 2 secondes avant d'afficher le menu
    time.sleep(2)

    # Démarrer le menu principal
    try:
        menu()
    except Exception as e:
        print(f"\n❌ Une erreur inattendue est survenue : {e}")
        input("Appuyez sur Entrée pour quitter...")


# Exécuter uniquement si ce fichier est le point d'entrée principal
if __name__ == "__main__":
    main()
