#!/usr/bin/env python3
import argparse


def add(x: int, y: int) -> int:
    """ Adds two numbers """
    if type(x) == int and type(y) == int:
        return int(x + y)
    else:
        return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="Operation to perform",
    )
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    args = parser.parse_args()

    result = None
    if args.operation == "add":
        result = add(args.x, args.y)
    elif args.operation == "subtract":
        result = subtract(args.x, args.y)
    elif args.operation == "multiply":
        result = multiply(args.x, args.y)
    elif args.operation == "divide":
        result = divide(args.x, args.y)

    print(f"Result of {args.operation}: {result}")


if __name__ == "__main__":
    main()
