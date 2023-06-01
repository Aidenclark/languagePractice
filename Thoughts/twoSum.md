1. Python:

Python is known for its simplicity and readability. The code is concise and expressive.
It uses a class structure (class Solution) to encapsulate the solution.
Python provides built-in data structures like dictionaries to handle the storage of numbers and their indices.
Python supports dynamic typing, meaning you don't need to explicitly declare variable types.


2. Java:

Java is a statically typed language with a more verbose syntax compared to Python.
It uses classes (public class Solution) and methods (public static) to define the solution.
Java relies on the HashMap class from the java.util package for efficient key-value storage.
Java requires explicit declaration of variable types, offering strong type safety.


3. JavaScript:

JavaScript is a dynamic, interpreted language mainly used for web development.
It uses a functional approach with the var and function keywords.
JavaScript employs the Map object, which is similar to a dictionary, for key-value storage.
JavaScript allows for more flexible variable typing and less strict syntax rules.


4. C#:

C# is a statically typed language developed by Microsoft, similar to Java in terms of syntax.
It uses classes (public class Solution) and methods (public int[] TwoSum) for structuring the solution.
C# utilizes the Dictionary class from the System.Collections.Generic namespace for efficient key-value storage.
C# supports both static and dynamic typing with the var keyword.


---




# Iteration 1:

i = 0, num = 2
complement = 9 - 2 = 7
Since the number_dictionary is empty, the condition complement in number_dictionary is False.
The number_dictionary is updated: {2: 0}.

# Iteration 2:

i = 1, num = 7
complement = 9 - 7 = 2
The complement value exists as a key in the number_dictionary (2: 0).
The condition complement in number_dictionary is True, so the code inside the if statement is executed.
The function returns [number_dictionary[complement], i] = [0, 1].

