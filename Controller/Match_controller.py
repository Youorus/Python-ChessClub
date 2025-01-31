import random
from typing import Tuple, Set, List

from Model import Player
from Model.Match import Match


class MatchController:
    """Gère l'organisation des matchs et l'attribution des scores."""

    @staticmethod
    def generate_matches(
        players: List[Player], past_matches: Set[Tuple[Player, Player]]
    ) -> List[Match]:
        """
        Génère des matchs en s'assurant que
        les mêmes joueurs ne se rencontrent pas plus d'une fois.

        Cette fonction génère une liste de matchs en fonction
        des joueurs disponibles et des rencontres déjà effectuées.
        Elle vérifie si les joueurs ont déjà joué ensemble
        et ajuste les paires pour éviter les répétitions.

        Args:
            players (List[Player]): Liste des joueurs participant au tournoi.
            past_matches (Set[Tuple[Player, Player]]):
            Ensemble des matchs déjà joués sous forme de tuples (Player, Player).

        Returns:
            List[Match]: Liste des matchs générés.
        """

        # Vérification du nombre minimum de joueurs
        if len(players) < 2:
            print("Impossible de générer des matchs : il faut au moins deux joueurs.")
            return []

        # Mélange aléatoire des joueurs (uniquement pour le premier round)
        random.shuffle(players)

        matches = []
        i = 0

        while i < len(players) - 1:
            player1, player2 = players[i], players[i + 1]

            # Vérifier si ces joueurs ont déjà joué ensemble
            if (player1, player2) in past_matches or (player2, player1) in past_matches:
                # Recherche d'un autre adversaire disponible
                j = i + 2
                while j < len(players):
                    alternate_player = players[j]
                    if (player1, alternate_player) not in past_matches and (
                        alternate_player,
                        player1,
                    ) not in past_matches:
                        player2 = alternate_player
                        players[i + 1], players[j] = players[j], players[i + 1]
                        break
                    j += 1
                else:
                    # Aucun autre joueur disponible, on saute ce tour
                    print(
                        f"Impossible de trouver un adversaire pour {player1.first_name} {player1.last_name}."
                    )
                    i += 1
                    continue

            # Création du match avec un score initial de 0
            match_instance = Match(player1, 0, player2, 0)
            matches.append(match_instance)

            # Enregistrement du match pour éviter les doublons
            past_matches.add((player1, player2))

            i += 2  # Passage aux joueurs suivants

        return matches
