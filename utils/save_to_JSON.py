import json
import os
from Execption.tournement_execption import TournamentAlreadyExistsException
from Model import Tournament, Player

#  Chemins centralisés pour une meilleure gestion
DATA_DIR = "data"
TOURNAMENTS_FILE = os.path.join(DATA_DIR, "tournaments.json")
PLAYERS_FILE = os.path.join(DATA_DIR, "players.json")


#  Fonction pour s'assurer que le fichier et le dossier existent
def ensure_file_exists(file_path: str):
    """Crée le dossier et le fichier JSON s'ils n'existent pas."""
    os.makedirs(
        os.path.dirname(file_path), exist_ok=True
    )  # ✅ Crée le dossier si nécessaire
    if not os.path.exists(file_path):  # ✅ Crée un fichier JSON vide si non existant
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


#  Fonction pour sauvegarder un fichier JSON
def save_json(file_path: str, data: list):
    """Écrit les données dans un fichier JSON en toute sécurité."""
    ensure_file_exists(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


#  Enregistrement d'un tournoi
def save_tournament(tournament: Tournament) -> bool:
    """Enregistre un tournoi dans le fichier JSON de manière sécurisée."""
    from utils.load_from_JSON import (
        load_json,
    )  # ✅ Import local pour éviter les importations circulaires

    tournaments = load_json(TOURNAMENTS_FILE)

    # Vérifier si un tournoi du même nom, lieu et date existe déjà
    if any(
        t["name"] == tournament.name
        and t["location"] == tournament.location
        and t["start_date"] == tournament.start_date
        for t in tournaments
    ):
        raise TournamentAlreadyExistsException(tournament.name)

    # Convertir en dictionnaire avant l'ajout
    tournaments.append(tournament.to_dict())
    save_json(TOURNAMENTS_FILE, tournaments)  # Sauvegarde les données
    return True


# ✅ Enregistrement d'un joueur
def save_player(player: Player) -> bool:
    """Enregistre un joueur dans le fichier JSON de manière sécurisée."""

    from utils.load_from_JSON import (
        load_json,
    )  # ✅ Import local pour éviter l'importation circulaire

    players = load_json(PLAYERS_FILE)

    # Convertir en dictionnaire avant l'ajout
    players.append(player.to_dict())
    save_json(PLAYERS_FILE, players)  # 💾 Sauvegarde les données
    return True
