class Player:
    """Modèle représentant un joueur d'échecs."""

    def __init__(self, national_id, last_name, first_name, dob):
        self.national_id = national_id
        self.last_name = last_name
        self.first_name = first_name
        self.dob = dob

    def __str__(self):
        """Affiche les informations du joueur."""
        return f"\n {self.first_name} {self.last_name} (ID: {self.national_id}, Né(e) le: {self.dob})\n"

    def __eq__(self, other):
        """Compare deux joueurs en fonction de leur ID national."""
        if isinstance(other, Player):
            return self.national_id == other.national_id
        return False

    def __hash__(self):
        """Rend Player hashable en utilisant l'ID national unique."""
        return hash(self.national_id)

    def to_dict(self):
        """Convertit un objet Player en dictionnaire JSON."""
        return {
            "national_id": self.national_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "dob": self.dob,
        }

    @classmethod
    def from_dict(cls, data):
        """Convertit un dictionnaire en objet Player"""
        return cls(
            national_id=data["national_id"],
            last_name=data["last_name"],
            first_name=data["first_name"],
            dob=data["dob"],
        )
