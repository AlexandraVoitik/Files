import random

#Guess the number from 1 to 50 in 6 tries

number = random.randint(1, 50)
tries = 0

while tries < 6:
    try:
        number1 = int(input("Guess the number from 1 to 50: "))
        tries += 1
        if number1 > 50 or number1 < 1:
            print("Number should be from 1 to 50")
        elif number1 == number:
           print(f"You guess on the {tries} try!")
           break
        elif number1 < number:
           print("Number is too low")
        elif number1 > number:
           print("Number is too high")
        if tries == 6 and number1 != number:
           print(f"You didn't guess! My number was {number}")

    except ValueError:
        print("Please, enter the number from 1 to 50.")
    except:
        print("Something went wrong. Try again!")
