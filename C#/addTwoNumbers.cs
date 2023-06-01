public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) { // defines a public class named Solution that contains the method AddTwoNumbers to
                                                              // solve the given problem
                                                              // declares the AddTwoNumbers method, which takes two ListNode parameters l1 and l2, 
                                                              // and returns a ListNode

        ListNode dummy = new ListNode(); // create a dummy node to track the head of the result linked list
        ListNode current = dummy; // initialize a current node to traverse the result linked list
        int carry = 0; // initialize a carry variable to track the carry-over value
        
        while (l1 != null || l2 != null || carry != 0) { // EXACTLY the same while loop as java works
            int sum = carry; // Start with the carry-over value
            
            if (l1 != null) {
                sum += l1.val; // add the value from l1 if it exists
                l1 = l1.next; // move to the next node in l1
            }
            
            if (l2 != null) {
                sum += l2.val; // add the value from l2 if it exists
                l2 = l2.next; // move to the next node in l2
            }

            /*
            In Java, the variable digit is explicitly declared using the int keyword before assigning it the value. 
            In C#, the declaration is omitted, and digit is directly assigned the value.
            */

            current.next = new ListNode(sum % 10); // create a new node with the calculated digit
            current = current.next; // move the current pointer to the next node
            
            carry = sum / 10; // calculate the carry-over value for the next position
        }
        
        return dummy.next; // return the head of the resulting linked list
    }
}

// https://stackoverflow.com/questions/2625520/java-and-c-how-close-are-they
