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
