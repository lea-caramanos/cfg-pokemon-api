from game.api import get_random_pokemon_api

def choose_pokemon(pokemons):
    print('')
    for index, pokemon in enumerate(pokemons, start=1):
        print(f"> Pokemon option #{index} = ID: {pokemon['id']} - NAME: {pokemon['name']}")
    
    choice = int(input("\nWhat is your choice (type the pokemon's id)? "))
    
    for pokemon in pokemons:
        if pokemon['id'] == choice:
            return pokemon

def get_pokemon(mode):
    if mode == "choose":
        pokemons = [get_random_pokemon_api() for _ in range(3)]
        return choose_pokemon(pokemons)
    else:
        return get_random_pokemon_api()

def assign_pokemons(game_type):
    player = get_pokemon(game_type)
    opponent = get_random_pokemon_api()
    return player, opponent
