while True:
    try:
        first_number = input("Enter first number: ")
        if first_number == "stop":
            break
        operation = input("Enter operation: ")
        if operation == "stop":
            break
        second_number = input("Enter second number: ")
        if second_number == "stop":
            break
        if operation == "+":
            first_number_count = float(first_number)
            second_number_count = float(second_number)
            solution = first_number_count + second_number_count
        elif operation == "-":
            solution = first_number - second_number
        elif operation == "/":
            solution = first_number / second_number
        elif operation == "*":
            solution = first_number * second_number
        print(f"Answer: {solution}")
    except ValueError:
        if str(first_number) != "stop" or str(second_number) != "stop" or str(solution) != "stop":
            print("Please, enter a number!")
    except:
        print("Something wrong. Please, try again")


