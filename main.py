#!/usr/bin/env python3

from my_package.module1 import hello_world
from my_package.module2 import add_numbers

def main():
    """Main function of the application"""
    hello_world()
    result = add_numbers(5, 7)
    print(f"The result of addition is: {result}")

if __name__ == "__main__":
    main()
