# Battle Game

[![Tests](https://github.com/Naeviant/Battle-Game/actions/workflows/tests.yml/badge.svg)](https://github.com/Naeviant/Battle-Game/actions/workflows/tests.yml)
[![Linting](https://github.com/Naeviant/Battle-Game/actions/workflows/linting.yml/badge.svg)](https://github.com/Naeviant/Battle-Game/actions/workflows/linting.yml)
[![Issues](https://img.shields.io/github/issues-search?label=Issues&logo=GitHub&query=repo%3ANaeviant%2FBattle-Game%20is%3Aopen)](https://img.shields.io/github/issues-search?label=Issues&logo=GitHub&query=repo%3ANaeviant%2FBattle-Game%20is%3Aopen)

My solution for the final project of the Digital People course, which requires learners to create a Pokemon-style fighting game.

### Gameplay

- Players will flip a virtual coin to decide who will go first.
- Players can name their own character and choose from one of three classes:
    - Assault Class: Does a lot of damage each round.
    - Health Class: Does an average amount of damage each round, but gradually replenishes its own health.
    - Magic Class: Does the least amount of damage, but attacks cause lasting damage.
- Players battle using one of three attack types:
    - Conservative Attack: Does a little damage to the opponent but does no damage to self.
    - Balanced Attack: Does a medium amount of damage to the opponent but does a little damage to self.
    - Aggressive Attack: Does a lot of damage to the opponent but does a medium amount of damage to self.
- Players play three rounds to determine a winner (rounds which result in draws are replayed).
- The winning player will get an extra point on the leaderboard. The top five entries on the leaderboard are shown at the end of each game.

### Code Features

- GUI included with guizero.
- Unit testing with over 90% coverage.
- Compliant with PEP8 styling guidelins.
- Compliant with PEP484 type hinting guidelines.

### Setup

Coming Soon


**Please Note:** This application is designed to be used in Replit as it uses ReplitDB. The application will otherwise run without saving the scoreboard.

### Support

If you have a question or discover a bug, please open an issue. There are currently no plans to add new features.

### License

> Copyright 2022, Sam Hirst

> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
