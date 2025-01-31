from typing import List

from utils.load_from_JSON import load_players
from utils.save_to_JSON import save_player
from Model.Player import Player


class PlayerController:

    @staticmethod
    def add_player(
        national_id: str, last_name: str, first_name: str, dob: str
    ) -> Player:
        """Ajoute un joueur et l'enregistre après validation."""
        new_player = Player(national_id, last_name, first_name, dob)
        save_player(new_player)  # Correction : Appel de la méthode statique
        return new_player

    @staticmethod
    def get_all_players() -> List[Player]:
        """
        Récupère et trie les joueurs par ordre alphabétique.

        Returns:
            List[Player]: Liste des objets Player triés.
        """
        players_data = load_players()

        if not players_data:
            return []

        # Convertir les dictionnaires en objets `Player`
        players = [Player.from_dict(player) for player in players_data]

        # Trier les joueurs par ordre alphabétique (nom, prénom)
        return sorted(
            players, key=lambda p: (p.last_name.lower(), p.first_name.lower())
        )
