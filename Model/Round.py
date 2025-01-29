from datetime import datetime
from typing import List

from Model.Match import Match


class Round:
    def __init__(self, round_id: int, match_list : List[Match]):
        self.id = round_id # Stocker l'ID du round
        self.name = f"Round {round_id}"  # Correction : utiliser `id` correctement
        self.matches = match_list  # Liste des matchs (tuples contenant les joueurs et leurs scores)
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp au début
        self.end_time = None  # Sera défini lorsque le round sera terminé
