"""
20 Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Time Complexity: O(n) - We traverse the string once
Space Complexity: O(n) - We use a stack that can grow up to n/2
"""

def isValid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.
    
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    
    Args:
        s: str - Input string containing only brackets
        
    Returns:
        bool - True if the string is valid, False otherwise
        
    Example:
        Input: s = "()"
        Output: true
        
        Input: s = "()[]{}"
        Output: true
        
        Input: s = "(]"
        Output: false
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing brackets to their corresponding opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in s:
        if char in mapping:
            # If it's a closing bracket
            # Pop the top element from stack if it's not empty, otherwise use '#'
            top_element = stack.pop() if stack else '#'
            
            # Check if the popped element matches the expected opening bracket
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If stack is empty, all brackets were properly closed
    return not stack

# Test the solution
if __name__ == "__main__":
    # Test case 1
    s1 = "()"
    print("Input:", s1)
    print("Output:", isValid(s1))  # Expected: True
    
    # Test case 2
    s2 = "()[]{}"
    print("\nInput:", s2)
    print("Output:", isValid(s2))  # Expected: True
    
    # Test case 3
    s3 = "(]"
    print("\nInput:", s3)
    print("Output:", isValid(s3))  # Expected: False
    
    # Test case 4
    s4 = "([)]"
    print("\nInput:", s4)
    print("Output:", isValid(s4))  # Expected: False
    
    # Test case 5
    s5 = "{[]}"
    print("\nInput:", s5)
    print("Output:", isValid(s5))  # Expected: True