"""function for addition"""


def add(number_1, number_2):
    """
    Args:
        number_1 (int): adding num 1
        number_2 (int): adding num 2

    Returns:
        int: addition of num 1 and num 2
    """
    return number_1 + number_2


def subtract(number_1, number_2):
    """
    Args:
        number_1 (int): giving num 1
        number_2 (int): subtracting num 2 from num 1
    Returns:
        int: subtraction of num 1 and num 2
    """
    return number_1 - number_2

def multiply(number_1, number_2):
    """
    Args:
        number_1 (int): giving num 1
        number_2 (int): multiplying num 2 with num 1
    Returns:
        int: multiplication of num 1 and num 2
    """
    return number_1 * number_2


def division(number_1, number_2):
    """
    Args:
        number_1 (int): giving num 1
        number_2 (int): dividing num 2 from num 1
    Returns:
        int: division of num 2 from num 1
    """
    return number_1 / number_2


print("select the type of operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Please enter choice (1/2/3/4): ")

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))

if choice == '1':
    print(number1, " + ", number2, " = ", add(number1, number2))

elif choice == '2':
    print(number1, " - ", number2, " = ", subtract(number1, number2))

elif choice == '3':
    print(number1, " * ", number2, " = ", multiply(number1, number2))
elif choice == '4':
    print(number1, " / ", number2, " = ", division(number1, number2))
else:
    print("This is an invalid input")
