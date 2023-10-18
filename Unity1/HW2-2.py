import math

def multiply():
    num1 = float(input("num1"))
    num2 = float(input("num2"))
    print(f"The result is {num1 * num2}.")
multiply()

def calculate_cylinder_volume():
    radius = float(input("Radius"))
    height = float(input("Height"))
    volume = radius ** 2 * math.pi * height
    print(volume)
calculate_cylinder_volume()

def print_triangle():
    char = str(input("Character"))
    print(f"{char:>5}")
    print(f"{char:>3}{char:>4}")
    print(char, char, char, char, char)
print_triangle()

def say_hello():
    name = str(input("Name"))
    print(f"Hello {name}.")
say_hello()

def calculate_circle_area():
    rad = float(input("Radius"))
    area = rad * math.pi
    print(f"The area is {area}.")
calculate_circle_area()

def print_square():
    character = str(input("Character"))
    print(character, character, character)
    print(f"{character:<3}{character:>2}")
    print(character, character, character)
print_square()

def calculate_power():
    power = float(input("Power"))
    number = float(input("Number"))
    print(number ** power)
calculate_power()

def calculate_triangle_area():
    base = float(input("Base"))
    hei = float(input("Height"))
    print(base * hei / 2)
calculate_triangle_area()