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

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = (input("Pick an operation from the lines above: "))

num2 = int(input("What's the second number?: "))

answer = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
