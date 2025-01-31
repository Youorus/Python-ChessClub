from datetime import datetime
from typing import List

from Model.Match import Match


class Round:
    def __init__(self, round_id: int, match_list: List[Match]):
        self.id = round_id  # Stocker l'ID du round
        # Correction : utiliser `id` correctement
        self.name = f"Round {round_id}"
        # Liste des matchs (tuples contenant les joueurs et leurs scores)
        self.matches = match_list
        self.start_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")  # Timestamp au début
        self.end_time = None  # Sera défini lorsque le round sera terminé

    def __str__(self):
        """Retourne une représentation lisible du round."""
        match_details = "\n".join(
            f"  - {match}" for match in self.matches
        ) if self.matches.__str__() else "  Aucun match pour ce round."

        return (
            f"\n{self.name}\n"
            f"🕒 Début : {self.start_time}\n"
            f"🕛 Fin : {self.end_time if self.end_time else 'En cours'}\n"
            f"⚔️ Matchs :\n{match_details}\n"
        )


    def to_dict(self):
        """Convertit l'objet Round en dictionnaire pour JSON."""
        return {
            "round_id": self.id,
            # Inclut tous les matchs
            "matches": [match.to_dict() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Round":
        """
        Convertit un dictionnaire JSON en objet `Round`.

        Args:
            data (dict): Dictionnaire représentant un round.

        Returns:
            Round: Instance de la classe `Round`.
        """
        return cls(
            round_id=data["round_id"],
            match_list=[Match.from_dict(match) for match in data.get("matches", [])]
        )