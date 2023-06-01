/**
 * @param {number[]} nums You don't need this garbadge because you can use map
 * @param {number} target
 * @return {number[]}
 */

// map an object for javascript whereas the JAVA hashmap is a class
// Java: HashMap in Java does not guarantee any specific order of the elements. If you need to iterate over the elements in a specific order, you can use a LinkedHashMap, which maintains the order of insertion.
// JavaScript: Map in JavaScript preserves the order of insertion. When you iterate over the elements of a Map, they are returned in the order in which they were added.
var twoSum = function(nums, target) {
    const map = new Map(); // create a Map to store numbers and their indices

    for (let i = 0; i < nums.length; i++) { // calculate the complement of the current number
    // same syntax as javascript
        const complement = target - nums[i]; // making he complement a const is best practice so it dones't change
        // Java's final provides immutability at the reference level- not a vairable level if you are wondering why we didn't use final (javas const) 
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i); // add the current number and its index to the Map
    } // very similar structure to java

    throw new Error('No two numbers add up to the target.');
}
