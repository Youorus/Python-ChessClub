from typing import List

from Model.Player import Player
from Model.Round import Round


class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str,
                 rounds_total: int, round_list: List[Round] = None, player_list: List[Player] = None, description: str = "") -> None:
        self.name: str = name
        self.location: str = location
        self.start_date: str = start_date  # Format: "YYYY-MM-DD"
        self.end_date: str = end_date      # Format: "YYYY-MM-DD"
        self.rounds_total: int = rounds_total
        self.current_round: int = 1  # Commence au premier tour
        self.rounds: List['Round'] = round_list if round_list is not None else []
        self.players: List[str] = player_list if player_list is not None else []
        self.description: str = description

    def __str__(self):
        """Retourne une représentation lisible d'un tournoi."""
        return (
            f"\n🏆 Tournoi : {self.name}\n"
            f"📍 Lieu : {self.location}\n"
            f"📅 Début : {self.start_date}  |  Fin : {self.end_date}\n"
            f"🔢 Nombre de rounds : {self.rounds_total}\n"
            f"📖 Description : {self.description if self.description else 'Aucune description fournie'}\n"
        )

    def to_dict(self):
        """Convertit l'objet tournoi en dictionnaire pour JSON"""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds_total": self.rounds_total,
            "current_round": self.current_round,
            # 🔹 Stocke uniquement les noms des joueurs
            # ✅ Stocker les joueurs en tant qu'objets
            "players": [player.to_dict() for player in self.players],
            # ✅ Inclure les rounds
            "rounds": [round_.to_dict() for round_ in self.rounds],
            "description": self.description
        }
