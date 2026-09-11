"""
21 Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Time Complexity: O(n + m) - We traverse both lists once
Space Complexity: O(1) - We use only constant extra space
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists into one sorted list.
    
    Args:
        list1: ListNode - Head of first sorted linked list
        list2: ListNode - Head of second sorted linked list
        
    Returns:
        ListNode - Head of the merged sorted linked list
        
    Example:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
    """
    # Create a dummy node to serve as the start of our result list
    dummy = ListNode()
    tail = dummy  # Tail points to the last node in our result list
    
    # Traverse both lists until one is exhausted
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    # Attach the remaining elements (if any)
    # Exactly one of list1 or list2 is not None at this point
    tail.next = list1 if list1 else list2
    
    # Return the head of the merged list (skip dummy node)
    return dummy.next

# Helper functions for testing
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
if __name__ == "__main__":
    # Test case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = mergeTwoLists(list1, list2)
    print("Test 1:", linked_list_to_list(merged))  # Expected: [1, 1, 2, 3, 4, 4]
    
    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = mergeTwoLists(list1, list2)
    print("Test 2:", linked_list_to_list(merged))  # Expected: []
    
    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = mergeTwoLists(list1, list2)
    print("Test 3:", linked_list_to_list(merged))  # Expected: [0]