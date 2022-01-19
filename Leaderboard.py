# pylint: disable=C0103
from typing import List, Union
from replit import db


if db is None:
    db = {}


class Leaderboard():
    """A controller for the leaderboard - handles getting existing
    entries and adding new ones."""

    def __init__(self, collection: str = "scoreboard") -> None:
        self.collection = collection
        if db.get(self.collection, None) is None:
            try:
                db.set(self.collection, [])
            except AttributeError:
                db[self.collection] = []

    def new_entry(self, player_name: str) -> None:
        """Add a new entry to the leaderboard. If the player is already
        on the leaderboard, there are given an additional point. Otherwise,
        they will be added with a score of 1.

        Args:
            player_name: The name of the player to be added.
        """
        existing_names = list(
            map(lambda x: x["name"], db.get(self.collection, [])))
        if player_name in existing_names:
            index = existing_names.index(player_name)
            db.get(self.collection, [])[index]["score"] += 1
        else:
            db.get(self.collection, []).append({
                "name": player_name,
                "score": 1
            })

    def get_data(self) -> List[Union[str, int]]:
        """Gets the current scoreboard data as a list of lists, where the first
        element in the sub list is the player's name and the second element is
        the player's score. The list is sorted with the highest scores coming
        first.

        Returns:
            The leaderboard data.
        """
        data = sorted(map(lambda x: [x["name"], x["score"]],
                          db.get(self.collection, [])),
                      key=lambda x: x[1],
                      reverse=True)
        if len(data) < 6:
            return data
        return data[:5]

    def clear_data(self) -> None:
        """Removes all data from the scoreboard."""
        try:
            db.set(self.collection, None)
        except AttributeError:
            db[self.collection] = None
