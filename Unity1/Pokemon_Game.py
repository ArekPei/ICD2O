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

# Task 4: Pokemon Battle + Task 6: Element reaction
def pokemon_battle(action, player_pokemon):
    if action == "battle":
        opponent_pokemon = random.choice(["Squirtle", "Bulbasaur", "Charmander"])
        print(f"You are battling a wild {opponent_pokemon} with your {player_pokemon}!")
        
        player_health = 100  # Set player's initial health
        player_energy = 5 # Set player's energy level
        opponent_health = 100  # Set opponent's initial health

        while player_health > 0 and opponent_health > 0:
            # Player's turn
            player_choice = input("Choose your attack (e.g., punch, kick, special move, defense): ")
            if player_choice == "punch" and player_energy >=1:
                player_attack = random.randint(5, 10)  # Simulate player's punch attack damage
                player_energy -= 1
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_attack += 5
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_attack += 10
                opponent_health -= player_attack
            elif player_choice == "kick" and player_energy >= 2:
                player_attack = random.randint(10, 15)  # Simulate player's kick attack damage
                player_energy -= 2
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_attack += 5
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_attack += 10
                opponent_health -= player_attack
            elif player_choice == "special move" and player_energy >= 4:
                player_attack = random.randint(0, 30)  # Simulate player's special move attack damage
                player_energy -= 4
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_attack += 5
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_attack += 10
                opponent_health -= player_attack
            elif player_choice == "defense" and player_energy < 9:
                player_energy += 2
                opponent_health += 10
                print(f"You defensed yourself, your {player_pokemon}'s health: {player_health}, opponent's health: {opponent_health}, your {player_pokemon}'s energy level: {player_energy}.")
                continue
            else:
                print("Invalid attack choice. Please choose a valid attack.")
                continue  # Restart the loop to allow the player to choose a valid attack
            
            if opponent_health <= 0:
                print(f"You defeated the wild {opponent_pokemon}! Congratulations!")
                # Implement victory logic here
                break
            
            # Opponent's turn
            print(f"The wild {opponent_pokemon} counterattacks!")
            opponent_attack = random.randint(15, 20)
            if player_pokemon == "Pikachu" and opponent_pokemon == "Charmander":
                opponent_attack += 5
            elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Charmander":
                opponent_attack += 10
            elif player_pokemon == "Charmander" and opponent_pokemon == "Squirtle":
                opponent_attack += 5
            player_health -= opponent_attack
            print(f"Your {player_pokemon}'s health: {player_health}, opponent's health: {opponent_health}, your {player_pokemon}'s energy level: {player_energy}.")
            
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

# Task 7: Game Completion
player_pokemon = choose_pokemon()
game_intro(player_pokemon)
decision = make_decision()
pokemon_battle(decision, player_pokemon)