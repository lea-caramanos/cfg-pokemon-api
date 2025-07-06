from api import pokeapi

# ==================================

# Choose pokemon options for player to pick from

def choose_pokemon(pokemons):
  print('')
  index = 1
  # For loop to print each pokemon's name & ID for player to choose
  for key in pokemons:
    print('> Pokemon option #',index,'= ID:',key['id'],'- NAME:',key['name'])
    index+=1
  choice = int(input("\nWhat is your choice (type the pokemon's id)? "))

  # For loop to save the chosen pokemon using its ID, compare each option to the choice ID imputed above
  for x in pokemons:
    if x['id'] == choice:
      break

  return x

# ==================================

# Get random pokemon
# If number = 1: one pokemon is directly assigned - DELETE?
# If number != 1: player can choose between randomly generated pokemons - DELETE?

def get_pokemon(number):
  if number == 1:
    pokemon = pokeapi.get_random_pokemon_api()
  elif number != 1:
    pokemons = []
    # For loop to retrieve data about pokemons and append to list
    for i in range(number):
      pokemons.append(pokeapi.get_random_pokemon_api())
    pokemon = choose_pokemon(pokemons)

  return pokemon

# ===================================

# Retrieve player & opponent's pokemon depending on game type
# If 'random': one pokemon randomly assigned to player - DELETE?
# If 'choice': player chooses between randomly generated pokemons - DELETE?

def assign_pokemons(type_game):
  
  # Player's pokemon is chosen based on game type
  if type_game == 'random':
    p_pokemon = get_pokemon(1)
  elif type_game == 'choice':
    number_options = int(input('How many pokemons do you want to choose from (between 2-5)? '))
    p_pokemon = get_pokemon(number_options)

  # Randomly generate opponent's pokemon and preventing pokemons being the same
  while True:
    o_pokemon = get_pokemon(1)
    if p_pokemon['id'] != o_pokemon['id']:
      break

  return p_pokemon, o_pokemon

# ==================================
