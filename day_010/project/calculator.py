from typing import Callable, Union, Dict
from art import logo


def add(n1: int, n2: int) -> int:
    """
    Adds two numbers (int or float) and returns the result.
    """
    return n1 + n2


def subtract(n1: int, n2: int) -> int:
    """
    Subtracts two numbers (int or float) and returns the result.
    """
    return n1 - n2


def multiply(n1: int, n2: int) -> int:
    """
    Multiplies two numbers (int or float) and returns the result.
    """
    return n1 * n2


def divide(n1: int, n2: int) -> Union[int, float]:
    """
    Divides two numbers (int or float) and returns the result.
    """
    return n1 / n2


operations: Dict[str, Callable] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Program Start
print(logo)
finished_calculation = False

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

while not finished_calculation:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    another_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
    if another_calculation == 'y':
        num1 = answer
    else:
        finished_calculation = True
