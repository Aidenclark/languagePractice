import java.util.HashSet;
// Unordered collections of unique elements that does not allow unique characters
// Efficeient insertation, deletion and lookup


class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Declaration for the lengthOfLongestSubstring method
        // Returns int but takes in a single string


        int n = s.length(); // Calculates length of input string to n
        int i = 0; // left pointer of the window
        int j = 0; // right pointer of window
        int maxLength = 0;


        HashSet<Character> set = new HashSet<>();
        // HashSet<Character> set: set variable will store objects of type Character in a HashSet
        // OR it creates a HashSet that can store characters
        // new HashSet<>(): creates a new hashset free of any elements


        while (j < n) { // continue until all loops are finished
            if (!set.contains(s.charAt(j))) {
                // if is to check if current character at index is present already
                // !set.contains(s.charAt(j)): if it is not present we add it to set using set.add(s.charAt(j));
                set.add(s.charAt(j));
                maxLength = Math.max(maxLength, j - i + 1);
                // Update maxLength
                j++;
                // Increment j by one to expand the window

            } else { // if character is already present in set we have encountered a repeatinc character, sooo
                set.remove(s.charAt(i));
                i++;
                // set.remove(s.charAt(i));: remove the character at index i from set
                // i++: increment left side of window 
            }
        }

        return maxLength;
    }
}
