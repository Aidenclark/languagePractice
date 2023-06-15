/*
The two-pointer approach is a commonly used technique for solving problems that involve searching or manipulating elements in an array or a linked list. It typically involves 
initializing two pointers that traverse the array or list in a specific way. Here are some common use cases for the two-pointer approach:

1. Two-Sum Problem: Given an array of integers and a target value, find two numbers in the array that sum up to the target value. The two-pointer approach can be used to solve 
this problem efficiently by maintaining two pointers at different ends of the array and incrementing/decrementing them based on the current sum compared to the target value.

2. Three-Sum Problem: Given an array of integers, find three numbers that sum up to zero. This problem can be solved using the two-pointer approach by fixing one element and 
then using two pointers to find the remaining two elements that sum up to the negation of the fixed element.

3. Reverse Array/List: Reversing an array or a linked list can be done using the two-pointer approach. One pointer starts at the beginning, and the other starts at the end, 
and they swap elements as they move towards each other until they meet in the middle.

4. Removing Duplicates: Given a sorted array or a linked list, removing duplicates can be done using the two-pointer approach. One pointer iterates through the array/list, 
while the other pointer tracks the last unique element encountered. When a duplicate is found, the first pointer skips it, and the second pointer remains at the last unique 
element.

5. Finding Palindromes: The two-pointer approach can be used to determine whether a string or an array is a palindrome. One pointer starts at the beginning, and the other 
starts at the end, and they move towards each other, comparing corresponding elements until they meet in the middle. If all elements match, it is a palindrome.

6. Partitioning Arrays: The two-pointer approach is useful for partitioning arrays around a specific value or condition. It can be used to solve problems like the Dutch 
National Flag problem or the partition step in quicksort.

These are just a few examples of the many use cases for the two-pointer approach. It is a versatile technique that can be applied to various scenarios that involve 
searching, manipulation, or traversal of arrays or linked lists.


To solve this problem efficiently, we can use the two-pointer approach. We initialize two pointers, one at the beginning of the array (left) and the other at the end 
(right). We calculate the area between the lines represented by the pointers and update the maximum area if necessary. Then, we move the pointer with the smaller height 
towards the center.


Let's consider the input height = [1, 8, 6, 2, 5, 4, 8, 3, 7].

We start with two pointers, left and right, at the beginning and end of the array:


   |
[1, 8, 6, 2, 5, 4, 8, 3, 7]
   |                       |
 left                   right
Calculate the area between the lines represented by the pointers:

h = min(height[left], height[right]) = min(1, 7) = 1
w = right - left = 8 - 0 = 8
area = h * w = 1 * 8 = 8
max_area = max(max_area, area) = max(0, 8) = 8
Since height[left] < height[right], we move the left pointer towards the center:


   |
[1, 8, 6, 2, 5, 4, 8, 3, 7]
    |                      |
  left                  right
Next iteration:

h = min(height[left], height[right]) = min(8, 7) = 7
w = right - left = 7 - 1 = 6
area = h * w = 7 * 6 = 42
max_area = max(max_area, area) = max(8, 42) = 42
Since height[left] < height[right], we move the left pointer towards the center:


    |
[1, 8, 6, 2, 5, 4, 8, 3, 7]
     |                     |
   left                 right
Next iteration:

h = min(height[left], height[right]) = min(6, 7) = 6
w = right - left = 6 - 2 = 4
area = h * w = 6 * 4 = 24
max_area = max(max_area, area) = max(42, 24) = 42
Since height[left] < height[right], we move the left pointer towards the center:


     |
[1, 8, 6, 2, 5, 4, 8, 3, 7]
      |                    |
    left                right

*/ 



function maxArea(height) {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;
    
    while (left < right) {
        const h = Math.min(height[left], height[right]);
        const w = right - left;
        const area = h * w;
        maxArea = Math.max(maxArea, area);
        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}
