"""
347 Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Time Complexity: O(n log k) - We process n elements and heap operations are O(log k)
Space Complexity: O(n) - We store frequency counts and heap of size k
"""

import heapq
from collections import Counter

def topKFrequent(nums, k):
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
    
    Args:
        nums: List[int] - Input array of integers
        k: int - Number of top frequent elements to return
        
    Returns:
        List[int] - The k most frequent elements
        
    Example:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
    """
    # Count frequency of each element
    count = Counter(nums)
    
    # Use a min heap of size k to keep track of top k elements
    # We store (frequency, element) tuples in the heap
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        # If heap size exceeds k, remove the smallest frequency element
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract the elements from the heap
    return [num for freq, num in heap]

# Alternative solution using bucket sort (O(n) time)
def topKFrequent_bucket(nums, k):
    """
    Alternative O(n) solution using bucket sort.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Count frequency of each element
    count = Counter(nums)
    
    # Create buckets where index represents frequency
    # Maximum frequency can be len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    # Place each number in its frequency bucket
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Collect results from highest frequency buckets
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

# Test the solution
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print("Input:", nums1, "k =", k1)
    print("Output:", topKFrequent(nums1, k1))  # Expected: [1, 2] or [2, 1]
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print("\nInput:", nums2, "k =", k2)
    print("Output:", topKFrequent(nums2, k2))  # Expected: [1]
    
    # Test case 3
    nums3 = [4, 1, -1, 2, -1, 2, 3]
    k3 = 2
    print("\nInput:", nums3, "k =", k3)
    print("Output:", topKFrequent(nums3, k3))  # Expected: [-1, 2] or [2, -1]