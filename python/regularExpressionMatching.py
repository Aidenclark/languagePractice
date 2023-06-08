'''
Imagine you have two strings, let's call them "word" and "pattern." The goal is to check if the word matches 
the pattern according to some special rules.

In our special rules, there are two special characters:

The dot (.), which can represent any single letter.
The asterisk (*), which can represent zero or more occurrences of the preceding letter.

For example, let's say the word is "cat" and the pattern is "c.t". In this case, the dot (.) in the pattern can 
match any letter, so the word "cat" matches the pattern "c.t".

Now, let's take another example. If the word is "caaat" and the pattern is "cat", the asterisk () in the pattern 
means that the preceding letter (which is 'a' in this case) can occur zero or more times. So, the word "caaat" 
matches the pattern "ca*t".

To solve this problem, we can use a technique called dynamic programming. We'll create a table to keep track of 
the matches between different parts of the word and pattern.

We start filling in the table from the beginning. For each letter in the word and each character in the pattern, 
we check if they match. If they do, we look at the previous parts of the word and pattern to see if they also match. 
We continue filling the table until we reach the end of the word and pattern.

Finally, we check if the last cell in the table indicates a match between the entire word and pattern. If it does, 
it means that the word follows the pattern according to our special rules.

By using this dynamic programming approach, we can efficiently determine if a word matches a pattern with dots (.) 
and asterisks (*) in a more organized and systematic way.
'''


class Solution(object):
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        
        # Create a 2D DP table with (m + 1) rows and (n + 1) columns, with all values initially set to False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # [[False] * (n + 1)] creates a list of False values, repeated (n + 1) times. 
        # This inner list will represent a row in the dynamic programming table.
        # for _ in range(m + 1), indicates that we want to create a total of (m + 1) 
        #rows in the dynamic programming table
        
        # Base case: an empty pattern matches an empty string
        dp[0][0] = True
        
        # Handle the case when string s is empty (has no characters), but the pattern 
        # p has an asterisk (*)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        # For each column, the code checks if the character p[j - 1] is an asterisk (*)
        # dp[0][j - 2], we consider the case where the asterisk and the preceding character 
        # are removed, effectively treating them as if they don't exist in the pattern.
        # his step is necessary because when the string s is empty, the asterisks in the 
        # pattern can potentially match zero characters and still result in a valid match.
        


        # IMPORTANT: the program moves from left to right when iterating over s, and each 
        # character of s is processed in the corresponding iteration of the outer loop.

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                #If p[j - 1] matches s[i - 1] or is a dot '.':
                    # Set dp[i][j] equal to the value in the cell dp[i - 1][j - 1]
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]


                # If p[j - 1] is an asterisk '*':
                        # Set dp[i][j] equal to the value in the cell dp[i][j - 2] (ignoring the preceding character and the asterisk)    
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]


                    # of the preceding character p[j - 2] matches s[i - 1] or is a dot '.':
                        # Update dp[i][j] by performing a logical OR (|=) with the value in the cell dp[i - 1][j].
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] |= dp[i - 1][j]
        
        return dp[m][n]



'''
dynamic programming table with the indices `i` and `j` labeled:

Example inputs:
- String `s`: "aab"
- Pattern `p`: "c*a*b"

Table representation:
       ""  c  *  a  *  b    [j]             -dp[0][0] represents an empty string s and an empty pattern p, which always match (hence True)
   "" [ T, F, T, F, T, F]
   a  [ F, F, T, T, T, F]                   -The first row of the table corresponds to an empty string s and the pattern p. The first column 
   a  [ F, F, T, T, T, F]                   represents an empty pattern p and the string s.
   b  [ F, F, T, F, T, T]
                                            - dp[3][5] represents whether the entire string s matches the entire pattern p. In this case,
   [i]                                      it is True


To create pseudocode for the given code, we can follow these steps:

1. Initialize the variables `m` and `n` with the lengths of strings `s` and `p`, respectively.
2. Create a 2D DP table `dp` with `(m + 1)` rows and `(n + 1)` columns, initialized with `False` values.
3. Set `dp[0][0]` to `True` since an empty pattern matches an empty string.
4. Handle the case when `s` is empty but `p` has an asterisk:
   - Iterate through each column `j` from 1 to `n`:
     - If `p[j - 1]` is an asterisk:
       - Set `dp[0][j]` to the value of `dp[0][j - 2]`.
5. Fill the DP table:
   - Iterate through each row `i` from 1 to `m`:
     - Iterate through each column `j` from 1 to `n`:
       - If `p[j - 1]` matches `s[i - 1]` or is a dot `'.'`:
         - Set `dp[i][j]` to the value of `dp[i - 1][j - 1]`.
       - If `p[j - 1]` is an asterisk:
         - Set `dp[i][j]` to the value of `dp[i][j - 2]`.
         - If `p[j - 2]` matches `s[i - 1]` or is a dot `'.'`:
           - Update `dp[i][j]` by performing a logical OR (`|=`) with the value of `dp[i - 1][j]`.
6. Return the value of `dp[m][n]` as the result.

'''
