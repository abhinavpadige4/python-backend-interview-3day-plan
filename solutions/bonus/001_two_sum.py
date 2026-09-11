"""
1 Two Sum
https://leetcode.com/problems/two-sum/

Time Complexity: O(n) - We traverse the array once
Space Complexity: O(n) - We store elements in a hash map
"""

def twoSum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices 
    of the two numbers such that they add up to target.
    
    Args:
        nums: List[int] - Input array of integers
        target: int - Target sum
        
    Returns:
        List[int] - Indices of the two numbers that add up to target
        
    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        
    Note: You may assume that each input would have exactly one solution, 
          and you may not use the same element twice.
    """
    # Create a hash map to store number -> index mapping
    num_map = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement we need to reach target
        complement = target - num
        
        # If complement exists in our map, we found the solution
        if complement in num_map:
            return [num_map[complement], i]
        
        # Otherwise, store current number and its index
        num_map[num] = i
    
    # According to problem constraints, we should always find a solution
    return []

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Input:", nums1, "target =", target1)
    print("Output:", twoSum(nums1, target1))  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("\nInput:", nums2, "target =", target2)
    print("Output:", twoSum(nums2, target2))  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("\nInput:", nums3, "target =", target3)
    print("Output:", twoSum(nums3, target3))  # Expected: [0, 1]