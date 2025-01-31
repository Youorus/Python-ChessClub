import json
import os
from typing import List

from Controller.save_to_JSON import save_player
from Execption.player_execption import PlayerAlreadyExistsException
from Model.Player import Player


class PlayerController:

    @staticmethod
    def add_player(national_id: str, last_name: str, first_name: str, dob: str):
        """Ajoute un joueur et l'enregistre après validation."""
        new_player = Player(national_id, last_name, first_name, dob)
        save_player(new_player)  # Correction : Appel de la méthode statique
        return
