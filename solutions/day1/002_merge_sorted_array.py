"""
88 Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Time Complexity: O(m + n) - We traverse both arrays once
Space Complexity: O(1) - We modify nums1 in-place
"""

def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays into nums1.
    
    Args:
        nums1: List[int] - First sorted array with enough space for m + n elements
        m: int - Number of initialized elements in nums1
        nums2: List[int] - Second sorted array
        n: int - Number of elements in nums2
        
    Returns:
        None - Modifies nums1 in-place
        
    Example:
        Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        Output: [1,2,2,3,5,6]
    """
    # Start from the end of both arrays
    p1 = m - 1  # Pointer for nums1
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for end of merged array
    
    # Merge in reverse order
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, copy them
    # (No need to copy from nums1 as they're already in place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print("Test 1:", nums1)  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print("Test 2:", nums1)  # Expected: [1]
    
    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print("Test 3:", nums1)  # Expected: [1]