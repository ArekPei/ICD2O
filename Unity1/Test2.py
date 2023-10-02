import math
print ("Welcome to this simple calculator!")
# pwCheck means password check
pwCheck = False
password = int (123456789)
while pwCheck == False:
    passwordCheck = int (input ("Please enter the password: "))
    if passwordCheck == password:
        pwCheck = True
        # naCheck means number check
        naCheck = False
        while naCheck == False:
            numAmount = int (input ("How many numbers do you want to use (1/2): "))
            if numAmount == 1:
                num_1 = float (input ("Please input the number: "))
                naCheck = True
            elif numAmount == 2:
                num_1 = float (input ("Please input the first number: "))
                num_2 = float (input ("Please input the second number: "))
                naCheck = True
            else:
                print ("Please enter 1 or 2.")
                naCheck = False
        if numAmount == 1:
            numCheck = False
            print ("Please input 1 for exponent calculating")
            print ("Please input 2 for square root")
            while numCheck == False:
                cal = int (input ("Please input: "))
                if cal == 1:
                    exp = float (input ("Please input the exponent: "))
                    print (num_1 ** exp)
                    numCheck = True
                elif cal == 2:
                    print (math.sqrt(num_1))
                    numCheck = True
                else:
                    print ("Please input 1 or 2.")
                    numCheck = False
        elif numAmount == 2:
            # numCheck2 means the number check for two numbers
            numCheck2 = False
            print ("Please input 1 for addition")
            print ("2 for subtraction")
            print ("3 for multiplication")
            print ("4 for division")
            print ("5 for division with remainder")
            print ("6 for finding the hypotenuse of a triangle")
            print ("7 for finding a side of the triangle using the hypotenuse")
            while numCheck2 == False:
                cal = int (input ("Please input: "))
                if cal == 1:
                    print (num_1 + num_2)
                    numCheck2 = True
                elif cal == 2:
                    print (num_1 - num_2)
                    numCheck2 = True
                elif cal == 3:
                    print (num_1 * num_2)
                    numCheck2 = True
                elif cal == 4:
                    print (num_1 / num_2)
                    numCheck2 = True
                elif cal == 5:
                    print (f"{int (num_1 / num_2)} remainder {int (num_1 % num_2)}")
                    numCheck2 = True
                elif cal == 6:
                    print (math.sqrt (num_1 ** 2 + num_2 ** 2))
                    numCheck2 = True
                elif cal == 7:
                    print (math.sqrt (num_1 ** 2 - num_2 ** 2))
                    numCheck2 = True
                else:
                    print ("Please input a number from 1 to 5.")
                    numCheck2 = False
    else:
        print ("The password is incorrect.")
        pwCheck = False