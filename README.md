# 🐍 Pokémon API Game (Python)

A Python project that demonstrates API integration and dynamic data handling using the [PokéAPI](https://pokeapi.co/). This command-line game retrieves, processes, and interacts with live Pokémon data to simulate battles — showcasing key data skills in a creative context.

## 🧠 Skills Demonstrated

- **Python programming**: Modular code structure with functions and conditionals.
- **API integration**: Fetching and handling live data from a public RESTful API.
- **JSON data handling**: Parsing and using nested JSON structures.
- **Data processing**: Managing user input, filtering responses, and generating outputs.
- **Command-line interaction**: Designing user-friendly CLI experiences.

## 📌 Features

- Fetches Pokémon data from PokéAPI.
- Option to choose your Pokémon or get one randomly assigned.
- Opponent gets a random Pokémon for a basic battle simulation.
- Fun, interactive command-line gameplay.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. You’ll also need the `requests` library:

```bash
pip install requests
```

### Clone the Repository

```bash
git clone https://github.com/lea-caramanos/cfg-pokemon-api.git
cd cfg-pokemon-api
```

### Run the Game

```bash
python main.py
```

## 📁 Folder/File Structure

- `main.py` – Script that runs the game. It imports from `game/`.

- `game/engine.py` – Core game logic: Pokémon assignment, game flow, etc.

- `game/api.py` – Functions for fetching Pokémon data from the PokéAPI.

## 🔧 Code Structure

- `get_random_pokemon_api()` – Fetches a random Pokémon from PokéAPI.

- `choose_pokemon()` – Lets the player pick from several random Pokémon.

- `get_pokemon(number)` – Assigns a Pokémon based on mode.

- `assign_pokemons(type_game)` – Assigns Pokémon to player and opponent.

## 🎮 Example Gameplay

```bash
> Pokemon option # 1 = ID: 7 - NAME: squirtle
> Pokemon option # 2 = ID: 25 - NAME: pikachu
> Pokemon option # 3 = ID: 150 - NAME: mewtwo

What is your choice (type the pokemon's id)? 25

You chose: Pikachu
Your opponent is: Charmander
```

## 📚 API Reference

- [PokéAPI](https://pokeapi.co/) – RESTful API with extensive Pokémon data.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.