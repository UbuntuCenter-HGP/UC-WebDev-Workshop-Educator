# Challenge 1: Number Doubler
# =========================
# Complete this function to double any input number

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

if __name__ == "__main__":
    test_doubler() 