"""
238 Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Time Complexity: O(n) - We traverse the array twice
Space Complexity: O(1) excluding output array - We use only constant extra space
"""

def productExceptSelf(nums):
    """
    Given an integer array nums, return an array answer such that 
    answer[i] is equal to the product of all the elements of nums except nums[i].
    
    Args:
        nums: List[int] - Input array of integers
        
    Returns:
        List[int] - Array where each element is product of all other elements
        
    Example:
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        
    Note: The problem guarantees that the product fits in a 32-bit integer.
    """
    n = len(nums)
    result = [1] * n
    
    # First pass: calculate prefix products
    # result[i] will contain product of all elements to the left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Second pass: calculate suffix products and multiply with prefix
    # We'll multiply result[i] by product of all elements to the right of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print("Input:", nums1)
    print("Output:", productExceptSelf(nums1))  # Expected: [24, 12, 8, 6]
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print("\nInput:", nums2)
    print("Output:", productExceptSelf(nums2))  # Expected: [0, 0, 9, 0, 0]
    
    # Test case 3
    nums3 = [2, 3, 4, 5]
    print("\nInput:", nums3)
    print("Output:", productExceptSelf(nums3))  # Expected: [60, 40, 30, 24]