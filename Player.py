# pylint: disable=C0103
from typing import List, Union

from Character import Assault, Health, Magic


class Player():
    """A player of the game.

    A player should be a real person using their real name. A player can then
    choose a character which will have a name of the player's choosing.
    """

    characters = [Assault, Health, Magic]

    @staticmethod
    def get_available_characters() -> List[Union[Assault, Health, Magic]]:
        """Gets a list of character classes which are not currently
        in use in the game.

        Returns:
            A list of character classes which are not currently
            in use in the game.
        """
        return Player.characters

    @staticmethod
    def reset_available_characters() -> None:
        """Reset the list of available characters in a game."""
        Player.characters = [Assault, Health, Magic]

    def __init__(self, name: str) -> None:
        self.name = name
        self.character = None

    def get_name(self) -> str:
        """Gets the name of this player.

        Returns:
            The name of this player.
        """
        return self.name

    def get_character(self) -> Union[Assault, Health, Magic]:
        """Gets the character of this player.

        Returns:
            The name of this player.
        """
        return self.character

    def choose_character(self, character: str, name: str) -> bool:
        """Selects a character for this player.

        Args:
            character: The character to assign to this player.
            name: The name to assign the character.

        Returns:
            True if the assignment was successful.
            False if the character was unavailable.
        """
        if character in map(lambda x: x.__name__, Player.characters):
            index = list(map(lambda x: x.__name__,
                             Player.characters)).index(character)
            self.character = Player.characters[index](name)
            del Player.characters[index]
            return True
        return False
