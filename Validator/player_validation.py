import re
from datetime import datetime


def validate_national_id(national_id: str) -> str:
    """Vérifie si le National ID est valide (2 lettres suivies de 5 chiffres)."""
    if not re.match(r"^[A-Za-z]{2}[0-9]{5}$", national_id):
        raise NationalIdInvalidException()
    return national_id

def validate_name(name: str) -> str:
    """Vérifie que le nom ou prénom ne contient que des lettres, accents et tirets."""
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ-]{2,50}$", name):
        raise NameInvalidException(name)
    return name.capitalize()  # Met la première lettre en majuscule

def validate_dob(dob: str) -> str:
    """Vérifie que la date de naissance est valide (format: JJ/MM/AAAA) et n'est pas dans le futur."""
    try:
        date_obj = datetime.strptime(dob, "%d/%m/%Y")
        if date_obj > datetime.today():
            raise FutureDateException()
        return dob
    except ValueError:
        raise DateOfBirthInvalidException()
