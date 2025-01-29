class PlayerExecption(Exception):
    """Exception de base pour les erreurs de validation."""
    pass

class NationalIdInvalidException(PlayerExecption):
    """Exception pour un National ID invalide."""
    def __init__(self, message="Le National ID doit contenir exactement 2 lettres suivies de 5 chiffres (ex: AB12345)."):
        super().__init__(message)

class NameInvalidException(PlayerExecption):
    """Exception pour un nom/prénom invalide."""
    def __init__(self, name):
        message = f"Le nom/prénom '{name}' contient des caractères invalides ou est trop court/long."
        super().__init__(message)

class DateOfBirthInvalidException(PlayerExecption):
    """Exception pour une date de naissance invalide."""
    def __init__(self, message="La date de naissance doit être au format JJ/MM/AAAA et valide."):
        super().__init__(message)

class FutureDateException(DateOfBirthInvalidException):
    """Exception pour une date de naissance dans le futur."""
    def __init__(self):
        super().__init__("La date de naissance ne peut pas être dans le futur.")

class PlayerAlreadyExistsException(PlayerExecption):
    """Exception pour un joueur déjà enregistré."""
    def __init__(self, national_id):
        super().__init__(f"⚠️ Joueur avec le National ID '{national_id}' est déjà enregistré.")