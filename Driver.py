# pylint: disable=C0103
from guizero import App, Box, Picture, Text, TextBox

from Character import Assault, Health, Magic
from Game import Game
from Leaderboard import Leaderboard
from Player import Player
from Widgets import Aligner, HoverablePushButton, Padding


class Driver():
    """The main game driver.

    Controls the GUI components and overall flow of the game.
    """
    def __init__(self, under_test: bool = False) -> None:
        # Create Game and Leaderboard controllers
        self.game = Game()
        self.leaderboard = Leaderboard()

        # Create app widget
        self.app = App(title="Battle Game", bg="#333333")

        # Render sign up content
        self.render_sign_up()

        # Start GUI
        if not under_test:
            self.app.display()

    def clear_display(self) -> None:
        """Destroys all child widgets in the app."""
        while len(self.app.children) > 0:
            self.app.children[0].destroy()

    def render_sign_up(self) -> None:
        """Renders the player sign up page."""
        # Create container widget
        Aligner(self.app, width=20)
        Padding(self.app, 20)
        container = Box(self.app, width=460, height=460)
        container.bg = "white"
        # Create padding
        Padding(container, 70)
        # Create GUI widgets
        Text(container, text="Welcome to\nBattle Game!", size=36)
        Padding(container, 20)
        Text(container, "Player 1 Name:")
        player_1_name = TextBox(container, width=30)
        Padding(container, 20)
        Text(container, "Player 2 Name:")
        player_2_name = TextBox(container, width=30)
        Padding(container, 20)
        HoverablePushButton(
            container, 28, "Start Game", lambda: self.do_player_creation(
                player_1_name.value, player_2_name.value))

    def render_coin_toss(self) -> None:
        """Renders the coin toss page."""
        # Create container widget
        Aligner(self.app, width=20)
        Padding(self.app, 20)
        container = Box(self.app, width=460, height=460)
        container.bg = "white"
        # Create padding
        Padding(container, 125)
        # Construct text to render
        player_name = self.game.get_player_1().get_name()
        # Create GUI widgets
        Text(container, text=player_name, size=24)
        Text(container, text="Choose heads or tails to flip the coin.")
        Padding(container, 20)
        HoverablePushButton(container, 28, "Choose Heads",
                            lambda: self.do_coin_toss("Heads"))
        Padding(container, 20)
        HoverablePushButton(container, 28, "Choose Tails",
                            lambda: self.do_coin_toss("Tails"))

    def render_after_coin_toss(self) -> None:
        """Renders the text to display the coin toss result."""
        # Create container widget
        Aligner(self.app, width=20)
        Padding(self.app, 18)
        container = Box(self.app, width=460, height=460)
        container.bg = "white"
        # Create padding
        Padding(container, 200)
        # Create GUI widgets
        self.after_coin_toss = Text(container)

    def render_character_choice(self) -> None:
        """Renders the character selection screen."""
        # Create container widget
        Aligner(self.app, width=20)
        Padding(self.app, 18)
        container = Box(self.app, width=460, height=460)
        container.bg = "white"
        # Construct text to render
        player_name = self.game.get_current_player().get_name()
        # Create GUI widgets
        Padding(container,
                40 + (3 - len(Player.get_available_characters())) * 40)
        Text(container, text=player_name, size=24)
        Padding(container, 20)
        Text(container, text="Name Your Character:")
        character_name = TextBox(container, width=30)
        Padding(container, 20)
        Text(container, text="Choose Character Class:")
        if Assault in Player.get_available_characters():
            HoverablePushButton(container,
                                40,
                                text="Assault Class",
                                command=lambda: self.do_character_choice(
                                    "Assault", character_name.value))
            Text(container, text=Assault.describe().split(": ")[1], size=10)
            Padding(container, 20)
        if Health in Player.get_available_characters():
            HoverablePushButton(container,
                                40,
                                text="Health Class",
                                command=lambda: self.do_character_choice(
                                    "Health", character_name.value))
            Text(container, text=Health.describe().split(": ")[1], size=10)
            Padding(container, 20)
        if Magic in Player.get_available_characters():
            HoverablePushButton(container,
                                40,
                                text="Magic Class",
                                command=lambda: self.do_character_choice(
                                    "Magic", character_name.value))
            Text(container, text=Magic.describe().split(": ")[1], size=10)
            Padding(container, 20)

    def render_main_game(self) -> None:
        """Renders the main game screen."""
        # Create container widget
        Aligner(self.app, width=20)
        Padding(self.app, 18)
        container = Box(self.app, width=460, height=460, layout="grid")
        container.bg = "white"
        # Construct text to render
        character_1 = self.game.get_player_1().get_character()
        character_2 = self.game.get_player_2().get_character()
        header = f"{self.game.get_current_player().get_name()}'s Turn"
        player_1_header = character_1.get_name()
        player_2_header = character_2.get_name()
        player_1_hp = f"{character_1.get_health()} HP"
        player_2_hp = f"{character_2.get_health()} HP"
        # Create GUI widgets
        Padding(container, 30, grid=[0, 0, 3, 1])
        self.main_header = Text(container,
                                text=header,
                                size=24,
                                grid=[0, 1, 3, 1])
        Padding(container, 30, grid=[0, 2, 3, 1])
        Text(container, text=player_1_header, grid=[0, 3])
        Text(container, text=player_2_header, grid=[2, 3])
        Text(container, text=player_1_hp, grid=[0, 4])
        Text(container, text=player_2_hp, grid=[2, 4])
        Picture(container, image="assets/texture.png", grid=[0, 5])
        Picture(container, image="assets/texture.png", grid=[2, 5])
        Padding(container, 30, grid=[0, 6, 3, 1])
        self.con_attack = HoverablePushButton(container,
                                              11,
                                              "Conservative\nAttack",
                                              command=self.do_attack,
                                              args=["con"],
                                              grid=[0, 7])
        self.bal_attack = HoverablePushButton(container,
                                              11,
                                              "Balanced\nAttack",
                                              command=self.do_attack,
                                              args=["bal"],
                                              grid=[1, 7])
        self.agg_attack = HoverablePushButton(container,
                                              11,
                                              "Aggressive\nAttack",
                                              command=self.do_attack,
                                              args=["agg"],
                                              grid=[2, 7])
        Padding(container, 20, grid=[0, 8, 3, 1])
        self.sub_text = Text(container,
                             text="Press a button to begin the game.",
                             grid=[0, 9, 3, 1])
        Box(container, width=150, height=1, grid=[0, 10])
        Box(container, width=150, height=1, grid=[1, 10])
        Box(container, width=150, height=1, grid=[2, 10])

    def render_leaderboard(self) -> None:
        """Renders the leaderboard screen."""
        # Create container widget
        Aligner(self.app, width=20)
        Padding(self.app, 18)
        container = Box(self.app, width=460, height=460)
        container.bg = "white"
        # Create GUI widgets
        Padding(container, 20)
        Text(container, text="Leaderboard", size=24)
        Padding(container, 110)
        leaderboard_text = Box(container, layout="grid")
        Padding(container, 110)
        HoverablePushButton(container, 20, "New Game", self.handle_new_game)

        # Populate leaderboard
        for index, row in enumerate(self.leaderboard.get_data()):
            Text(leaderboard_text, text=row[0], width=10, grid=[0, index])
            Text(leaderboard_text, text=row[1], width=10, grid=[1, index])

    def do_player_creation(self, player_1, player_2) -> None:
        """Handles button presses on sign up screen."""
        # If a player didn't choose a name, set a default
        player_1 = "Player 1" if player_1 == "" else player_1
        player_2 = "Player 2" if player_2 == "" else player_2

        # Assign players to the game
        self.game.set_players(Player(player_1), Player(player_2))

        # Change GUI
        self.clear_display()
        self.render_coin_toss()

    def do_coin_toss(self, choice) -> None:
        """Handles button presses on coin toss screen."""
        # Do coin flip
        outcome = self.game.coin_toss(choice)

        # Change GUI
        self.clear_display()
        self.render_after_coin_toss()

        # Set text on GUI to coin flip result
        text = f"The result was {outcome}.\n\nLoading Game..."
        self.after_coin_toss.value = text

        # Change GUI after 3 seconds
        self.after_coin_toss.after(
            3000,
            lambda: [self.clear_display(),
                     self.render_character_choice()])

    def do_character_choice(self, choice, name) -> None:
        """Handles button presses on character selection screen."""
        # If no choice was made, do not proceed
        if choice == "":
            return

        # If no character name was entered, use the class name
        name = choice if name == "" else name

        # Make character selection in game engine
        self.game.get_current_player().choose_character(choice, name)

        # Change to next player turn
        self.game.swap_player()

        # Change GUI
        self.clear_display()
        if self.game.get_current_player().get_character() is None:
            self.render_character_choice()
        else:
            self.render_main_game()

    def do_attack(self, strength) -> None:
        """Handles button presses during gameplay."""
        # Do attack
        damage_opponent, damage_self = self.game.get_current_player(
        ).get_character().attack(
            self.game.get_opponent_player().get_character(), strength)
        # Update subtext
        player_name = self.game.get_current_player().get_character().get_name()
        info = f"{player_name} dealt {damage_opponent}"
        if damage_self > 0:
            info += f", but suffered {damage_self}."
        else:
            info += "."
        # Change to next player turn
        self.game.swap_player()
        # Regenerate GUI
        self.clear_display()
        self.render_main_game()
        self.sub_text.value = info
        self.handle_end_game()

    def handle_end_game(self) -> None:
        """Handles actions when a character dies during gameplay."""
        # Detect end of round
        if self.game.is_round_over():
            self.con_attack.disable()
            self.bal_attack.disable()
            self.agg_attack.disable()

            # Determine winner of game
            player_1 = self.game.get_player_1()
            player_2 = self.game.get_player_2()
            if player_1.get_character().is_dead(
            ) and self.game.get_player_2().get_character().is_dead():
                self.main_header.value = "It's a Draw."
                draw = True
            elif self.game.get_player_2().get_character().is_dead():
                self.main_header.value = f"{player_1.get_name()} Wins!"
                self.game.register_round_winner(player_1)
                draw = False
            elif self.game.get_player_1().get_character().is_dead():
                self.main_header.value = f"{player_2} Wins!"
                self.game.register_round_winner(player_2)
                draw = False

            # Detect end of game
            if self.game.is_game_over():
                # Add winner to leaderboard
                self.leaderboard.new_entry(
                    self.game.get_game_winner().get_name())
                # Change GUI
                self.main_header.after(
                    3000,
                    lambda: [self.clear_display(),
                             self.render_leaderboard()])
            else:
                # Change round
                self.game.next_round(draw)
                # Change GUI
                self.main_header.after(
                    3000,
                    lambda: [self.clear_display(),
                             self.render_main_game()])

    def handle_new_game(self) -> None:
        """Handles new game button presses on leaderboard screen."""
        self.app.destroy()
        Player.reset_available_characters()
        self.__init__()
