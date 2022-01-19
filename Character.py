# pylint: disable=C0103
from random import randint, uniform
from typing import Tuple


class Character():
    """A character in the game.

    A character is fictional. They should be given a name by the player they
    are assigned to. A character is either of Assault, Health or Magic class
    - each having its own strengths and weaknesses.
    """

    def __init__(self, name: str, health: int, damage: int) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.damage_per_round = 0

    def get_name(self) -> str:
        """Gets the name of this character.

        Returns:
            The name of the character.
        """
        return self.name

    def get_health(self) -> int:
        """Gets the health of this character.

        Returns:
            The health of the character.
        """
        return self.health

    def reset_health(self) -> None:
        """Resets the health of this character to maximum."""
        self.health = 100

    def get_damage_ticks(self) -> int:
        """Returns the number of health points removed per round.

        Used when attacked by a Magic character.

        Returns:
            The number of health points removed per round.
        """
        return self.damage_per_round

    def increment_damage_ticks(self, value: int) -> None:
        """Increases the number of health points removed per round.

        Used when attacked by a Magic character.

        Args:
            value: The amount to increase by.
        """
        self.damage_per_round += value

    def reset_damage_ticks(self) -> None:
        """Resets the number of health points removed per round to 0."""
        self.damage_per_round = 0

    def is_dead(self) -> bool:
        """Determine if the character is dead.

        Returns:
            If the character is dead.
        """
        return self.health <= 0

    def take_damage(self, damage: int) -> None:
        """Reduces the health points of this character by a given amount.

        Used when attacked by a another character.

        Args:
            damage: The number of health points to remove.
        """
        self.health -= damage
        self.health = max(self.health, 0)

    def conservative_attack(self) -> int:
        """Generate the amount of damage to deal to the opponent character.

        Does the least amount of damage to the opponent, but does no harm
        to self.

        Returns:
            The amount of damage to deal to the opponent character.
        """
        return round(self.damage * uniform(0.4, 0.6))

    def balanced_attack(self) -> int:
        """Generate the amount of damage to deal to the opponent character.

        Does a medium amount of damage to the opponent, but does a little
        harm to self.

        Returns:
            The amount of damage to deal to the opponent character.
        """
        return round(self.damage * uniform(0.6, 0.8))

    def aggressive_attack(self) -> int:
        """Generate the amount of damage to deal to the opponent character.

        Does the most amount of damage to the opponent, but does medium
        harm to self.

        Returns:
            The amount of damage to deal to the opponent character.
        """
        return round(self.damage * uniform(0.8, 1))

    def attack(self, opponent, strength) -> Tuple[int, int]:
        """Calculates damage to deal to opponent and self. Then does the
        calculated damage.

        Returns:
            A tuple where the first element is the damage done to the opponent
            and the  second element is the damage done to self.
        """
        if strength == "agg":
            damage_opponent = self.aggressive_attack()
            damage_self = self.balanced_attack()
        elif strength == "bal":
            damage_opponent = self.balanced_attack()
            damage_self = self.conservative_attack()
        elif strength == "con":
            damage_opponent = self.conservative_attack()
            damage_self = 0
        opponent.take_damage(damage_opponent)
        self.take_damage(damage_self)
        return damage_opponent, damage_self


class Assault(Character):
    """Assault characters have do more damage each round."""

    @staticmethod
    def describe() -> str:
        """Generates a description of this class.

        Returns:
            A description of this class.
        """
        return "Assault Class: Does more damage... but that's about it really!"

    def __init__(self, name: str) -> None:
        super().__init__(name, 100, 30)


class Health(Character):
    """Health characters regain some of their health points each round."""

    @staticmethod
    def describe() -> str:
        """Generates a description of this class.

        Returns:
            A description of this class.
        """
        return "Health Class: Does average damage and heals over time."

    def __init__(self, name: str) -> None:
        super().__init__(name, 100, 20)

    def heal(self) -> int:
        """Regenerate some health.

        Returns:
            The number of health points regenerated.
        """
        regen = randint(5, 10)
        self.health += regen
        return regen


class Magic(Character):
    """Magic characters deal lasting damage each round."""

    @staticmethod
    def describe() -> str:
        """Generates a description of this class.

        Returns:
            A description of this class.
        """
        return "Magic class: Does little damage, but attacks cause lasting damage."  # pylint: disable=C0301

    def __init__(self, name: str) -> None:
        super().__init__(name, 100, 15)

    def attack(self, opponent, strength) -> Tuple[int, int]:
        """Calculates damage to deal to opponent and self. Then does the
        calculated damage.

        Returns:
            A tuple where the first element is the damage done to the opponent
            and the second element is the damage done to self.
        """
        damage_ticks = opponent.get_damage_ticks()
        if strength == "agg":
            damage_opponent = self.aggressive_attack() + damage_ticks
            opponent.increment_damage_ticks(3)
            damage_self = self.balanced_attack()
        elif strength == "bal":
            damage_opponent = self.balanced_attack() + damage_ticks
            opponent.increment_damage_ticks(2)
            damage_self = self.conservative_attack()
        elif strength == "con":
            damage_opponent = self.conservative_attack() + damage_ticks
            opponent.increment_damage_ticks(1)
            damage_self = 0
        opponent.take_damage(damage_opponent)
        self.take_damage(damage_self)
        return damage_opponent, damage_self
