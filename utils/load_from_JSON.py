import json
from typing import List

from utils.save_to_JSON import TOURNAMENTS_FILE, PLAYERS_FILE


def load_json(file_path: str) -> List[dict]:
    """Charge un fichier JSON et retourne son contenu, ou une liste vide si le fichier est vide/non existant."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retourne une liste vide en cas d'erreur de lecture


# ✅ Charger les tournois
def load_tournaments() -> List[dict]:
    """Charge les tournois depuis le fichier JSON."""
    return load_json(TOURNAMENTS_FILE)


# ✅ Charger les joueurs
def load_players() -> List[dict]:
    """Charge les joueurs depuis le fichier JSON."""
    return load_json(PLAYERS_FILE)
