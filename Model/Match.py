from typing import Tuple, List

from Model.Player import Player


class Match:
    def __init__(self, player1: Player, score1: int, player2: Player, score2: int) -> None:
        """Initialise un match avec deux joueurs et leurs scores respectifs."""
        self.match: Tuple[Tuple[Player, int], Tuple[Player, int]] = (
            (player1, score1), (player2, score2))

    def __str__(self):
        """Retourne une représentation lisible du match."""
        player1, score1 = self.match[0]
        player2, score2 = self.match[1]

        return f"⚔️ {player1.first_name} {player1.last_name} ({score1}) 🆚 ({score2}) {player2.first_name} {player2.last_name}"

    def to_dict(self):
        """Convertit un match en dictionnaire, incluant sa version textuelle via __str__()"""
        return {
            "player1": f"{self.match[0][0].first_name} {self.match[0][0].last_name}",
            "score1": self.match[0][1],
            "player2": f"{self.match[1][0].first_name} {self.match[1][0].last_name}",
            "score2": self.match[1][1]
        }
