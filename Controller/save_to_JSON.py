import json
import os
from typing import List
from Execption.player_execption import PlayerAlreadyExistsException
from Execption.tournement_execption import TournamentAlreadyExistsException
from Model import Tournament, Player

#  Chemins centralisés pour une meilleure gestion
DATA_DIR = "data"
TOURNAMENTS_FILE = os.path.join(DATA_DIR, "tournaments.json")
PLAYERS_FILE = os.path.join(DATA_DIR, "players.json")

#  Fonction pour s'assurer que le fichier et le dossier existent


def ensure_file_exists(file_path: str):
    """Crée le dossier et le fichier JSON s'ils n'existent pas."""
    os.makedirs(os.path.dirname(file_path),
                exist_ok=True)  # 📂 Crée le dossier si nécessaire
    if not os.path.exists(file_path):  # 📄 Crée un fichier JSON vide si non existant
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

#  Fonction pour charger un fichier JSON en toute sécurité


def load_json(file_path: str) -> List[dict]:
    """Charge un fichier JSON et retourne son contenu, ou une liste vide si le fichier est vide/non existant."""
    ensure_file_exists(file_path)  # ✅ S'assure que le fichier existe
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []  # Retourne une liste vide en cas d'erreur de lecture

#  Fonction pour sauvegarder un fichier JSON


def save_json(file_path: str, data: list):
    """Écrit les données dans un fichier JSON en toute sécurité."""
    ensure_file_exists(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

#  Enregistrement d'un tournoi


def save_tournament(tournament: Tournament) -> bool:
    """Enregistre un tournoi dans le fichier JSON de manière sécurisée."""
    tournaments = load_json(TOURNAMENTS_FILE)

    # Vérifier si un tournoi du même nom, lieu et date existe déjà
    if any(t["name"] == tournament.name and t["location"] == tournament.location and t["start_date"] == tournament.start_date for t in tournaments):
        raise TournamentAlreadyExistsException(tournament.name)

    # Convertir en dictionnaire avant l'ajout
    tournaments.append(tournament.to_dict())
    save_json(TOURNAMENTS_FILE, tournaments)  # Sauvegarde les données
    return True

#  Enregistrement d'un joueur


def save_player(player: Player) -> bool:
    """Enregistre un joueur dans le fichier JSON de manière sécurisée."""
    players = load_json(PLAYERS_FILE)

    # Vérifie si le joueur existe déjà (évite les doublons)
    if any(p["national_id"] == player.national_id for p in players):  # 🔹 Correction ici
        raise PlayerAlreadyExistsException(player.national_id)

    # ✅ Convertir en dictionnaire avant l'ajout
    players.append(player.to_dict())
    save_json(PLAYERS_FILE, players)  # 💾 Sauvegarde les données
    return True

# ✅ Charger les tournois


def load_tournaments() -> List[Tournament]:
    """Charge les tournois depuis le fichier JSON."""
    return load_json(TOURNAMENTS_FILE)

# Charger les joueurs


def load_players() -> List[Player]:
    """Charge les joueurs depuis le fichier JSON et retourne une liste de `Player`."""
    players_data = load_json(PLAYERS_FILE)  # ✅ Charger les joueurs depuis JSON
    # ✅ Convertir chaque dictionnaire en `Player`
    return [player for player in players_data]


def load_players_names() -> List[str]:
    """Charge les joueurs depuis le fichier JSON et retourne une liste de noms complets (Prénom Nom)."""
    players_data = load_json(PLAYERS_FILE)
    # ✅Concatène prénom et nom
    return [f"{player['first_name']} {player['last_name']}" for player in players_data]
