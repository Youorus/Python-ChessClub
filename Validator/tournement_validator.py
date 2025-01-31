import re
from datetime import datetime
from Execption.tournement_execption import (
    InvalidNameException, InvalidLocationException, InvalidDateException,
    PastEndDateException, InvalidRoundsTotalException
)


def validate_tournament_name(name: str) -> str:
    """Vérifie que le nom du tournoi contient seulement des lettres, chiffres, espaces et tirets."""
    if not re.match(r"^[A-Za-z0-9À-ÖØ-öø-ÿ -]{3,50}$", name):
        raise InvalidNameException()
    return name.strip().title()


def validate_location(location: str) -> str:
    """Vérifie que le lieu du tournoi est valide."""
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ -]{3,50}$", location):
        raise InvalidLocationException()
    return location.strip().title()


def validate_date(date_str: str) -> str:
    """Vérifie que la date est valide et au format européen (JJ/MM/AAAA)."""
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")  # Format européen
        if date_obj.year < 1900 or date_obj.year > 2100:
            raise InvalidDateException(
                "L'année du tournoi doit être comprise entre 1900 et 2100.")
        return date_str
    except ValueError:
        raise InvalidDateException()


def validate_tournament_dates(start_date: str, end_date: str) -> tuple:
    """Vérifie que la date de fin du tournoi n'est pas avant la date de début."""
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")

    if end < start:
        raise PastEndDateException()

    return start_date, end_date


def validate_rounds_total(rounds_total: str) -> int:
    """Vérifie que le nombre total de rounds est un entier positif. Si vide, utilise la valeur par défaut (4)."""
    if rounds_total.strip() == "":
        return 4  # Valeur par défaut
    try:
        rounds_total = int(rounds_total)
        if rounds_total <= 0:
            raise InvalidRoundsTotalException()
        return rounds_total
    except ValueError:
        raise InvalidRoundsTotalException(
            "Veuillez entrer un nombre entier valide pour les rounds.")
