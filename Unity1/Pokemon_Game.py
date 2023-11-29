import random

# Task 1: Pokemon Selection
def choose_pokemon():
    print('''Before you even start the game, I will need to introduce the mechanics of the game first:
In this game, the starting health of both you and your opponent is 100.
In this game, you will have four move options:
First one being a 1, which deals 5~10 points of damage, and causes 1 energy.
Second one is a 2, which deals 10~15 points of damage, and causes 2 energy.
Third one is a 3, which deals a random 5~30 points of damage, and causes 3 energy.
The last option is to defense, which will restore 2 energy, immune to damage on that round, restore 5 or 10 health points,
but your opponent will also restore 5 or 10 health points.
I would also need to talk about the Element reaction system.
As we all know, Pikachu is electric, Charmander is fire, Squirtle is water, and Bulbasaur is grass.
In this game, electric restrains water and deals a 5 extra damage to water, which will result in a "Electrify";
electric restrains grass and deals a 5 extra damage to grass, which will result in a "Intensify";
grass restrains water and deals a 5 extra damage to water, which will result in a "Burst";
fire restrains grass and deals a 10 extra damage to grass, which will result in a "Burn";
fire restrains electric and deals a 5 extra damage to electric, which will result in a "Overload";
water restrains fire and deals a 5 extra damage to fire, which will result in a "Evaporate".
If the player is being restrained, the defense move will restore more health for the player.
If the opponent is being restored, the defense move will restore more health for the opponent.
Also, if your attack damage goes beyond 20, the enemy can't attack at that round.
I wish you a good luck~''')
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
        if player_health > 100:
            player_health == 100
        elif opponent_health > 100:
            opponent_health == 100
        elif player_energy > 10:
            player_energy == 10

        while player_health > 0 and opponent_health > 0:
            # Player's turn
            player_choice = input("Choose your attack (1, 2, 3, defense): ")
            if player_choice == "1" and player_energy >=1:
                player_attack = random.randint(5, 10)  # Simulate player's 1 attack damage
                print(player_attack, "!!!")
                player_energy -= 1
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                    print("Element reaction: Electrify!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_attack += 5
                    print("Element reaction: Intensify!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                    print("Element reaction: Burst!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_attack += 10
                    print("Element reaction: Burn!")
                    print(player_attack, "!!!")
                opponent_health -= player_attack
            elif player_choice == "2" and player_energy >= 2:
                player_attack = random.randint(10, 15)  # Simulate player's 2 attack damage
                print(player_attack, "!!!")
                player_energy -= 2
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                    print("Element reaction: Electrify!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_attack += 5
                    print("Element reaction: Intensify!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                    print("Element reaction: Burst!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_attack += 10
                    print("Element reaction: Burn!")
                    print(player_attack, "!!!")
                opponent_health -= player_attack
            elif player_choice == "3" and player_energy >= 3:
                player_attack = random.randint(5, 30)  # Simulate player's 3 attack damage
                print(player_attack, "!!!")
                player_energy -= 3
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                    print("Element reaction: Electrify!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_attack += 5
                    print("Element reaction: Intensify!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_attack += 5
                    print("Element reaction: Burst!")
                    print(player_attack, "!!!")
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_attack += 10
                    print("Element reaction: Burn!")
                    print(player_attack, "!!!")
                opponent_health -= player_attack
            elif player_choice == "defense" and player_energy < 9 and player_health <= 95 and opponent_health <= 90:
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_energy += 2
                    player_health += 5
                    opponent_health += 10
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_energy += 2
                    player_health += 5
                    opponent_health += 10
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_energy += 2
                    player_health += 5
                    opponent_health += 10
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_energy += 2
                    player_health += 5
                    opponent_health += 10
            elif player_choice == "defense" and player_energy < 9 and player_health <= 90 and opponent_health <= 95:
                if player_pokemon == "Pikachu" and opponent_pokemon == "Charmander":
                    player_energy += 2
                    player_health += 10
                    opponent_health += 5
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Charmander":
                    player_energy += 2
                    player_health += 10
                    opponent_health += 5
                elif player_pokemon == "Charmander" and opponent_pokemon == "Squirtle":
                    player_energy += 2
                    player_health += 10
                    opponent_health += 5
            elif player_choice == "defense" and player_energy < 9 and player_health > 95 and opponent_health <= 90:
                if player_pokemon == "Pikachu" and opponent_pokemon == "Squirtle":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 10
                elif player_pokemon == "Pikachu" and opponent_pokemon == "Bulbasaur":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 10
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Squirtle":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 10
                elif player_pokemon == "Charmander" and opponent_pokemon == "Bulbasaur":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 10
            elif player_choice == "defense" and player_energy < 9 and player_health > 95 and opponent_health <= 95:
                if player_pokemon == "Pikachu" and opponent_pokemon == "Charmander":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 5
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Charmander":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 5
                elif player_pokemon == "Charmander" and opponent_pokemon == "Squirtle":
                    player_energy += 2
                    player_health == 100
                    opponent_health += 5
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
            if (player_attack < 20):
                print(f"The wild {opponent_pokemon} counterattacks!")
                opponent_attack = random.randint(15, 20)
                print(f"The wild {opponent_pokemon} deals {opponent_attack} points damage!")
                if player_pokemon == "Pikachu" and opponent_pokemon == "Charmander":
                    opponent_attack += 5
                    print("Element reaction: Overload! Enemy attack + 5!")
                elif player_pokemon == "Bulbasaur" and opponent_pokemon == "Charmander":
                    opponent_attack += 10
                    print("Element reaction: Burn! Enemy attack + 10!")
                elif player_pokemon == "Charmander" and opponent_pokemon == "Squirtle":
                    opponent_attack += 10
                    print("Element reaction: Evaporate! Enemy attack + 10!")
                player_health -= opponent_attack
                print(f"Your {player_pokemon}'s health: {player_health}, opponent's health: {opponent_health}, your {player_pokemon}'s energy level: {player_energy}.")
            else:
                print(f"Your {player_pokemon}'s health: {player_health}, opponent's health: {opponent_health}, your {player_pokemon}'s energy level: {player_energy}.")
            
            # Task 5: Health Management
            if player_health <= 0:
                print(f"Your {player_pokemon} fainted! Game over.")
                # Implement defeat logic here
                break
            elif opponent_health <= 0:
                print(f"You defeated the wild {opponent_pokemon}! Congratulations!")
                # Implement victory logic here
                break
            elif player_health <= 0 and opponent_health <= 0:
                print(f"Both your {player_pokemon} and the wild {opponent_pokemon} fainted! game over.")
                # Implement tie logic here

    elif action == "catch":
        print("You are trying to catch the wild Pokemon...")
        catch_attempt = random.randint(1, 2)  # Simulate a catch attempt
        if catch_attempt == 1:
            print(f"You successfully caught the wild Pokemon with your {player_pokemon}!")
            # Implement catch success logic here
        else:
            print("Oh no! The wild Pokemon broke free!")
            # Implement catch failure logic here

# Task 7: Game Completion
player_pokemon = choose_pokemon()
game_intro(player_pokemon)
decision = make_decision()
pokemon_battle(decision, player_pokemon)