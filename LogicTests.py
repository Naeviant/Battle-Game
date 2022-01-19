import unittest

from Character import Character, Assault, Health, Magic
from Game import Game
from Leaderboard import Leaderboard
from Player import Player


# pylama:ignore=C0116
class TestCharacter(unittest.TestCase):
    CHARACTER_NAME = "Character"
    CHARACTER_HEALTH = 100
    CHARACTER_DAMAGE = 20

    def setUp(self):
        self.character = Character(TestCharacter.CHARACTER_NAME,
                                   TestCharacter.CHARACTER_HEALTH,
                                   TestCharacter.CHARACTER_DAMAGE)

    def test_name_getter(self):
        self.assertEqual(self.character.get_name(),
                         TestCharacter.CHARACTER_NAME)

    def test_health_getter(self):
        self.assertEqual(self.character.get_health(),
                         TestCharacter.CHARACTER_HEALTH)

    def test_is_dead(self):
        self.assertFalse(self.character.is_dead())
        self.character.take_damage(TestCharacter.CHARACTER_HEALTH)
        self.assertTrue(self.character.is_dead())

    def test_damage_ticks(self):
        self.assertEqual(self.character.get_damage_ticks(), 0)
        self.character.increment_damage_ticks(3)
        self.assertEqual(self.character.get_damage_ticks(), 3)

    def test_take_damage(self):
        self.character.take_damage(10)
        self.assertEqual(self.character.get_health(),
                         TestCharacter.CHARACTER_HEALTH - 10)

    def test_negative_health_prevention(self):
        self.character.take_damage(110)
        self.assertEqual(self.character.get_health(), 0)

    def test_conservative_attack(self):
        opponent = Character("Opponent", 100, 20)
        attack = self.character.attack(opponent, "con")
        self.assertGreaterEqual(attack[0],
                                TestCharacter.CHARACTER_DAMAGE * 0.4)
        self.assertLessEqual(attack[0], TestCharacter.CHARACTER_DAMAGE * 0.6)
        self.assertEqual(attack[1], 0)

    def test_balanced_attack(self):
        opponent = Character("Opponent", 100, 20)
        attack = self.character.attack(opponent, "bal")
        self.assertGreaterEqual(attack[0],
                                TestCharacter.CHARACTER_DAMAGE * 0.6)
        self.assertLessEqual(attack[0], TestCharacter.CHARACTER_DAMAGE * 0.8)
        self.assertGreaterEqual(attack[1],
                                TestCharacter.CHARACTER_DAMAGE * 0.4)
        self.assertLessEqual(attack[1], TestCharacter.CHARACTER_DAMAGE * 0.6)

    def test_aggressive_attack(self):
        opponent = Character("Opponent", 100, 20)
        attack = self.character.attack(opponent, "agg")
        self.assertGreaterEqual(attack[0],
                                TestCharacter.CHARACTER_DAMAGE * 0.8)
        self.assertLessEqual(attack[0], TestCharacter.CHARACTER_DAMAGE)
        self.assertGreaterEqual(attack[1],
                                TestCharacter.CHARACTER_DAMAGE * 0.6)
        self.assertLessEqual(attack[1], TestCharacter.CHARACTER_DAMAGE * 0.8)


class TestAssault(unittest.TestCase):
    DESCRIPTION = "Assault Class: Does more damage... but that's about it really!"  # pylint: disable=C0301

    def test_description(self):
        self.assertEqual(Assault.describe(), TestAssault.DESCRIPTION)


class TestHealth(unittest.TestCase):
    DESCRIPTION = "Health Class: Does average damage and heals over time."
    CHARACTER_NAME = "Character"

    def setUp(self):
        self.character = Health(TestCharacter.CHARACTER_NAME)

    def test_description(self):
        self.assertEqual(Health.describe(), TestHealth.DESCRIPTION)

    def test_heal(self):
        self.character.take_damage(20)
        self.character.heal()
        self.assertGreaterEqual(self.character.get_health(), 85)
        self.assertLessEqual(self.character.get_health(), 90)


class TestMagic(unittest.TestCase):
    DESCRIPTION = "Magic class: Does little damage, but attacks cause lasting damage."  # pylint: disable=C0301
    CHARACTER_NAME = "Character"

    def setUp(self):
        self.character = Magic(TestMagic.CHARACTER_NAME)

    def test_description(self):
        self.assertEqual(Magic.describe(), TestMagic.DESCRIPTION)

    def test_conservative_attack(self):
        opponent = Character("Opponent", 100, 20)
        self.character.attack(opponent, "con")
        self.assertEqual(opponent.get_damage_ticks(), 1)

    def test_balanced_attack(self):
        opponent = Character("Opponent", 100, 20)
        self.character.attack(opponent, "bal")
        self.assertEqual(opponent.get_damage_ticks(), 2)

    def test_aggressive_attack(self):
        opponent = Character("Opponent", 100, 20)
        self.character.attack(opponent, "agg")
        self.assertEqual(opponent.get_damage_ticks(), 3)


class TestPlayer(unittest.TestCase):
    PLAYER_NAME = "Player 1"

    def setUp(self):
        self.player = Player(TestPlayer.PLAYER_NAME)
        Player.reset_available_characters()

    def test_name_getter(self):
        self.assertEqual(self.player.get_name(), TestPlayer.PLAYER_NAME)

    def test_available_characters(self):
        self.assertTrue(Assault in Player.get_available_characters())
        self.assertTrue(Health in Player.get_available_characters())
        self.assertTrue(Magic in Player.get_available_characters())

    def test_reset_available_characters(self):
        self.player.choose_character("Assault", None)
        Player.reset_available_characters()
        self.assertTrue(Assault in Player.get_available_characters())
        self.assertTrue(Health in Player.get_available_characters())
        self.assertTrue(Magic in Player.get_available_characters())

    def test_choose_assault(self):
        result = self.player.choose_character("Assault", None)
        self.assertTrue(result)
        self.assertTrue(Assault not in Player.get_available_characters())
        self.assertTrue(Health in Player.get_available_characters())
        self.assertTrue(Magic in Player.get_available_characters())
        self.assertTrue(isinstance(self.player.get_character(), Assault))

    def test_choose_health(self):
        result = self.player.choose_character("Health", None)
        self.assertTrue(result)
        self.assertTrue(Assault in Player.get_available_characters())
        self.assertTrue(Health not in Player.get_available_characters())
        self.assertTrue(Magic in Player.get_available_characters())
        self.assertTrue(isinstance(self.player.get_character(), Health))

    def test_choose_magic(self):
        result = self.player.choose_character("Magic", None)
        self.assertTrue(result)
        self.assertTrue(Assault in Player.get_available_characters())
        self.assertTrue(Health in Player.get_available_characters())
        self.assertTrue(Magic not in Player.get_available_characters())
        self.assertTrue(isinstance(self.player.get_character(), Magic))

    def test_choose_invalid(self):
        result = self.player.choose_character("", None)
        self.assertFalse(result)
        self.assertTrue(Assault in Player.get_available_characters())
        self.assertTrue(Health in Player.get_available_characters())
        self.assertTrue(Magic in Player.get_available_characters())
        self.assertEqual(self.player.get_character(), None)


class TestGame(unittest.TestCase):
    PLAYER_1_NAME = "Player 1"
    PLAYER_2_NAME = "Player 2"

    def setUp(self):
        self.game = Game()
        self.player_1 = Player(TestGame.PLAYER_1_NAME)
        self.player_2 = Player(TestGame.PLAYER_2_NAME)
        self.player_1.choose_character("Assault", "")
        self.player_2.choose_character("Health", "")
        Player.reset_available_characters()

    def test_player_1_getter(self):
        self.assertEqual(self.game.get_player_1(), None)

    def test_player_2_getter(self):
        self.assertEqual(self.game.get_player_2(), None)

    def test_player_setter(self):
        self.game.set_players(self.player_1, self.player_2)
        self.assertEqual(self.game.get_player_1(), self.player_1)
        self.assertEqual(self.game.get_player_2(), self.player_2)

    def test_coin_toss(self):
        self.game.set_players(self.player_1, self.player_2)
        for _ in range(100):
            coin = self.game.coin_toss("Heads")
            self.assertTrue(coin in ["Heads", "Tails"])
            if coin == "Heads":
                self.assertEqual(self.game.get_current_player(), self.player_1)
                self.assertEqual(self.game.get_opponent_player(),
                                 self.player_2)
            else:
                self.assertEqual(self.game.get_current_player(), self.player_2)
                self.assertEqual(self.game.get_opponent_player(),
                                 self.player_1)

    def test_turn_taking(self):
        self.game.set_players(self.player_1, self.player_2)
        self.game.coin_toss("Heads")
        for _ in range(100):
            if self.game.get_current_player() == self.player_1:
                self.game.swap_player()
                self.assertEqual(self.game.get_current_player(), self.player_2)
            else:
                self.game.swap_player()
                self.assertEqual(self.game.get_current_player(), self.player_1)

    def test_winner_calculation(self):
        self.game.set_players(self.player_1, self.player_2)
        self.game.coin_toss("Heads")
        self.assertEqual(self.game.get_game_winner(), None)
        self.game.register_round_winner(self.player_1)
        self.assertEqual(self.game.get_game_winner(), self.game.get_player_1())
        self.game.register_round_winner(self.player_2)
        self.assertEqual(self.game.get_game_winner(), None)
        self.game.register_round_winner(self.player_2)
        self.assertEqual(self.game.get_game_winner(), self.game.get_player_2())

    def test_is_round_over(self):
        self.assertFalse(self.game.is_round_over())

        self.game.set_players(self.player_1, self.player_2)
        self.game.coin_toss("Heads")
        self.assertFalse(self.game.is_round_over())

        self.game.get_player_1().get_character().take_damage(100)
        self.assertTrue(self.game.is_round_over())

    def test_is_game_over(self):
        self.game.set_players(self.player_1, self.player_2)
        self.game.coin_toss("Heads")
        self.assertFalse(self.game.is_game_over())

        self.game.next_round(False)
        self.game.next_round(False)
        self.game.get_player_1().get_character().take_damage(100)
        self.assertTrue(self.game.is_game_over())


class LeaderboardTest(unittest.TestCase):
    def setUp(self):
        self.leaderboard = Leaderboard("test")
        self.leaderboard.new_entry("Player 1")
        self.leaderboard.new_entry("Player 1")
        self.leaderboard.new_entry("Player 2")
        self.leaderboard.new_entry("Player 3")

    def test_leaderboard(self):
        scoreboard = self.leaderboard.get_data()
        self.assertTrue(len(scoreboard) == 3)
        for row in scoreboard:
            if row[0] == "Player 1":
                self.assertEqual(row[1], 2)
            elif row[0] == "Player 2" or row[0] == "Player 3":
                self.assertEqual(row[1], 1)
        self.assertFalse("Player 4" in list(map(lambda x: x[0], scoreboard)))

    def test_leaderboard_size(self):
        self.assertLessEqual(len(self.leaderboard.get_data()), 5)
        self.leaderboard.new_entry("Player 4")
        self.leaderboard.new_entry("Player 5")
        self.leaderboard.new_entry("Player 6")
        self.leaderboard.new_entry("Player 7")
        self.assertLessEqual(len(self.leaderboard.get_data()), 5)

    def tearDown(self):
        self.leaderboard.clear_data()
