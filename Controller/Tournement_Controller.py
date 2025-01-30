import json
import os
from typing import List

from Execption.tournement_execption import TournamentAlreadyExistsException
from Model.Tournament import Tournament

class TournamentController:
    FILE_PATH = "data/tournaments.json"

    @staticmethod
    def add_tournament(name: str, location: str, start_date: str, end_date: str,
                       rounds_total: int = 4, description: str = "") -> Tournament:
        """Ajoute un tournoi et l'enregistre après validation."""
        new_tournament = Tournament(name, location, start_date, end_date, rounds_total, description=description)
        TournamentController.save_tournament(new_tournament)  # Enregistrement du tournoi
        return new_tournament

    @staticmethod
    def save_tournament(tournament: Tournament) -> bool:
        """Enregistre un tournoi dans le fichier JSON de manière sécurisée."""
        os.makedirs(os.path.dirname(TournamentController.FILE_PATH), exist_ok=True)  # 📂 Crée le dossier si nécessaire

        tournaments = TournamentController.load_tournaments()  # 🔄 Charge les tournois existants

        #  Vérifie si le tournoi existe déjà (même nom, même lieu, même date)
        if any(t["name"] == tournament.name and
               t["location"] == tournament.location and
               t["start_date"] == tournament.start_date for t in tournaments):
            raise TournamentAlreadyExistsException(tournament.name, tournament.location, tournament.start_date)

        tournaments.append(tournament.to_dict())  # Ajoute le tournoi

        #  Écriture des données JSON
        with open(TournamentController.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(tournaments, file, indent=4)

        return True  # ✅ Confirme l'enregistrement

    @staticmethod
    def load_tournaments() -> List[Tournament]:
        """Charge les tournois depuis le fichier JSON (s'il existe)."""
        if os.path.exists(TournamentController.FILE_PATH):  # 📂 Vérifie si le fichier existe
            with open(TournamentController.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)  # 🔄 Charge et retourne la liste des tournois

        return []  # 🔄 Retourne une liste vide si le fichier n'existe pas
