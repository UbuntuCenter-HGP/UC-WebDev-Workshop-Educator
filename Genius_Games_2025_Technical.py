# Welcome to Genius Games 2025 - Technical Challenge!
# ==============================================
# This is a coding challenge where you need to complete the missing parts of the code.
# You have 45 minutes to complete as many challenges as you can.
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
    
    test_numbers = [5, 10]  # Two test cases
    expected_results = [10, 20]  # Expected results
    
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
    # BONUS CHALLENGE: Try implementing the remainder operation (%)
    # HINT: For remainder, think about what's left after division
    
    if operation == "+":
        # Write your code here:
        return num1  # <-- This line needs to be fixed!
    elif operation == "-":
        # Write your code here:
        return num1 - num2  # <-- This line is already correct!
    elif operation == "*":
        return num1 * num2  # <-- This one is already correct!
    elif operation == "/":
        # Write your code here:
        return num1 / num2  
    # BONUS: Try implementing the remainder operation
    # elif operation == "%":
    #     # Write your code here:
    #     return num1  # <-- This line needs to be fixed! (Hint: What's left after division?)
    else:
        return "Invalid operation"

def test_calculator():
    print("\nTesting Calculator...")
    print("=" * 40)
    
    test_cases = [
        (10, 5, "+", 15),    # Addition
        (10, 5, "-", 5),     # Subtraction
        (10, 5, "*", 50),    # Multiplication
        (10, 5, "/", 2),     # Division
        # BONUS: We also need to remainder operators
        (10, 3, "%", 1),     # Remainder (10 divided by 3 leaves remainder 1)
        (7, 4, "%", 3),      # Remainder (7 divided by 4 leaves remainder 3)
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
            elif op == "/":
                print("HINT: Division means how many times one number fits into another!")
            # elif op == "%":
            #     print("HINT: Remainder means what's left after division! For example, 10 % 3 = 1 because 3 goes into 10 three times with 1 left over!")
    
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total_tests}")
    print("=" * 40)
    
    if score == total_tests:
        print("\nCongratulations! You've fixed the calculator!")
        print("BONUS CHALLENGE: Try implementing the remainder operation (%)!")
    else:
        print("\nKeep trying! Look at the failed tests for hints.")

# ===== Challenge 3: FizzBuzz =====
def fizzbuzz(number):
    # TODO: Complete this function to handle multiples of 3 and 5
    # HINT: You need to add the correct conditions
    # HINT: Check for multiples of both 3 and 5 first
    # HINT: Use the modulo operator (%) to check for divisibility
    
    # Write your code here:
    # Are these in the correct order?
    if number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0 and number % 5 == 0:
        return "Fizz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return str(number)

def test_fizzbuzz():
    print("\nTesting FizzBuzz...")
    print("=" * 40)
    
    test_cases = [
        (3, "Fizz"),      # Test 1: Multiple of 3
        (5, "Buzz"),      # Test 2: Multiple of 5
        (15, "FizzBuzz"), # Test 3: Multiple of both 3 and 5
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
                print("HINT: The order of conditions matters!")
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
    print("You have 45 minutes to complete the challenges.")
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
    time_limit = 45 * 60  # 45 minutes in seconds
    
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