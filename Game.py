# pylint: disable=C0103
from random import choice as choose
from typing import Union

from Player import Player


class Game():
    """The main game controller.

    Handles all of the logic which makes the game work.
    """

    def __init__(self) -> None:
        self.player_1 = None
        self.player_2 = None
        self.current_player = 0
        self.order = [None, None]
        self.winners = []
        self.round = 1

    def get_player_1(self) -> Union[Player, None]:
        """Gets player 1 in the current game if one has been set.

        Returns:
            Player 1 in the current game if one has been set. Otherwise, None.
        """
        return self.player_1

    def get_player_2(self) -> Union[Player, None]:
        """Gets player 2 in the current game if one has been set.

        Returns:
            Player 2 in the current game if one has been set. Otherwise, None.
        """
        return self.player_2

    def get_current_player(self) -> Union[Player, None]:
        """Gets the player whose turn it currently is in the current game.

        Returns:
            The player whose turn it currently is in the current game if the
            playing order has been decided. Otherwise, None.
        """
        return self.order[self.current_player]

    def get_opponent_player(self) -> Player:
        """Gets the player whose turn it currently isn't in the current game.

        Returns:
            The player whose turn it currently isn't in the current game if the
            playing order has been decided. Otherwise, None.
        """
        return self.order[1 if self.current_player == 0 else 0]

    def swap_player(self) -> None:
        """Changes whose turn it currently is in the game."""
        self.current_player = 1 if self.current_player == 0 else 0

    def set_players(self, player_1: Player, player_2: Player) -> None:
        """Set player 1 and player 2 in the current game.

        Args:
            player_1: The Player object for player 1.
            player_2: The Player object for player 2.
        """
        self.player_1 = player_1
        self.player_2 = player_2

    def coin_toss(self, choice: str) -> str:
        """Flips a coin and compares it against the choice made by player 1 of
        the current game. This will set the order in which players will take
        their turns.

        Args:
            choice: The choice made by player 1 of the current game: "Heads"
            or "Tails".

        Returns:
            The result of the coin flip: "Heads" or "Tails".
        """
        outcome = choose(["Heads", "Tails"])
        self.current_player = 0
        self.order = [self.player_1, self.player_2] if outcome == choice else [
            self.player_2, self.player_1
        ]
        return outcome

    def register_round_winner(self, player: Player):
        """Registers the winner of a round."""
        self.winners.append(player)

    def next_round(self, draw: bool) -> None:
        """Resets the players' health points.

        Increments round number if the round wasn't a draw."""
        if not draw:
            self.round += 1
        self.player_1.get_character().reset_health()
        self.player_2.get_character().reset_health()
        self.player_1.get_character().reset_damage_ticks()
        self.player_2.get_character().reset_damage_ticks()

    def get_game_winner(self) -> Union[Player, None]:
        """Gets the overall winner of the game, or None if it is a draw.

        Returns:
            The player who won the game, or None.
        """
        player_1_wins = self.winners.count(self.player_1)
        player_2_wins = self.winners.count(self.player_2)
        if player_1_wins > player_2_wins:
            return self.player_1
        if player_2_wins > player_1_wins:
            return self.player_2
        return None

    def is_round_over(self) -> bool:
        """Determine if the round is over. This happens when one or both
        players are dead.

        Returns:
            If the round is over.
        """
        if self.order == [None, None]:
            return False
        return any(map(lambda x: x.get_character().is_dead(), self.order))

    def is_game_over(self) -> bool:
        """Determine if the game is over. This happens when one or both
        players are dead on the third round.

        Returns:
            If the game is over.
        """
        if self.is_round_over() and self.round == 3:
            return True
        return False
