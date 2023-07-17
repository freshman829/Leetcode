# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        # Push digits of l1 into stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        # Push digits of l2 into stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        # Calculate sum of digits and create new nodes from right to left
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()

            if stack2:
                carry += stack2.pop()

            # Create new node with the value (carry % 10) and update carry
            carry, val = divmod(carry, 10)
            new_node = ListNode(val)

            # Update the 'next' pointer of the new node
            new_node.next = result

            # Update result as the new node
            result = new_node

        return result