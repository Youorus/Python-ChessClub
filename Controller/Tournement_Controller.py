from typing import List

from Controller.Round_controller import RoundController
from utils.load_from_JSON import load_players, load_tournaments
from utils.save_to_JSON import save_tournament
from Model.Player import Player
from Model.Tournament import Tournament


class TournamentController:

    @staticmethod
    def add_tournament(name, location, start_date, end_date, rounds_total, description):
        """Ajoute un tournoi après validation et génère les rounds."""

        players_list = load_players()  # Charger les joueurs depuis JSON

        #  Vérifier si les joueurs sont bien des objets Player et les convertir si nécessaire
        players = [Player.from_dict(player) for player in players_list]

        round_list = RoundController.generate_rounds(
            rounds_total, players
        )  # ✅ Génération des rounds

        new_tournament = Tournament(
            name,
            location,
            start_date,
            end_date,
            rounds_total,
            round_list,
            players,
            description,
        )

        save_tournament(new_tournament)  # ✅ Sauvegarde
        return new_tournament

    @staticmethod
    def get_all_tournaments() -> List[Tournament]:
        """
        Retourne tous les tournois enregistrés sous forme d'objets Tournament.

        Returns:
            List[Tournament]: Liste des tournois en tant qu'objets Tournament.
        """
        tournaments_data = load_tournaments()

        if not tournaments_data:
            return []

        # Convertir chaque dictionnaire en objet `Tournament` avec from_dict()
        return [Tournament.from_dict(data) for data in tournaments_data]
