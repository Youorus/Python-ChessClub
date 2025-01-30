class TournamentException(Exception):
    """Exception de base pour les erreurs liées au tournoi."""
    pass

class InvalidNameException(TournamentException):
    """Exception pour un nom de tournoi invalide."""
    def __init__(self, message="Le nom du tournoi est invalide."):
        super().__init__(message)

class InvalidLocationException(TournamentException):
    """Exception pour un lieu de tournoi invalide."""
    def __init__(self, message="Le lieu du tournoi est invalide."):
        super().__init__(message)

class InvalidDateException(TournamentException):
    """Exception pour une date de tournoi invalide."""
    def __init__(self, message="La date doit être au format YYYY-MM-DD et valide."):
        super().__init__(message)

class PastEndDateException(TournamentException):
    """Exception pour une date de fin avant la date de début."""
    def __init__(self):
        super().__init__("La date de fin du tournoi ne peut pas être avant la date de début.")

class InvalidRoundsTotalException(TournamentException):
    """Exception pour un nombre de rounds invalide."""
    def __init__(self):
        super().__init__("Le nombre de rounds doit être un entier positif supérieur à 0.")

class TournamentAlreadyExistsException(TournamentException):
    """Exception levée lorsqu'un tournoi avec le même nom, lieu et date existe déjà."""
    def __init__(self, tournament_name: str, location: str, date: str):
        super().__init__(f"Le tournoi '{tournament_name}' à '{location}' prévu pour le {date} existe déjà dans la base de données.")
