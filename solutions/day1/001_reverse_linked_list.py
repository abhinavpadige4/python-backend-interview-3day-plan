"""
206 Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Time Complexity: O(n) - We visit each node exactly once
Space Complexity: O(1) - We use only constant extra space
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Reverse a singly linked list.
    
    Args:
        head: ListNode - The head of the linked list
        
    Returns:
        ListNode - The new head of the reversed list
        
    Example:
        Input: 1->2->3->4->5->NULL
        Output: 5->4->3->2->1->NULL
    """
    prev = None
    current = head
    
    # Iterate through the list, reversing pointers
    while current:
        # Store next node before changing current.next
        next_temp = current.next
        # Reverse the pointer
        current.next = prev
        # Move prev and current forward
        prev = current
        current = next_temp
    
    # Prev will be the new head
    return prev

# Helper function to create linked list from list (for testing)
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list (for testing)
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return "->".join(values) + "->NULL"

# Test the solution
if __name__ == "__main__":
    # Test case 1: Normal list
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverseList(head1)
    print("Original: 1->2->3->4->5->NULL")
    print("Reversed:", print_linked_list(reversed1))
    
    # Test case 2: Single element
    head2 = create_linked_list([1])
    reversed2 = reverseList(head2)
    print("\nOriginal: 1->NULL")
    print("Reversed:", print_linked_list(reversed2))
    
    # Test case 3: Empty list
    head3 = create_linked_list([])
    reversed3 = reverseList(head3)
    print("\nOriginal: NULL")
    print("Reversed:", print_linked_list(reversed3))