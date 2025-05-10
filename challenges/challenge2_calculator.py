# Challenge 2: Calculator
# ======================
# Fix this calculator to perform basic arithmetic operations

def calculate(num1, num2, operation):
    # TODO: Fix this calculator function
    # HINT: You need to fix the return statements for each operation
    # HINT: Look at the test cases to see what each operation should return
    
    if operation == "+":
        return num1 + num2  # <-- This is wrong! Fix it!
    elif operation == "-":
        return num1 - num2  # <-- This is wrong! Fix it!
    elif operation == "*":
        return num1 * num2  # This one is correct!
    elif operation == "/":
        return num1 / num2  # <-- This is wrong! Fix it!
    else:
        return "Invalid operation"

def test_calculator():
    print("\nTesting Calculator...")
    print("=" * 40)
    
    test_cases = [
        (5, 3, "+", 8),    # Addition
        (10, 4, "-", 6),   # Subtraction
        (6, 7, "*", 42),   # Multiplication
        (20, 5, "/", 4),   # Division
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
                print("HINT: Addition means adding numbers together!")
            elif op == "-":
                print("HINT: Subtraction means taking away the second number from the first!")
            elif op == "/":
                print("HINT: Division means splitting the first number into equal parts!")
    
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total_tests}")
    print("=" * 40)
    
    if score == total_tests:
        print("\nCongratulations! You've fixed the calculator!")
    else:
        print("\nKeep trying! Look at the failed tests for hints.")

if __name__ == "__main__":
    test_calculator() 