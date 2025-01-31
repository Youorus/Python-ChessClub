import random
from typing import List, Tuple, Set

from Controller.Match_controller import MatchController
from Model import Player, Match
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

        # Vérifie que des joueurs sont disponibles
        if not players:
            print("Aucun joueur disponible. Impossible de générer des rounds.")
            return []

        num_players = len(players)
        print(f"\n{num_players} joueurs chargés : {[p.first_name + ' ' + p.last_name for p in players]}")

        # Vérifie que le nombre de joueurs est suffisant (au moins 2)
        if num_players < 2:
            print("Impossible de créer des rounds : Il faut au moins 2 joueurs.")
            return []

        # Vérifie que le nombre de joueurs est pair
        if num_players % 2 != 0:
            print("Attention : Nombre impair de joueurs. Un joueur sera laissé de côté à chaque round.")

        # Liste des rounds générés
        rounds = []

        # Ensemble des matchs déjà joués pour éviter les doublons
        past_matches: Set[Tuple[Player, Player]] = set()

        # Compteur du nombre de rounds créés
        rounds_created = 0

        for round_id in range(1, total_rounds + 1):
            print(f"\nGénération du Round {round_id}...")

            # Génération des matchs pour le round actuel
            matches = MatchController.generate_matches(players, past_matches)

            # Vérification si aucun match n'a été généré
            if not matches:
                print(f"Round {round_id} annulé : Pas assez de joueurs disponibles.")
                break  # Arrêt de la génération si plus de rounds ne peuvent être créés

            # Ajout des matchs au suivi des matchs déjà joués
            for match in matches:
                past_matches.add((match.match[0][0], match.match[1][0]))

            # Création de l'objet Round et ajout à la liste des rounds
            round_instance = Round(round_id, matches)
            rounds.append(round_instance)
            rounds_created += 1
            print(f"Round {round_id} créé avec {len(matches)} matchs.")

        # Affichage du nombre de rounds réellement créés
        print(f"\n{rounds_created} round(s) généré(s) sur {total_rounds} demandé(s).")

        return rounds  # Retourne la liste complète des rounds
