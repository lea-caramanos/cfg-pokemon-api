# ===================================

# Announce the results of the battle and retrieve data about winning pokemon
# Results for entire game are stored in a file

def announce_results(p_pokemon, o_pokemon, p_score, o_score, battle):
  print('\n----------------------------')
  print('--- Battle Final Results ---')
  print('----------------------------\n')

  draw = False

  if p_score > o_score:
    result = 'Congratulations, you have won the battle! 🏆'
    winning_pokemon = p_pokemon
    losing_pokemon = o_pokemon

  elif o_score > p_score:
    result = 'You fought well, but your opponent was stronger... 🥈'
    winning_pokemon = o_pokemon
    losing_pokemon = p_pokemon

  else:
    draw = True
    result = "What a battle! You were both equally strong, it's a draw. 🤝"

  print(result)

  # If not a draw, can retrieve all info
  if draw == False:
    with open('battles_results.txt', 'a+') as results_file:
      results_file.write('📝 Details for battle #')
      results_file.write(str(battle))
      results_file.write("\n")
      results_file.write(result)
      results_file.write("\nThe player's score is: ")
      results_file.write(str(p_score))
      results_file.write("\nThe opponent's score is: ")
      results_file.write(str(o_score))
      results_file.write("\nThe winning pokemon's name is: ")
      results_file.write(winning_pokemon['name'])
      results_file.write("\nThe losing pokemon's name is: ")
      results_file.write(losing_pokemon['name'])
      results_file.write("\n")
  # If draw, don't retrieve winning pokemon's info
  else:
    with open('battles_results.txt', 'a+') as results_file:
      results_file.write('📝 Details for battle #')
      results_file.write(str(battle))
      results_file.write("\n")
      results_file.write(result)
      results_file.write("\nThe player's score is: ")
      results_file.write(str(p_score))
      results_file.write("\nThe opponent's score is: ")
      results_file.write(str(o_score))
      results_file.write("\nThe player's pokemon is: ")
      results_file.write(p_pokemon['name'])
      results_file.write("\nThe opponent's pokemon is: ")
      results_file.write(o_pokemon['name'])
      results_file.write("\n")

# ===================================
