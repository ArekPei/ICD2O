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

def calculate_customers(weather, temp):
    if weather == "sunny":
        if temp == "hot":
            return random.randint(50, 70)
        elif temp == "warm":
            return random.randint(30, 50)
        elif temp == "cold":
            return random.randint(20, 40)
        elif temp == "freezing":
            return random.randint(10, 30)
    elif weather == "cloudy":
            if temp == "hot":
                return random.randint(40, 60)
            elif temp == "warm":
                return random.randint(20, 40)
            elif temp == "cold":
                return random.randint(10, 30)
            elif temp == "freezing":
                return random.randint(5, 20)
    elif weather == "rainy":
        if temp == "hot":
            return random.randint(50, 70)
        elif temp == "warm":
            return random.randint(25, 45)
        elif temp == "cold":
            return random.randint(10, 30)
        elif temp == "freezing":
            return random.randint(0, 10)

def main():
    print('''Before you even start the game, I will need to introduce the mechanics of the game first:
The weather conditions are "sunny," "cloudy," and "rainy."
The temperature conditions are "hot," "warm," "cold," and "freezing."
The number of potential customers will depend on both the weather and the temperature. Warmer temperatures generally attract more customers, while colder temperatures may reduce the number of potential customers.
You will be simulating the lemonade stand business for a specific number of days that you will input at the beginning of the game.
For each day, you will receive the weather forecast and the temperature, and you will need to make decisions based on this information.
You will be asked to input the following for each day:
The number of glasses of lemonade to make.
The number of advertising signs to use.
The cost of lemonade per glass.
The program will calculate your profit based on the decisions you make and the weather conditions for each day.
Your profit will be influenced by the number of potential customers, your pricing strategy, and your expenses for production and advertising.
After simulating the specified number of days, the program will display the daily profit for each day and the total profit over the simulated days.
You can experiment with different pricing strategies for each weather condition and observe how it affects your profit.
Have fun''')
    days = int(input("How many days do you want to simulate:"))  # Number of days to simulate
    total_profit = 0

    for day in range(1, days + 1):
        weather = random.choices(["sunny", "cloudy", "rainy"], weights=[0.4, 0.3, 0.3])[0]
        temp = random.choices(["hot", "warm", "cold", "freezing"], weights=[0.4, 0.3, 0.3, 0.2])[0]
        customers = calculate_customers(weather, temp)

        print(f"Day {day}: Weather forecast - {weather} - {temp}")

        # Ask the player to make decisions
        glasses_of_lemonade = int(input("Enter the number of glasses of lemonade to make: "))
        advertising_signs = int(input("Enter the number of advertising signs to use: "))
        price_per_glass = float(input("Enter the cost of lemonade per glass: "))

        # Calculate profit based on the player's decisions and the weather condition
        # For simplicity, let's assume a fixed cost of production per glass
        cost_of_production = 1  # Cost of production per glass
        cost_of_advertising = 1 # Cost of production per sign
        revenue = price_per_glass * min(glasses_of_lemonade, customers)
        if price_per_glass == 0:
            expenses = glasses_of_lemonade * cost_of_production + advertising_signs * cost_of_advertising * 5
        elif price_per_glass <= 1 and not price_per_glass == 0:
            expenses = glasses_of_lemonade * cost_of_production + advertising_signs * cost_of_advertising * 2
        elif price_per_glass <= 3 and not price_per_glass == 0:
            expenses = glasses_of_lemonade * cost_of_production + advertising_signs * cost_of_advertising * 1.5
        else:
            expenses = glasses_of_lemonade * cost_of_production + advertising_signs * cost_of_advertising * 1.5
        
        daily_profit = revenue - expenses

        total_profit += daily_profit

        print(f"Day {day} Profit: ${daily_profit:.2f}")

    print(f"Total profit over {days} days: ${total_profit:.2f}")

gameMode = str(input("Please select the game mode(Pokemon/Superhero/Lemonade):"))
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
elif gameMode == "Lemonade":
    main()
else:
    print("Invalid input, game over.")