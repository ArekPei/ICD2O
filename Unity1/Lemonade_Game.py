import random

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
        expenses = glasses_of_lemonade * cost_of_production + advertising_signs * cost_of_advertising
        if price_per_glass == 0:
            revenue = price_per_glass * min(glasses_of_lemonade, (customers * 2)) + (advertising_signs / 100) * min(glasses_of_lemonade, (customers * 2))
        elif price_per_glass <= 1 and not price_per_glass == 0:
            revenue = price_per_glass * min(glasses_of_lemonade, (customers * 1.5)) + (advertising_signs / 100) * min(glasses_of_lemonade, (customers * 1.5))
        elif price_per_glass <= 3 and not price_per_glass == 0:
            revenue = price_per_glass * min(glasses_of_lemonade, (customers)) + (advertising_signs / 100) * min(glasses_of_lemonade, (customers * 1.25))
        
        daily_profit = revenue - expenses

        total_profit += daily_profit

        print(f"Day {day} Profit: ${daily_profit:.2f}")

    print(f"Total profit over {days} days: ${total_profit:.2f}")

if __name__ == "__main__":
    main()