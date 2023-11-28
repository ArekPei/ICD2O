import random

# Task 1: Pokemon Selection
def choose_pokemon():
    print("Welcome to the world of Pokemon! Choose your starter Pokemon:")
    print("1. Pikachu")
    print("2. Bulbasaur")
    print("3. Charmander")
    choice = int(input("Enter the number of your chosen Pokemon: "))
    if choice == 1:
        return "Pikachu"
    elif choice == 2:
        return "Bulbasaur"
    elif choice == 3:
        return "Charmander"
    else:
        print("Invalid choice. Please try again.")
        return choose_pokemon()

# Task 2: Game Introduction
def game_intro(player_pokemon):
    print(f"Welcome to the world of Pokemon, Trainer! You have chosen {player_pokemon} as your starter Pokemon.")
    print("Your journey to become a Pokemon Master begins now!")

# Task 3: Decision Making
def make_decision():
    decision = input("You encounter a wild Pokemon. Do you want to battle it or try to catch it? (battle/catch): ")
    if decision.lower() == "battle":
        return "battle"
    elif decision.lower() == "catch":
        return "catch"
    else:
        print("Invalid decision. Please try again.")
        return make_decision()

# Task 4: Pokemon Battle
def pokemon_battle(action, player_pokemon):
    if action == "battle":
        opponent_pokemon = random.choice(["Squirtle", "Bulbasaur", "Charmander"])
        print(f"You are battling a wild {opponent_pokemon} with your {player_pokemon}!")
        
        player_attack = random.randint(5, 15)  # Simulate player's attack damage
        opponent_attack = random.randint(5, 15)  # Simulate opponent's attack damage
        
        player_health = 100  # Set player's initial health
        opponent_health = 100  # Set opponent's initial health
        
        while player_health > 0 and opponent_health > 0:
            # Player's turn
            print(f"Your {player_pokemon} attacks the wild {opponent_pokemon}!")
            opponent_health -= player_attack
            print(f"The wild {opponent_pokemon}'s health: {opponent_health}")
            
            if opponent_health <= 0:
                print(f"You defeated the wild {opponent_pokemon}! Congratulations!")
                # Implement victory logic here
                break
            
            # Opponent's turn
            print(f"The wild {opponent_pokemon} counterattacks!")
            player_health -= opponent_attack
            print(f"Your {player_pokemon}'s health: {player_health}")
            
            if player_health <= 0:
                print(f"Your {player_pokemon} fainted! Game over.")
                # Implement defeat logic here
                break
    elif action == "catch":
        print("You are trying to catch the wild Pokemon...")
        catch_attempt = random.randint(1, 3)  # Simulate a catch attempt
        if catch_attempt == 1:
            print(f"You successfully caught the wild Pokemon with your {player_pokemon}!")
            # Implement catch success logic here
        else:
            print("Oh no! The wild Pokemon broke free!")
            # Implement catch failure logic here

# Task 5: Health Management
def manage_health(current_health, damage_taken):
    remaining_health = current_health - damage_taken
    if remaining_health <= 0:
        print("Your Pokemon fainted! Game over.")
        # End the game
    else:
        print(f"Your Pokemon's health: {remaining_health}")

# Task 1: Superhero Selection
def choose_superhero():
    print("Welcome to the Marvel universe! Choose your superhero:")
    print("1. Iron Man")
    print("2. Spider-Man")
    print("3. Captain America")
    choice = int(input("Enter the number of your chosen superhero: "))
    if choice == 1:
        return "Iron Man"
    elif choice == 2:
        return "Spider-Man"
    elif choice == 3:
        return "Captain America"
    else:
        print("Invalid choice. Please try again.")
        return choose_superhero()

# Task 2: Game Introduction
def game_intro2(player_superhero):
    print(f"Welcome, superhero! You have chosen {player_superhero} as your Marvel superhero.")
    print("The world is in danger, and it's up to you to save it!")

# Task 3: Decision Making
def make_decision2():
    decision = input("A supervillain is causing trouble. Do you want to confront the villain or seek assistance from another hero? (confront/seek): ")
    if decision.lower() == "confront":
        return "confront"
    elif decision.lower() == "seek":
        return "seek"
    else:
        print("Invalid decision. Please try again.")
        return make_decision()

# Task 4: Superhero Mission
def superhero_mission(action, player_superhero):
    if action == "confront":
        print(f"You, as {player_superhero}, are confronting the supervillain!")

        player_health = 100  # Set player's initial health
        villain_health = 100  # Set villain's initial health

        while player_health > 0 and villain_health > 0:
            # Player's turn
            player_choice = input("Choose your attack (e.g., punch, kick, special move): ")
            if player_choice == "punch":
                player_attack = random.randint(10, 15)  # Simulate player's punch attack damage
            elif player_choice == "kick":
                player_attack = random.randint(15, 20)  # Simulate player's kick attack damage
            elif player_choice == "special move":
                player_attack = random.randint(25, 30)  # Simulate player's special move attack damage
            else:
                print("Invalid attack choice. Please choose a valid attack.")
                continue  # Restart the loop to allow the player to choose a valid attack

            print(f"You, as {player_superhero}, attack the supervillain with {player_choice}!")
            villain_health -= player_attack
            print(f"The supervillain's health: {villain_health}")

            if villain_health <= 0:
                print("Congratulations! You defeated the supervillain!")
                # Implement victory logic here
                break

            # Villain's turn
            villain_attack = random.randint(15, 25)  # Simulate villain's attack damage
            print("The supervillain counterattacks!")
            player_health -= villain_attack
            print(f"Your superhero's health: {player_health}")

            if player_health <= 0:
                print(f"Your superhero, {player_superhero}, has been defeated! Game over.")
                # Implement defeat logic here
                break
    elif action == "seek":
        print(f"You, as {player_superhero}, are seeking assistance from another hero.")
        available_heroes = ["Thor", "Black Widow", "Hulk", "Doctor Strange"]  # List of available heroes
        team_up_hero = random.choice(available_heroes)
        print(f"You team up with {team_up_hero} to confront the supervillain!")

        combined_attack = random.randint(20, 30)  # Simulate combined attack damage
        villain_attack = random.randint(15, 25)  # Simulate villain's attack damage

        player_health = 100  # Set player's initial health
        team_up_hero_health = 120  # Set team-up hero's initial health
        villain_health = 150  # Set villain's initial health

        while player_health > 0 and team_up_hero_health > 0 and villain_health > 0:
            # Player's turn
            player_choice = input("Choose your attack (e.g., punch, kick, special move): ")
            if player_choice == "punch":
                player_attack = random.randint(10, 15)  # Simulate player's punch attack damage
            elif player_choice == "kick":
                player_attack = random.randint(15, 20)  # Simulate player's kick attack damage
            elif player_choice == "special move":
                player_attack = random.randint(25, 30)  # Simulate player's special move attack damage
            else:
                print("Invalid attack choice. Please choose a valid attack.")
                continue  # Restart the loop to allow the player to choose a valid attack

            print(f"You, as {player_superhero}, attack the supervillain with {player_choice}!")
            villain_health -= player_attack
            print(f"The supervillain's health: {villain_health}")

            if villain_health <= 0:
                print(f"Congratulations! You and {team_up_hero} defeated the supervillain!")
                # Implement victory logic here
                break

            # Villain's turn
            print("The supervillain counterattacks!")
            player_health -= villain_attack
            team_up_hero_health -= villain_attack
            print(f"Your superhero's health: {player_health}")
            print(f"{team_up_hero}'s health: {team_up_hero_health}")

            if player_health <= 0 and team_up_hero_health <= 0:
                print(f"Both you and {team_up_hero} have been defeated! Game over.")
                # Implement defeat logic here
                break
            elif player_health <= 0:
                print(f"Your superhero, {player_superhero}, has been defeated! Game over.")
                # Implement defeat logic here
                break
            elif team_up_hero_health <= 0:
                print(f"{team_up_hero} has been defeated! You must continue the battle alone.")
                # Implement logic for continuing the battle alone
                break

# Task 5: Health Management
def manage_health2(current_health, damage_taken):
    remaining_health = current_health - damage_taken
    if remaining_health <= 0:
        print("Your superhero has been defeated! Game over.")
        # End the game
    else:
        print(f"Your superhero's health: {remaining_health}")

gameMode = str(input("Please select the game mode(Pokemon/Superhero):"))
if gameMode == "Pokemon":   
    player_pokemon = choose_pokemon()
    game_intro(player_pokemon)
    decision = make_decision()
    pokemon_battle(decision, player_pokemon)
elif gameMode == "Superhero":
    player_superhero = choose_superhero()
    game_intro2(player_superhero)
    decision = make_decision2()
    superhero_mission(decision, player_superhero)
else:
    print("Invalid input, game over.")