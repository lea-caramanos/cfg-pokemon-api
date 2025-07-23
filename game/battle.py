import random

# ===================================

# Choose the stat played in round depending on the person choosing
# Player is decider no.1 and opponent no.2
# If player decides, he can input his choice
# If opponent decides, the stat is randomly generated using the list indexes

def stat_input():
  stat_decider = random.randint(1, 2)
  stats = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']

  if stat_decider == 1:
    print('Player will choose the stat.\n')
    print('The stats available to choose from are:', stats)
    stat = input('Which stat do you want to use? ').strip().lower()
    if stat not in stats:
      print("\nInvalid stat. 👋🏼 Exiting the game.")
      exit()
  else:
    print('Opponent will randomly choose the stat.')
    random_index = random.randint(1,len(stats))
    stat = stats[random_index - 1]

  print('\nThe chosen stat for the battle is:', stat)

  return stat

# ===================================

# Compare figures from chosen stat for the round
# Store the outcome in a string that can be referred in the battle

def compare_stat(p_pokemon, o_pokemon, stat):

  def get_stat_value(pokemon_data, stat_name):
        for s in pokemon_data["stats"]:
            if s["stat"]["name"] == stat_name:
                return s["base_stat"]
        return None  # Fallback if stat not found
  
  p_value = get_stat_value(p_pokemon, stat)
  o_value = get_stat_value(o_pokemon, stat)

  print(f"\nThe player stat value is:", p_value)
  print(f"The opponent stat value is:", o_value, "\n")

  if p_value > o_value:
    result = 'p'

  elif p_value < o_value:
    result = 'o'

  else:
    result = 'd'

  return result

# ===================================

# Set conditions of win/loss/draw

def pokemon_battle(p_pokemon, o_pokemon, rounds):
  rounds_played = 0

  # Set initial scores before battle
  p_score = 0
  o_score = 0

  # While loop to continue playing rounds until chosen number reached
  while(rounds_played < rounds):
    print('\n...............')
    print(f'... ROUND {rounds_played + 1} ...')
    print('...............\n')
    # Retrieve chosen stat (if 'exit', the game stops)
    stat = stat_input()

    if stat != 'exit':
      result = compare_stat(p_pokemon, o_pokemon, stat)
      rounds_played += 1
      if result == 'p':
        p_score += 1
        print('Congratulations, you won the round! 😄')
      elif result == 'o':
        o_score += 1
        print('Sorry, you lost the round... 😢')
      else:
        print("It's a draw. 😐")

      continue
    else:
      break

  return p_score, o_score

# ===================================
