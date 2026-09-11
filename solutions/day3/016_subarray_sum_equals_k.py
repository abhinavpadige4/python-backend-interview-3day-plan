"""
560 Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Time Complexity: O(n) - We traverse the array once
Space Complexity: O(n) - We store prefix sums in a hash map
"""

def subarraySum(nums, k):
    """
    Given an array of integers nums and an integer k, return the total number 
    of continuous subarrays whose sum equals to k.
    
    Args:
        nums: List[int] - Input array of integers
        k: int - Target sum
        
    Returns:
        int - Number of continuous subarrays whose sum equals k
        
    Example:
        Input: nums = [1,1,1], k = 2
        Output: 2
        
    Explanation: Uses prefix sum and hash map approach.
    """
    count = 0
    current_sum = 0
    # Dictionary to store frequency of prefix sums
    # Initialize with {0: 1} to handle subarrays starting from index 0
    prefix_sums = {0: 1}
    
    for num in nums:
        current_sum += num
        
        # If (current_sum - k) exists in prefix_sums, 
        # it means there are subarrays ending at current index with sum k
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        
        # Update the frequency of current prefix sum
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    
    return count

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1]
    k1 = 2
    print("Input:", nums1, "k =", k1)
    print("Output:", subarraySum(nums1, k1))  # Expected: 2
    
    # Test case 2
    nums2 = [1, 2, 3]
    k2 = 3
    print("\nInput:", nums2, "k =", k2)
    print("Output:", subarraySum(nums2, k2))  # Expected: 2 ([1,2] and [3])
    
    # Test case 3
    nums3 = [1]
    k3 = 0
    print("\nInput:", nums3, "k =", k3)
    print("Output:", subarraySum(nums3, k3))  # Expected: 0
    
    # Test case 4
    nums4 = [1, -1, 0]
    k4 = 0
    print("\nInput:", nums4, "k =", k4)
    print("Output:", subarraySum(nums4, k4))  # Expected: 3 ([1,-1], [0], [1,-1,0])