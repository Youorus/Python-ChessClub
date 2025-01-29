import re
from datetime import datetime

from Execption.tournement_execption import InvalidNameException, InvalidLocationException, InvalidDateException, \
    PastEndDateException, InvalidRoundsTotalException


def validate_tournament_name(name: str) -> str:
    """Vérifie que le nom du tournoi ne contient que des lettres, chiffres, espaces et tirets."""
    if not re.match(r"^[A-Za-z0-9À-ÖØ-öø-ÿ -]{3,50}$", name):
        raise InvalidNameException("Le nom du tournoi doit contenir entre 3 et 50 caractères valides.")
    return name.strip().title()


def validate_date(date_str: str) -> str:
    """Vérifie que la date est au format européen (JJ/MM/AAAA) et est une date valide."""
    try:
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")  # Format JJ/MM/AAAA
        return date_str
    except ValueError:
        raise InvalidDateException("La date doit être au format JJ/MM/AAAA et valide.")


def validate_tournament_dates(start_date: str, end_date: str) -> tuple:
    """Vérifie que la date de fin du tournoi n'est pas avant la date de début."""
    start = datetime.strptime(start_date, "%d/%m/%Y")  # Format JJ/MM/AAAA
    end = datetime.strptime(end_date, "%d/%m/%Y")  # Format JJ/MM/AAAA

    if end < start:
        raise PastEndDateException()

    return start_date, end_date


def validate_rounds_total(rounds_total: int) -> int:
    """Vérifie que le nombre total de rounds est un entier positif."""
    if not isinstance(rounds_total, int) or rounds_total <= 0:
        raise InvalidRoundsTotalException()
    return rounds_total
