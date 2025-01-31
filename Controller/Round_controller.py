from typing import List, Tuple, Set

from Controller.Match_controller import MatchController
from Model import Player
from Model.Round import Round


class RoundController:
    """
    Gère la génération et l'organisation des rounds dans un tournoi d'échecs.

    Cette classe assure la création des rounds en respectant les règles suivantes :
    - Évite que les mêmes joueurs se rencontrent plus d'une fois.
    - Génère des paires en fonction du nombre total de points des joueurs.
    - Vérifie que le nombre de joueurs est suffisant pour générer les rounds.
    """

    @staticmethod
    def generate_rounds(total_rounds: int, players: List[Player]) -> List[Round]:
        """
        Génère une liste de rounds pour un tournoi donné.

        Cette fonction s'assure que les joueurs ne se rencontrent pas plus d'une fois.
        Elle prend en compte les cas où le nombre de joueurs est impair et informe l'utilisateur.

        Args:
            total_rounds (int): Nombre total de rounds à générer.
            players (List[Player]): Liste des joueurs participant au tournoi.

        Returns:
            List[Round]: Liste des rounds générés, ou une liste vide si les conditions ne sont pas remplies.
        """

        if not players:
            print("Aucun joueur disponible. Impossible de générer des rounds.")
            return []

        num_players = len(players)
        print(f"\n{num_players} joueurs chargés : "
              f"{[p.first_name + ' ' + p.last_name for p in players]}")

        if num_players < 2:
            print("Impossible de créer des rounds : Il faut au moins 2 joueurs.")
            return []

        if num_players % 2 != 0:
            print("Attention : Nombre impair de joueurs. Un joueur sera laissé de côté à chaque round.")

        rounds = []
        past_matches: Set[Tuple[Player, Player]] = set()
        rounds_created = 0

        for round_id in range(1, total_rounds + 1):
            print(f"\nGénération du Round {round_id}...")
            matches = MatchController.generate_matches(players, past_matches)

            if not matches:
                print(f"Round {round_id} annulé : Pas assez de joueurs disponibles.")
                break

            for match in matches:
                past_matches.add((match.match[0][0], match.match[1][0]))

            rounds.append(Round(round_id, matches))
            rounds_created += 1
            print(f"Round {round_id} créé avec {len(matches)} matchs.")

        print(f"\n{rounds_created} round(s) généré(s) sur {total_rounds} demandé(s).")
        return rounds
