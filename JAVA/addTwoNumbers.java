/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) { // defines the addTwoNumbers method that takes two ListNode parameters and returns a ListNode.
        ListNode dummy = new ListNode(0); // create a dummy node to track the head of the result linked list
        ListNode current = dummy; // initialize a current node to traverse the result linked list
        int carry = 0; // initialize a carry variable to track the carry-over value
        
        while (l1 != null || l2 != null || carry != 0) { // starts a loop that continues until both input lists and the carry-over value are exhausted.
            int sum = carry; // start with the carry-over value
            
            if (l1 != null) {
                sum += l1.val; // add the value from l1 if it exists
                l1 = l1.next; // move to the next node in l1
            }
            
            if (l2 != null) {
                sum += l2.val; // add the value from l2 if it exists
                l2 = l2.next; // move to the next node in l2
            }
            
            int digit = sum % 10; // calculate the digit value for the current position
            carry = sum / 10; // calculate the carry-over value for the next position
            
            current.next = new ListNode(digit); // create a new node with the calculated digit
            current = current.next; // move the current pointer to the next node
            /*
            Both node.next in Python and node.next in Java refer to the next node in the linked list, allowing you to traverse the 
            list or manipulate the connections between nodes.
            */
        }
        
        return dummy.next; // return the head of the resulting linked list
    }
}
