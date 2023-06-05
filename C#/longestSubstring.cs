public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int maxLength = 0;
        int left = 0;
        int right = 0;
        HashSet<char> set = new HashSet<char>();
        // HashSet<T>: is a built in C# class where you create a new object to store chars
        // It has some methods like .Add(), .Remove(), and .Contains()
        // HashSet<char> implementation ensures that there are no duplicate characters

        while (right < s.Length) {
            if (!set.Contains(s[right])) {
                set.Add(s[right]);
                maxLength = Math.Max(maxLength, set.Count);
                right++;
            } else {
                set.Remove(s[left]);
                left++;
            }
        }
        // I think it is important to not that the structure of this code is similar to other languages
        // Obviously the syntax is just different ;)

        return maxLength;
    }
}
