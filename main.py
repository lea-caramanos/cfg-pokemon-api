from game.engine import assign_pokemons
from game.api import get_random_pokemon_api

def main():
    print("Welcome to the Pokémon Battle Game!\n")

    game_type = input("Do you want to choose your Pokémon or get a random one? (choose/random): ").lower()
    if game_type not in ["choose", "random"]:
        print("Invalid input. Defaulting to random.")
        game_type = "random"

    player, opponent = assign_pokemons(game_type)

    print(f"\nYou chose: {player['name'].capitalize()}")
    print(f"Your opponent is: {opponent['name'].capitalize()}")

if __name__ == "__main__":
    main()
