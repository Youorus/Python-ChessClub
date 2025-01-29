import json
import os
from Execption.player_execption import PlayerAlreadyExistsException
from Model.Player import Player


class PlayerController:
    FILE_PATH = "players.json"

    @staticmethod
    def add_player(national_id: str, last_name: str, first_name: str, dob: str) -> Player:
        """Ajoute un joueur et l'enregistre après validation."""
        new_player = Player(national_id, last_name, first_name, dob)
        PlayerController.save_player(new_player)  # Correction : Appel de la méthode statique
        return new_player

    @staticmethod
    def save_player(player: Player) -> bool:
        """Enregistre un joueur dans le fichier JSON de manière sécurisée."""
        os.makedirs(os.path.dirname(PlayerController.FILE_PATH), exist_ok=True)  # 📂 Crée le dossier si nécessaire

        players = PlayerController.load_players()  # 🔄 Charge les joueurs existants

        # Vérifie si le joueur existe déjà (évite les doublons)
        if any(p["national_id"] == player.national_id for p in players):  # 🔹 Correction ici
            raise PlayerAlreadyExistsException(player.national_id)  # Lève une exception

        players.append(player.to_dict())  # ✅ Ajoute le joueur sous forme de dictionnaire

        #  Écriture des données JSON
        with open(PlayerController.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4)

        return True  # Confirme l’enregistrement

    @staticmethod
    def load_players() -> list:
        """Charge les joueurs depuis le fichier JSON (s'il existe)."""
        if os.path.exists(PlayerController.FILE_PATH):  # Vérifie si le fichier existe
            with open(PlayerController.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)  # 🔄 Charge et retourne la liste des joueurs

        return []  # 🔄 Retourne une liste vide si le fichier n'existe pas
