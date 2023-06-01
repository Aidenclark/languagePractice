# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Imagine you have two numbers, let's say 123 and 456. In the traditional way of representing numbers, the digits are ordered from left to right, with the most significant digit on the left. However, in this problem, the digits are stored in reverse order in two separate lists.

So, for the number 123, the digits would be stored as follows: 3 -> 2 -> 1. Similarly, for the number 456, the digits would be stored as: 6 -> 5 -> 4.

The task is to add these two numbers together and return the result as a linked list, where each node contains a single digit.

In our example, when we add 123 and 456, we get 579. Therefore, the resulting linked list would be: 9 -> 7 -> 5.

The important thing to note is that we need to account for carrying over any excess when the addition of two digits exceeds 9. For example, if we have to add 9 and 8, the result would be 17. In this case, we put down 7 and carry over the 1 to the next digit.

It is mentioned that we can assume the numbers do not contain any leading zeros, except for the number 0 itself. This means there won't be any unnecessary zeros at the beginning of the linked lists.
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # use a dummy node to track the head of the result linked list- serves as placeholder
        current = dummy      # current is a node that goes through (taverses) the linked list and adds new nodes as the operation progresses (setting it = to dummy acts as a pointer to it)
        carry = 0            # initializes carry- we need this to keep track of carry over values

        while l1 or l2 or carry: # while loop will continue unit digits of in at least one of the linked lists is non zero
            
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry # calculates the sum if it exists

            digit = sum % 10 # determines digit value for next iteration
            '''% acts as the modulo operator, meaning when its arguments are numbers, it divides the first by the second and returns the remainder.
             34 % 10 == 4 since 34 divided by 10 is three, with a remainder of four.'''
            carry = sum // 10 # Updates the carry value for the next iteration by performing integer division (//) of the sum by 10. 
            # This gives the quotient after dividing the sum by 10, which represents the carry-over value for the next addition operation.

            current.next = ListNode(digit)  # create a new node with the calculated digit
            # current.next is what you use when you want to find the last node in the list

            current = current.next          # Move the current pointer to the next node

            # moves to the next nodes in l1 and l2 if they exist. If l1 or l2 is not None, it assigns the next node to l1 or l2, respectively.
            # otherwise, it assigns None to indicate the end of the linked list
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # return the head of the resulting linked list
