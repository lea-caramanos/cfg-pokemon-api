from game import logic, battle, results

# ==== MAIN PROGRAM =====

# As a new game starts, delete the existing content of the file
with open('battles_results.txt', 'w+') as results_file:
    results_file.write('\n')

print('\n===========================================')
print('==== ⚔️  WELCOME TO THE POKEMON GAME ⚔️  ====')
print('===========================================\n')

battles = 1
while(True):
    print('----------------------------')   
    print('---- Pokemon Battle #',battles,'----')
    print('----------------------------')

    game_type_text = (
        "\nType of games available:\n"
        "- 'random': A random Pokemon will be assigned to you and your opponent.\n"
        "- 'choice': You will choose your Pokemon from a list of randomly generated options.\n"
        "\nEnter your preferred game type: "
    )

    game_type = input(game_type_text).strip().lower()
    if game_type not in ['random', 'choice']:
        print("\nInvalid game type. Defaulting to 'random'.")
        game_type = 'random'

    player_pokemon, opponent_pokemon = logic.assign_pokemons(game_type)

    print(f"\nThe player's pokemon name is: {player_pokemon['name']} 🦖")
    print(f"The opponent's pokemon name is: {opponent_pokemon['name']} 🦕")

    # Define the number of rounds to be played
    number_rounds = int(input('\nHow many number of rounds? (between 3-7, an even number can result in a draw): '))

    # Pokemons go to battle for a specific number of rounds
    # Results are returned and set to '_score' variables
    player_score, opponent_score = battle.pokemon_battle(player_pokemon, opponent_pokemon, number_rounds)

    # Announce results of the battle
    results.announce_results(player_pokemon, opponent_pokemon, player_score, opponent_score, battles)

    # Player chooses whether to play again
    print('\n============================')
    play_again = input('\nDo you want to play another game? (y/n) ')

    if play_again == 'y':
        battles += 1
    # If no more battles, results are stored in file for the game and displayed
    elif play_again == 'n':
        with open('battles_results.txt', 'r') as results_file:
            battles_outcome = results_file.read()

            print(battles_outcome)
        break
        