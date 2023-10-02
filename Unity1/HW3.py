name = input ("What is your name?")
print ("Hello,", name)

num_1 = float (input ("Please input the first number:"))
num_2 = float (input ("Please input the second number:"))
cal = int (input ("Please input 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division:"))
if cal == 1:
    print (num_1 + num_2)
elif cal == 2:
    print (num_1 - num_2)
elif cal == 3:
    print (num_1 * num_2)
else:
    print (num_1 / num_2)

tempInCel = float (input ("Please input the temperature in degree Celsius:"))
tempInFer = float (tempInCel * 9 / 5 + 32)
print (f"{tempInCel} degrees Celsius is equal to {tempInFer} degrees Fahrenheit.")

Name = str (input ("What is your name?"))
age = int (input ("Hou old are you?"))
city = str (input ("Which city do you live in?"))
print (f"Your name is {Name}, you are {age} years old, and you live in {city}.")

length = float (input ("Please input the length:"))
width = float (input ("Please input the width:"))
unit = str (input ("Please input the unit:"))
area = float (length * width)
print (f"The area of the shape is {area} {unit} squared.")

CADamount = float (input ("Please input the amount of CAD:"))
RMBamount = float (CADamount * 5.3)
print (f"{CADamount} Canadian dollars are equal to {RMBamount} of RMBs.")

firstName = str (input ("Please input your first name:"))
lastName = str (input ("Please input your last name:"))
print (f"Your full name is {firstName} {lastName}.")

price_1 = str (input("Please input the first item's price:"))
price_2 = str (input ("Please input the price of the second item:"))
price_3 = str (input ("Please input the price of the third item:"))
totalPrice = float (price_1) + float (price_2) + float (price_3)
print (f"The total price is {totalPrice} dollars.")

days = str (input ("Please input the number of days:"))
hours = int (days) * 24
print (f"{days} number of days is equal to {hours} hours.")

time = str (input ("Please input the time of the trip in number of hours:"))
dist = str (input ("Please input the distance traveled in kilometers:"))
speed = float (dist) / float (time)
print (f"The average speed while traveling is {speed} km/h.")