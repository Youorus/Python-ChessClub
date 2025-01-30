from typing import List

from Model.Player import Player
from Model.Round import Round


class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str,
                 rounds_total: int = 4, round_list: List[Round] = None, player_list: List[Player] = None, description: str = "") -> None:
        self.name: str = name
        self.location: str = location
        self.start_date: str = start_date  # Format: "YYYY-MM-DD"
        self.end_date: str = end_date      # Format: "YYYY-MM-DD"
        self.rounds_total: int = rounds_total
        self.current_round: int = 1 # Commence au premier tour
        self.rounds: List['Round'] = round_list if round_list is not None else []
        self.players: List['Player'] = player_list if player_list is not None else []
        self.description: str = description


    def to_dict(self):
        """Convertit un objet Tournament en dictionnaire JSON-compatible."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds_total": self.rounds_total,
            "description": self.description
        }