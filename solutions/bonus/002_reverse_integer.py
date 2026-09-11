"""
7 Reverse Integer
https://leetcode.com/problems/reverse-integer/

Time Complexity: O(log n) - Number of digits in the integer
Space Complexity: O(1) - We use only constant extra space
"""

def reverse(x):
    """
    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the signed 32-bit integer 
    range [-2^31, 2^31 - 1], then return 0.
    
    Args:
        x: int - Input integer
        
    Returns:
        int - Reversed integer, or 0 if overflow occurs
        
    Example:
        Input: x = 123
        Output: 321
        
        Input: x = -123
        Output: -321
        
        Input: x = 120
        Output: 21
    """
    # Define 32-bit integer limits
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648
    
    # Store the sign and work with absolute value
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    
    # Reverse the digits
    reversed_num = 0
    while x_abs > 0:
        # Extract the last digit
        digit = x_abs % 10
        # Append digit to reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from x_abs
        x_abs //= 10
    
    # Apply the original sign
    reversed_num *= sign
    
    # Check for 32-bit integer overflow
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    
    return reversed_num

# Test the solution
if __name__ == "__main__":
    # Test case 1
    x1 = 123
    print("Input:", x1)
    print("Output:", reverse(x1))  # Expected: 321
    
    # Test case 2
    x2 = -123
    print("\nInput:", x2)
    print("Output:", reverse(x2))  # Expected: -321
    
    # Test case 3
    x3 = 120
    print("\nInput:", x3)
    print("Output:", reverse(x3))  # Expected: 21
    
    # Test case 4 (overflow case)
    x4 = 1534236469
    print("\nInput:", x4)
    print("Output:", reverse(x4))  # Expected: 0 (overflow)