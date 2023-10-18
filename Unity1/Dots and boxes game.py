name = str(input("What is your name?"))
# Name Of Opponent; Armaan
noo_1 = str(input("Who is your opponent for the first game?"))
# Number of boxes you created; 28
nby_1 = int(input("How many boxes did you create in the first game?"))
# Number of boxes opponent created
nbo_1 = int(input("How many boxes did your opponent create in the first game?"))
# Number of grids
nog_1 = int(input("How much grids are there in the first game?"))

noo_2 = str(input("Who is your opponent for the second game?"))
# Kainen
nby_2 = int(input("How many boxes did you create in the second game?"))
# 15
nbo_2 = int(input("How many boxes did your opponent create in the second game?"))
# 34
nog_2 = int(input("How much grids are there in the second game?"))

noo_3 = str(input("Who is your opponent for the third game?"))
# Cameron
nby_3 = int(input("How many boxes did you create in the third game?"))
# 35
nbo_3 = int(input("How many boxes did your opponent create in the third game?"))
# 14
nog_3 = int(input("How much grids are there in the third game?"))

noo_4 = str(input("Who is your opponent for the fourth game?"))
nby_4 = int(input("How many boxes did you create in the fourth game?"))
nbo_4 = int(input("How many boxes did your opponent create in the fourth game?"))
nog_4 = int(input("How much grids are there in the fourth game?"))

noo_5 = str(input("Who is your opponent for the fifth game?"))
nby_5 = int(input("How many boxes did you create in the fifth game?"))
nbo_5 = int(input("How many boxes did your opponent create in the fifth game?"))
nog_1 = int(input("How much grids are there in the fifth game?"))

print(f"Your opponents are {noo_1}, {noo_2}, {noo_3}, {noo_4}, {noo_5}.")
print(f"Your total point is {nby_1 + nby_2 + nby_3 + nby_4 + nby_5}.")
print(f"The total point for your opponent is {nbo_1 + nbo_2 + nbo_3 + nbo_4 + nbo_5}.")
print(f"The percentage of boxes filled")