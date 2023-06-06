class Solution {
    public String longestPalindrome(String s) {
        // Check if the string is null or has length less than 2, return the input string
        // Could just check if null
        if (s == null || s.length() < 2) {
            return s;
        }
        
        // Initialize start and end indices of the longest palindromic substring
        // IMPORTANT: using the start and end indices instead of saving the longest string as an array
        // is a memeory efficient approach. You don't need to store the substring- just indicate where it is
        int start = 0;
        int end = 0;
        
        // Iterate over each character in the string
        for (int i = 0; i < s.length(); i++) {
            // Expand around the center for odd-length palindromes
            int len1 = expandAroundCenter(s, i, i);
            
            // Expand around the center for even-length palindromes
            int len2 = expandAroundCenter(s, i, i + 1);
            
            // Compute the length of the longest palindrome at current center position
            int len = Math.max(len1, len2);
            
            // If the current palindrome is longer than the previously found longest palindrome,
            // update the start and end indices accordingly
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        
        // Extract and return the longest palindromic substring using substring(start, end + 1)
        return s.substring(start, end + 1);
    }
    
    // Helper method to expand around the center of a palindrome
    private int expandAroundCenter(String s, int left, int right) {
        // Expand until the left and right indices are within bounds and characters are equal
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        
        // Return the length of the palindrome (right - left - 1)
        return right - left - 1;
    }
}
