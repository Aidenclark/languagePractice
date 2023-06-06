/*
The difference between `s.charAt(left)` in Java and `s[left]` in JavaScript lies in how they access characters in a string.

In Java, the `charAt` method is used to access a character at a specific index in a string. It is a method of the `String` class and requires the `.` operator to invoke it. The syntax is `s.charAt(index)`, where `s` is the string and `index` is the position of the character to be accessed. The `charAt` method returns the character at the specified index as a `char` data type.

On the other hand, in JavaScript, you can directly access characters in a string using square brackets notation. The syntax is `s[index]`, where `s` is the string and `index` is the position of the character to be accessed. JavaScript treats strings as arrays of characters, so you can access individual characters using array-like notation. The expression `s[index]` returns the character at the specified index as a string data type.

Here's an example to illustrate the difference:

```java
String s = "Hello";
char ch = s.charAt(1); // Accessing the character 'e' using charAt
System.out.println(ch); // Output: e
```

```javascript
var s = "Hello";
var ch = s[1]; // Accessing the character 'e' using square brackets
console.log(ch); // Output: e
```

In both Java and JavaScript, you can access individual characters in a string using different methods. However, the syntax and method names differ between the two languages.
*/

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s === null || s.length < 2) {
        return s;
    }
    
    let start = 0;
    let end = 0;
    
    for (let i = 0; i < s.length; i++) {
        let len1 = expandAroundCenter(s, i, i);
        let len2 = expandAroundCenter(s, i, i + 1);
        let len = Math.max(len1, len2);
        
        // The Math.floor () function returns the largest integer less than or equal to a given number.
        if (len > end - start) {
            start = i - Math.floor((len - 1) / 2);
            end = i + Math.floor(len / 2);
        }
    }
    
    return s.substring(start, end + 1);
};

var expandAroundCenter = function(s, left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
        left--;
        right++;
    }
    
    return right - left - 1;
};
