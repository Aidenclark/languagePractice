'''
This solution works by expanding around the center to find palindromes

function LongestPalindrome
    if s is empty
    return

    longest = ""

    create loop from i to 0 to length of s - 1
        # check for odd length palidrome
        oddpalidrome = expandFunction(s,i,i)
        if length of oddplaidrome is greater than length of longest
            set longest as odd
        
        # check for even palidrome 
        evenpalidrome = expandFunction(s,i ,i)
        if length of even palidrome is greater than length of longest
            set longest as even

expandFunction(s, left, right)
    
    while left is >= 0 and right is < than length of s and s[left] = s[right]
        decrement left by one
        increment right by one
        
    return substring of s from left + 1 to right
    

'''

class Solution(object):
    # Definition that takes in self (to reference solution) and s (the input string)
    # First line is a conditional statement to check if the string is empty
    def longestPalindrome(self, s):
        if not s:
            return ""

        # Input string will be called longest
        longest = ""

        # Loop starts to iterate over the indices of string s
        # range(len(s)) creates a sequence of numbers from 0 to len(s) - 1; which are the valid indices in the string
        for i in range(len(s)):

            # Check for odd length palindromes
            # Calls expand_around_center method; passing s, i (as current index), and i (for center index)
            # The method results in the odd_palindrome- it does a quick check to see if it is the longest string
            odd_palindrome = self.expand_around_center(s, i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            # Check for even length palindromes
            # Same as above but this time the method expands from two adjacent indicies to find longest even length palidrome
            # Because it is even ;)
            even_palindrome = self.expand_around_center(s, i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest # longest palidrome should be returned

    def expand_around_center(self, s, left, right):
        # While loop will continue as three conditions are satisfied simulteanously: (ensuring they don't go out of bounds)
        # left: is great than or equal to 0 
        # right: less than the length of the string s (they also must be equal because palindrome)
        while left >= 0 and right < len(s) and s[left] == s[right]:

            # Left is decremented by 1 and right is incremented by one- palidrome range is expanded 
            left -= 1
            right += 1

        # Returns the SUBSTRING
        # This slices the s string to exclude the non-palindromic chars
        # Since the left will be the first to know of the bad character you must slice it using + 1
        return s[left + 1:right]
