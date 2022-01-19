import unittest

from guizero import Box, Picture, PushButton, Text, TextBox

from Driver import Driver
from Player import Player
from Widgets import Aligner, HoverablePushButton, Padding


# pylama:ignore=C0116
class DriverTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver(True)
        self.driver.game.set_players(Player("Player 1"), Player("Player 2"))
        self.driver.game.coin_toss("Heads")
        self.driver.game.get_current_player().choose_character("Assault", "")
        self.driver.game.swap_player()
        self.driver.game.get_current_player().choose_character("Health", "")
        Player.reset_available_characters()
        self.app = self.driver.app
        self.driver.clear_display()

    def tearDown(self):
        self.app.destroy()

    def test_clear_display(self):
        self.assertTrue(len(self.app.children) == 0)

    def test_render_sign_up(self):
        self.driver.render_sign_up()
        self.assertTrue(len(self.app.children) == 3)
        self.assertTrue(isinstance(self.app.children[0], Box))
        self.assertTrue(isinstance(self.app.children[1], Box))
        self.assertTrue(isinstance(self.app.children[2], Box))
        self.assertTrue(len(self.app.children[2].children) == 10)

        elements = self.app.children[2].children
        self.assertTrue(isinstance(elements[0], Box))
        self.assertTrue(isinstance(elements[1], Text))
        self.assertTrue(isinstance(elements[2], Box))
        self.assertTrue(isinstance(elements[3], Text))
        self.assertTrue(isinstance(elements[4], TextBox))
        self.assertTrue(isinstance(elements[5], Box))
        self.assertTrue(isinstance(elements[6], Text))
        self.assertTrue(isinstance(elements[7], TextBox))
        self.assertTrue(isinstance(elements[8], Box))
        self.assertTrue(isinstance(elements[9], PushButton))

    def test_render_coin_toss(self):
        self.driver.render_coin_toss()
        self.assertTrue(len(self.app.children) == 3)
        self.assertTrue(isinstance(self.app.children[0], Box))
        self.assertTrue(isinstance(self.app.children[1], Box))
        self.assertTrue(isinstance(self.app.children[2], Box))
        self.assertTrue(len(self.app.children[2].children) == 7)

        elements = self.app.children[2].children
        self.assertTrue(isinstance(elements[0], Box))
        self.assertTrue(isinstance(elements[1], Text))
        self.assertTrue(isinstance(elements[2], Text))
        self.assertTrue(isinstance(elements[3], Box))
        self.assertTrue(isinstance(elements[4], PushButton))
        self.assertTrue(isinstance(elements[5], Box))
        self.assertTrue(isinstance(elements[6], PushButton))

    def test_render_after_coin_toss(self):
        self.driver.render_after_coin_toss()
        self.assertTrue(len(self.app.children) == 3)
        self.assertTrue(isinstance(self.app.children[0], Box))
        self.assertTrue(isinstance(self.app.children[1], Box))
        self.assertTrue(isinstance(self.app.children[2], Box))
        self.assertTrue(len(self.app.children[2].children) == 2)

        elements = self.app.children[2].children
        self.assertTrue(isinstance(elements[0], Box))
        self.assertTrue(isinstance(elements[1], Text))

    def test_render_character_choice(self):
        self.driver.render_character_choice()
        self.assertTrue(len(self.app.children) == 3)
        self.assertTrue(isinstance(self.app.children[0], Box))
        self.assertTrue(isinstance(self.app.children[1], Box))
        self.assertTrue(isinstance(self.app.children[2], Box))
        self.assertTrue(len(self.app.children[2].children) == 16)

        elements = self.app.children[2].children
        self.assertTrue(isinstance(elements[0], Box))
        self.assertTrue(isinstance(elements[1], Text))
        self.assertTrue(isinstance(elements[2], Box))
        self.assertTrue(isinstance(elements[3], Text))
        self.assertTrue(isinstance(elements[4], TextBox))
        self.assertTrue(isinstance(elements[5], Box))
        self.assertTrue(isinstance(elements[6], Text))
        self.assertTrue(isinstance(elements[7], PushButton))
        self.assertTrue(isinstance(elements[8], Text))
        self.assertTrue(isinstance(elements[9], Box))
        self.assertTrue(isinstance(elements[10], PushButton))
        self.assertTrue(isinstance(elements[11], Text))
        self.assertTrue(isinstance(elements[12], Box))
        self.assertTrue(isinstance(elements[13], PushButton))
        self.assertTrue(isinstance(elements[14], Text))
        self.assertTrue(isinstance(elements[15], Box))

    def test_render_main_game(self):
        self.driver.render_main_game()
        self.assertTrue(len(self.app.children) == 3)
        self.assertTrue(isinstance(self.app.children[0], Box))
        self.assertTrue(isinstance(self.app.children[1], Box))
        self.assertTrue(isinstance(self.app.children[2], Box))
        self.assertTrue(len(self.app.children[2].children) == 18)

        elements = self.app.children[2].children
        self.assertTrue(isinstance(elements[0], Box))
        self.assertTrue(isinstance(elements[1], Text))
        self.assertTrue(isinstance(elements[2], Box))
        self.assertTrue(isinstance(elements[3], Text))
        self.assertTrue(isinstance(elements[4], Text))
        self.assertTrue(isinstance(elements[5], Text))
        self.assertTrue(isinstance(elements[6], Text))
        self.assertTrue(isinstance(elements[7], Picture))
        self.assertTrue(isinstance(elements[8], Picture))
        self.assertTrue(isinstance(elements[9], Box))
        self.assertTrue(isinstance(elements[10], PushButton))
        self.assertTrue(isinstance(elements[11], PushButton))
        self.assertTrue(isinstance(elements[12], PushButton))
        self.assertTrue(isinstance(elements[13], Box))
        self.assertTrue(isinstance(elements[14], Text))
        self.assertTrue(isinstance(elements[15], Box))
        self.assertTrue(isinstance(elements[16], Box))
        self.assertTrue(isinstance(elements[17], Box))

    def test_render_leaderboard(self):
        self.driver.render_leaderboard()
        self.assertTrue(len(self.app.children) == 3)
        self.assertTrue(isinstance(self.app.children[0], Box))
        self.assertTrue(isinstance(self.app.children[1], Box))
        self.assertTrue(isinstance(self.app.children[2], Box))
        self.assertTrue(len(self.app.children[2].children) == 6)

        elements = self.app.children[2].children
        self.assertTrue(isinstance(elements[0], Box))
        self.assertTrue(isinstance(elements[1], Text))
        self.assertTrue(isinstance(elements[2], Box))
        self.assertTrue(isinstance(elements[3], Box))
        self.assertTrue(isinstance(elements[4], Box))
        self.assertTrue(isinstance(elements[5], PushButton))


class WidgetsTest(unittest.TestCase):
    def setUp(self):
        self.driver = Driver(True)
        self.app = self.driver.app
        self.Aligner = Aligner(self.app, 1)
        self.HoverablePushButton = HoverablePushButton(self.app)
        self.Padding = Padding(self.app, 1)

    def tearDown(self):
        self.app.destroy()

    def test_button_hover(self):
        self.assertEqual(self.HoverablePushButton.widget.bg, HoverablePushButton.DEFAULT_COLOUR)  # pylint: disable=C0301
        self.HoverablePushButton.on_hover(None)
        self.assertEqual(self.HoverablePushButton.widget.bg, HoverablePushButton.HOVER_COLOUR)  # pylint: disable=C0301
        self.HoverablePushButton.off_hover(None)
        self.assertEqual(self.HoverablePushButton.widget.bg, HoverablePushButton.DEFAULT_COLOUR)  # pylint: disable=C0301

    def test_button_state(self):
        self.assertTrue(self.HoverablePushButton.widget.enabled)
        self.HoverablePushButton.disable()
        self.assertFalse(self.HoverablePushButton.widget.enabled)
        self.HoverablePushButton.enable()
        self.assertTrue(self.HoverablePushButton.widget.enabled)
