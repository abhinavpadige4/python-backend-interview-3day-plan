"""
152 Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Time Complexity: O(n) - We traverse the array once
Space Complexity: O(1) - We use only constant extra space
"""

def maxProduct(nums):
    """
    Given an integer array nums, find the contiguous subarray within an array 
    (containing at least one number) which has the largest product.
    
    Args:
        nums: List[int] - Input array of integers
        
    Returns:
        int - The maximum product of any contiguous subarray
        
    Example:
        Input: nums = [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.
    """
    if not nums:
        return 0
    
    # Initialize variables to track max and min products ending at current position
    # We need to track min because a negative number can make a min product become max
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        # If current number is negative, swapping max and min will help
        # because multiplying by negative makes big numbers small and small numbers big
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        # Calculate max and min products ending at current position
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        # Update global maximum
        result = max(result, max_prod)
    
    return result

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 3, -2, 4]
    print("Input:", nums1)
    print("Output:", maxProduct(nums1))  # Expected: 6
    
    # Test case 2
    nums2 = [-2, 0, -1]
    print("\nInput:", nums2)
    print("Output:", maxProduct(nums2))  # Expected: 0
    
    # Test case 3
    nums3 = [-2, 3, -4]
    print("\nInput:", nums3)
    print("Output:", maxProduct(nums3))  # Expected: 24
    
    # Test case 4
    nums4 = [0, 2]
    print("\nInput:", nums4)
    print("Output:", maxProduct(nums4))  # Expected: 2