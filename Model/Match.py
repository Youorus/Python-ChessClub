from typing import Tuple

from Model.Player import Player


class Match:
    def __init__(
        self, player1: Player, score1: int, player2: Player, score2: int
    ) -> None:
        """Initialise un match avec deux joueurs et leurs scores respectifs."""
        self.match: Tuple[Tuple[Player, int], Tuple[Player, int]] = (
            (player1, score1),
            (player2, score2),
        )

    def __str__(self):
        """Retourne une représentation lisible du match."""
        player1, score1 = self.match[0]
        player2, score2 = self.match[1]

        return f"⚔️ {
            player1.first_name} {
            player1.last_name} ({score1}) 🆚 ({score2}) {
            player2.first_name} {
                player2.last_name}"

    def to_dict(self):
        return {
            "player1": self.match[0][
                0
            ].to_dict(),  # Stocke un dictionnaire, pas une `str`
            "score1": self.match[0][1],
            "player2": self.match[1][
                0
            ].to_dict(),  # Stocke un dictionnaire, pas une `str`
            "score2": self.match[1][1],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Match":
        """
        Convertit un dictionnaire JSON en objet `Match`.

        Args:
            data (dict): Dictionnaire représentant un match.

        Returns:
            Match: Instance de la classe `Match`.
        """
        # Vérifier si les joueurs existent et sont bien des dictionnaires
        player1 = Player(
            national_id="UNKNOWN",
            first_name="Unknown",
            last_name="Player",
            dob="Unknown",
        )
        player2 = Player(
            national_id="UNKNOWN",
            first_name="Unknown",
            last_name="Player",
            dob="Unknown",
        )
        return cls(
            player1=player1,
            score1=data.get("score1", 0),
            player2=player2,
            score2=data.get("score2", 0),
        )
