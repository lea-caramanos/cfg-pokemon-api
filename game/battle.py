import random

# ===================================

# Choose the stat played in round depending on the person choosing
# Player is decider no.1 and opponent no.2
# If player decides, he can input his choice
# If opponent decides, the stat is randomly generated using the list indexes

def stat_input():
  stat_decider = random.randint(1, 2)
  stats = ['id', 'height', 'weight', 'base_experience']

  if stat_decider == 1:
    print('Player will choose the stat.\n')
    print('The stats available to choose from are:', stats)
    stat = input('Which stat do you want to use? (or type "exit" to end) ')
  else:
    print('Opponent will randomly choose the stat.')
    random_index = random.randint(1,len(stats))
    stat = stats[random_index - 1]

  print('\nThe chosen stat for the battle is:', stat)

  return stat

# ===================================

# Compare figures from chosen stat for the round
# Store the outcome in a string that can be referred in the battle

def compare_stat(p_pokemon, o_pokemon, characteristic):
  print(f"\nThe player stat value is:", p_pokemon[characteristic])
  print(f"The opponent stat value is:", o_pokemon[characteristic], "\n")

  if p_pokemon[characteristic] > o_pokemon[characteristic]:
    result = 'p'

  elif p_pokemon[characteristic] < o_pokemon[characteristic]:
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
        print('Congratulations, you won the round! 🙂')
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
