"""
295 Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

Time Complexity: O(log n) for addNum, O(1) for findMedian
Space Complexity: O(n) - We store all elements in two heaps
"""

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        
        We use two heaps:
        - max_heap: stores the smaller half of numbers (as negatives for max heap behavior)
        - min_heap: stores the larger half of numbers
        
        This allows us to access the median in O(1) time.
        """
        # Max heap for the lower half (we store negatives to simulate max heap)
        self.max_heap = []  
        # Min heap for the upper half
        self.min_heap = []
    
    def addNum(self, num: int) -> None:
        """
        Adds a number from the data stream to the data structure.
        
        Args:
            num: int - The number to add
        """
        # Always add to max_heap first (as negative for max heap behavior)
        heapq.heappush(self.max_heap, -num)
        
        # Ensure every number in max_heap <= every number in min_heap
        # If the largest in max_heap > smallest in min_heap, we need to rebalance
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Balance the sizes: max_heap can have at most one more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
    
    def findMedian(self) -> float:
        """
        Returns the median of current data stream
        
        Returns:
            float - The median value
        """
        # If max_heap has more elements, its top is the median
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        # If both heaps have equal size, median is average of both tops
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Test the solution
if __name__ == "__main__":
    # Test case from LeetCode example
    medianFinder = MedianFinder()
    medianFinder.addNum(1)    # arr = [1]
    medianFinder.addNum(2)    # arr = [1, 2]
    print("Median after [1,2]:", medianFinder.findMedian())  # Expected: 1.5
    medianFinder.addNum(3)    # arr = [1, 2, 3]
    print("Median after [1,2,3]:", medianFinder.findMedian())  # Expected: 2.0
    
    # Additional test
    print("\nAdditional test:")
    medianFinder2 = MedianFinder()
    medianFinder2.addNum(-1)
    print("Median after [-1]:", medianFinder2.findMedian())  # Expected: -1.0
    medianFinder2.addNum(-2)
    print("Median after [-1,-2]:", medianFinder2.findMedian())  # Expected: -1.5
    medianFinder2.addNum(-3)
    print("Median after [-1,-2,-3]:", medianFinder2.findMedian())  # Expected: -2.0
    medianFinder2.addNum(-4)
    print("Median after [-1,-2,-3,-4]:", medianFinder2.findMedian())  # Expected: -2.5
    medianFinder2.addNum(-5)
    print("Median after [-1,-2,-3,-4,-5]:", medianFinder2.findMedian())  # Expected: -3.0