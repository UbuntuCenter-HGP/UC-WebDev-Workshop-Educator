# Welcome to Genius Games 2025 - Technical Challenge!
# ==============================================
# This is a coding challenge where you need to complete the missing parts of the code.
# You have 30 minutes to complete as many challenges as you can.
# Each challenge is independent, so you can work on them in any order.

import os
import time
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ===== Challenge 1: Number Doubler =====
def double_number(number):
    # TODO: Complete this function to double the input number
    # HINT: You need to add one line of code here
    # HINT: What operation do we use to multiply numbers?
    # HINT: Look at the test cases to see what the function should return
    
    # Write your code here:
    return number  # <-- This line needs to be fixed!

def test_doubler():
    print("\nTesting Number Doubler...")
    print("=" * 40)
    
    test_numbers = [2, 5, 10, 0, -3]
    expected_results = [4, 10, 20, 0, -6]
    
    score = 0
    total_tests = len(test_numbers)
    
    for i, (num, expected) in enumerate(zip(test_numbers, expected_results), 1):
        result = double_number(num)
        print(f"\nTest {i}:")
        print(f"Input: {num}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        
        if result == expected:
            print("✓ Test passed!")
            score += 1
        else:
            print("✗ Test failed!")
            print("HINT: Remember, doubling means multiplying by 2!")
    
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total_tests}")
    print("=" * 40)
    
    if score == total_tests:
        print("\nCongratulations! You've fixed the number doubler!")
    else:
        print("\nKeep trying! Look at the failed tests for hints.")

# ===== Challenge 2: Calculator =====
def calculate(num1, num2, operation):
    # TODO: Complete this function to perform basic operations
    # HINT: You need to add the correct operation for each case
    # HINT: Look at the test cases to see what each operation should do
    
    if operation == "+":
        # Write your code here:
        return num1  # <-- This line needs to be fixed!
    elif operation == "-":
        # Write your code here:
        return num1  # <-- This line needs to be fixed!
    elif operation == "*":
        return num1 * num2  # This one is correct!
    elif operation == "/":
        return num1 / num2  # This one is correct!
    else:
        return "Invalid operation"

def test_calculator():
    print("\nTesting Calculator...")
    print("=" * 40)
    
    test_cases = [
        (10, 5, "+", 15),  # Addition
        (10, 5, "-", 5),   # Subtraction
        (10, 5, "*", 50),  # Multiplication
        (10, 5, "/", 2),   # Division
        (0, 5, "+", 5),    # Edge case: zero
        (-5, 3, "*", -15)  # Edge case: negative numbers
    ]
    
    score = 0
    total_tests = len(test_cases)
    
    for i, (num1, num2, op, expected) in enumerate(test_cases, 1):
        result = calculate(num1, num2, op)
        print(f"\nTest {i}:")
        print(f"Input: {num1} {op} {num2}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        
        if result == expected:
            print("✓ Test passed!")
            score += 1
        else:
            print("✗ Test failed!")
            if op == "+":
                print("HINT: Addition means adding two numbers together!")
            elif op == "-":
                print("HINT: Subtraction means taking one number away from another!")
    
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total_tests}")
    print("=" * 40)
    
    if score == total_tests:
        print("\nCongratulations! You've fixed the calculator!")
    else:
        print("\nKeep trying! Look at the failed tests for hints.")

# ===== Challenge 3: FizzBuzz =====
def fizzbuzz(number):
    # TODO: Complete this function to handle multiples of 3 and 5
    # HINT: You need to add the correct conditions
    # HINT: Check for multiples of both 3 and 5 first
    # HINT: Use the modulo operator (%) to check for divisibility
    
    # Write your code here:
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def test_fizzbuzz():
    print("\nTesting FizzBuzz...")
    print("=" * 40)
    
    test_cases = [
        (3, "Fizz"),      # Multiple of 3
        (5, "Buzz"),      # Multiple of 5
        (15, "FizzBuzz"), # Multiple of both 3 and 5
        (1, "1"),         # Not a multiple of 3 or 5
        (30, "FizzBuzz"), # Another multiple of both
        (9, "Fizz"),      # Another multiple of 3
        (10, "Buzz")      # Another multiple of 5
    ]
    
    score = 0
    total_tests = len(test_cases)
    
    for i, (num, expected) in enumerate(test_cases, 1):
        result = fizzbuzz(num)
        print(f"\nTest {i}:")
        print(f"Input: {num}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        
        if result == expected:
            print("✓ Test passed!")
            score += 1
        else:
            print("✗ Test failed!")
            if num % 3 == 0 and num % 5 == 0:
                print("HINT: Numbers divisible by both 3 and 5 should return 'FizzBuzz'!")
            elif num % 3 == 0:
                print("HINT: Numbers divisible by 3 should return 'Fizz'!")
            elif num % 5 == 0:
                print("HINT: Numbers divisible by 5 should return 'Buzz'!")
    
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total_tests}")
    print("=" * 40)
    
    if score == total_tests:
        print("\nCongratulations! You've fixed the FizzBuzz function!")
    else:
        print("\nKeep trying! Look at the failed tests for hints.")

def print_header():
    print("\n" + "="*60)
    print("Genius Games 2025 - Technical Challenge".center(60))
    print("="*60)
    print("\nWelcome to the coding challenge!")
    print("You have 30 minutes to complete the challenges.")
    print("Each challenge is independent - work on them in any order.")
    print("\nAvailable Challenges:")
    print("1. Number Doubler (Easy)")
    print("   - Complete one line of code to double a number")
    print("   - Look at the test cases for hints")
    print("\n2. Calculator Challenge (Medium)")
    print("   - Complete the addition and subtraction operations")
    print("   - Multiplication and division are already working")
    print("\n3. FizzBuzz Challenge (Hard)")
    print("   - Complete the conditions to check for multiples of 3 and 5")
    print("   - Remember to check for multiples of both first")
    print("\nGood luck!")

def main():
    clear_screen()
    print_header()
    
    start_time = time.time()
    time_limit = 30 * 60  # 30 minutes in seconds
    
    # Run all tests immediately
    print("\nRunning all tests...")
    print("=" * 60)
    
    # Test Challenge 1
    test_doubler()
    
    # Test Challenge 2
    test_calculator()
    
    # Test Challenge 3
    test_fizzbuzz()
    
    # Show remaining time
    elapsed_time = time.time() - start_time
    remaining_time = time_limit - elapsed_time
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    print(f"\nTime remaining: {minutes:02d}:{seconds:02d}")
    
    print("\n" + "="*60)
    print("Thank you for participating in Genius Games 2025!")
    print("="*60)

if __name__ == "__main__":
    main() 