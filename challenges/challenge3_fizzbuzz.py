# Challenge 3: FizzBuzz
# ====================
# Fix this FizzBuzz function to handle multiples of 3 and 5 correctly

def fizzbuzz(number):
    # TODO: Fix this FizzBuzz function
    # HINT: The order of conditions matters!
    # HINT: Check for multiples of both 3 and 5 first
    # HINT: Use the modulo operator (%) to check for divisibility
    
    if number % 5 == 0:  # <-- This condition is in the wrong order!
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 3 == 0 and number % 5 == 0:  # <-- This condition will never be reached!
        return "FizzBuzz"
    else:
        return str(number)

def test_fizzbuzz():
    print("\nTesting FizzBuzz...")
    print("=" * 40)
    
    test_cases = [
        (3, "Fizz"),      # Multiple of 3
        (5, "Buzz"),      # Multiple of 5
        (15, "FizzBuzz"), # Multiple of both 3 and 5
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
            if num == 15:
                print("HINT: Check for multiples of both 3 and 5 first!")
            elif num == 3:
                print("HINT: Check for multiples of 3!")
            elif num == 5:
                print("HINT: Check for multiples of 5!")
    
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total_tests}")
    print("=" * 40)
    
    if score == total_tests:
        print("\nCongratulations! You've fixed the FizzBuzz function!")
    else:
        print("\nKeep trying! Look at the failed tests for hints.")

if __name__ == "__main__":
    test_fizzbuzz() 