""" Contains operations for working with numeric values"""
from decimal import Decimal

def add(x: Decimal, y: Decimal) -> Decimal:
    """Return the sum of x and y

    Args:
        x: A positive or negative Decimal value
        y: A positive or negative Decimal value

    Returns:
        A Decimal value representing the result of the operation."""
    return x + y

def subtract(x: Decimal, y: Decimal) -> Decimal:
    """Return the difference of x and y

    Args:
        x: A positive or negative Decimal value
        y: A positive or negative Decimal value

    Returns:
        A Decimal value representing the result of the operation."""
    return x - y

def multiply(x: Decimal, y: Decimal) -> Decimal:
    """Return the product of x and y

    Args:
        x: A positive or negative Decimal value
        y: A positive or negative Decimal value

    Returns:
        A Decimal value representing the result of the operation."""
    return x * y

def divide(x: Decimal, y: Decimal) -> Decimal:
    """Return the quotient of x and y

    Args:
        x: A positive or negative Decimal value
        y: A positive or negative Decimal value

    Returns:
        A Decimal value representing the result of the operation."""
    if y == 0:
        # Handle ZeroDivisionError
        raise ValueError("You can't divide by zero.")
    return x / y
