/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLength = 0;
    let left = 0;
    let right = 0;
    let set = new Set();
    // new Set(): is a built in object that only stores unique values- duplicate values will be eliminated
    // Set maintains the order of insertion
    // Set also has a few methods: add(), delete(), has() --> check existence & a size property

    while(right < s.length) {
        if (!set.has(s.charAt(right))) {
            // "if the character at the current position in the string is not already present in the set.."
            // .has method checks if value is present 
            // charAt() method is used to access the character at a specific index
            // So it checks if the character at the current position is unique, which allows us to add it to the set

            set.add(s.charAt(right));
            // "Add the character at the current positon in the string to the set"
            // Adds the unique characters to the current substring

            maxLength = Math.max(maxLength, set.size);
            right++;
            // Update the max length and move the window over a slot
        } else {

            // If the character at the current postion is present ...
            // Then delete the character at the left point and move the window
            set.delete(s.charAt(left));
            left++;
        }
    }

    return maxLength;
};
