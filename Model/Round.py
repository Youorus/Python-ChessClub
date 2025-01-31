from datetime import datetime
from typing import List

from Model.Match import Match
from Model.Player import Player


class Round:
    def __init__(self, round_id: int, match_list: List[Match]):
        self.id = round_id  # Stocker l'ID du round
        # Correction : utiliser `id` correctement
        self.name = f"Round {round_id}"
        # Liste des matchs (tuples contenant les joueurs et leurs scores)
        self.matches = match_list
        self.start_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )  # Timestamp au début
        self.end_time = None  # Sera défini lorsque le round sera terminé

    def __str__(self):
        """Retourne une représentation lisible du round."""
        match_details = (
            "\n".join(f"  - {match}" for match in self.matches)
            if self.matches.__str__()
            else "  Aucun match pour ce round."
        )

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
            "matches": [match.to_dict() for match in self.matches],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Round":
        matches_data = data.get("matches", [])

        fixed_matches = []
        for match in matches_data:
            if not isinstance(match, dict):
                print(f"❌ Erreur : Match invalide (Type: {type(match)})")
                continue

            player1_data = match.get("player1")
            player2_data = match.get("player2")

            fixed_matches.append({
                "player1": player1_data.to_dict() if isinstance(player1_data, Player) else player1_data,
                "score1": match["score1"],
                "player2": player2_data.to_dict() if isinstance(player2_data, Player) else player2_data,
                "score2": match["score2"]
            })

        return cls(
            round_id=data["round_id"],
            match_list=[
                Match(
                    player1=Player.from_dict(match["player1"]) if isinstance(match["player1"], dict) else None,
                    score1=match["score1"],
                    player2=Player.from_dict(match["player2"]) if isinstance(match["player2"], dict) else None,
                    score2=match["score2"]
                ) for match in fixed_matches
            ]
        )
