/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) { // function that takes two ListNode parameters and returns a ListNode.
    let dummy = new ListNode(0); // create a dummy node to track the head of the result linked list
    let current = dummy; // initialize a current node to traverse the result linked list
    let carry = 0; // initialize a carry variable to track the carry-over value
    
    while (l1 || l2 || carry) {
        let sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry; // calculate the sum of the current digits and the carry-over value
        /*
        ? : expression. It checks if l1 is truthy (not null or undefined). If it is truthy, it evaluates to l1.val, 
        which accesses the val property of the l1 node. Otherwise, if l1 is falsy (null or undefined), it evaluates to 0
        */
        let digit = sum % 10; // determine the digit value for the current position
        carry = Math.floor(sum / 10); // determine the carry-over value for the next position
        
        current.next = new ListNode(digit); // create a new node with the calculated digit
        current = current.next; // move the current pointer to the next node
        // .next is also in javascript
        
        l1 = l1 ? l1.next : null; // move to the next node in l1 if it exists
        l2 = l2 ? l2.next : null; // move to the next node in l2 if it exists
    }
    
    return dummy.next; // return the head of the resulting linked list
