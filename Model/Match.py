from typing import Tuple, List

from Model.Player import Player

class Match:
    def __init__(self, player1: Player, score1: int, player2: Player, score2: int) -> None:
        self.match: Tuple[List[Player, int], List[Player, int]] = ([player1, score1], [player2, score2])