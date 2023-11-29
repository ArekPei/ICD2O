import random

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
def game_intro(player_superhero):
    print(f"Welcome, superhero! You have chosen {player_superhero} as your Marvel superhero.")
    print("The world is in danger, and it's up to you to save it!")

# Task 3: Decision Making
def make_decision():
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

        villain_attack = random.randint(15, 25)  # Simulate villain's attack damage

        player_health = 100  # Set player's initial health
        team_up_hero_health = 100  # Set team-up hero's initial health
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

            print(f"You, as {team_up_hero}, attack the supervillain with {player_choice}!")
            villain_health -= player_attack
            print(f"The supervillain's health: {villain_health}")

            if villain_health <= 0:
                print(f"Congratulations! You and {team_up_hero} defeated the supervillain!")
                # Implement victory logic here
                break

            # Villain's turn
            print("The supervillain counterattacks!")
            team_up_hero_health -= villain_attack
            player_health -= villain_attack / 2
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
                break

# Task 5: Health Management
def manage_health2(current_health, damage_taken):
    remaining_health = current_health - damage_taken
    if remaining_health <= 0:
        print("Your superhero has been defeated! Game over.")
        # End the game
    else:
        print(f"Your superhero's health: {remaining_health}")

# Task 7: Game Completion
player_superhero = choose_superhero()
game_intro(player_superhero)
decision = make_decision()
superhero_mission(decision, player_superhero)