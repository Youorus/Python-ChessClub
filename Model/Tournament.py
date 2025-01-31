from typing import List

from Model.Player import Player
from Model.Round import Round


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        rounds_total: int,
        round_list: List[Round] = None,
        player_list: List[Player] = None,
        description: str = "",
    ) -> None:
        self.name: str = name
        self.location: str = location
        self.start_date: str = start_date  # Format: "YYYY-MM-DD"
        self.end_date: str = end_date  # Format: "YYYY-MM-DD"
        self.rounds_total: int = rounds_total
        self.current_round: int = 1  # Commence au premier tour
        self.rounds: List["Round"] = round_list if round_list is not None else []
        self.players: List[str] = player_list if player_list is not None else []
        self.description: str = description

    def __str__(self):
        """Retourne une représentation concise du tournoi sur une seule ligne."""
        return f"🏆 {self.name} | 📍 {self.location} | 📅 {self.start_date} - {self.end_date}"

    def to_dict(self):
        """Convertit l'objet tournoi en dictionnaire pour JSON"""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds_total": self.rounds_total,
            "current_round": self.current_round,  # Stocke uniquement les noms des joueurs
            "players": [
                player.to_dict() for player in self.players
            ],  # tocker les joueurs en tant qu'objets
            "rounds": [
                round_.to_dict() for round_ in self.rounds
            ],  # Inclure les rounds
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Tournament":
        """
        Convertit un dictionnaire JSON en objet `Tournament`.

        Args:
            data (dict): Dictionnaire représentant un tournoi.

        Returns:
            Tournament: Instance de la classe `Tournament`.
        """
        players_data = data.get("players", [])
        rounds_data = data.get("rounds", [])
        #  Retourne l'objet Tournament
        return cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            rounds_total=data["rounds_total"],
            player_list=[
                Player.from_dict(player) if isinstance(player, dict) else None
                for player in players_data
            ],  # Vérifie que `player` est un dict avant conversion
            round_list=[
                Round.from_dict(round_) if isinstance(round_, dict) else None
                for round_ in rounds_data
            ],  # Vérifie que `round_` est un dict avant conversion
            description=data.get("description", ""),
        )
