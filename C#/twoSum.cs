public class Solution {
    public int[] TwoSum(int[] nums, int target) { // two params one is an array
        Dictionary<int, int> map = new Dictionary<int, int>(); // Dictionary<int, int> to store numbers and their indices
        // C# does not have a hashmap- instead use dictionary

        for (int i = 0; i < nums.Length; i++) { // loops through nums array and calculates complement for each
            int complement = target - nums[i];
            if (map.ContainsKey(complement)) { // ContainsKey(complement): is a method of the Dictionary
                // map: This is the dictionary (specifically, a Dictionary<int, int>)- to me this is confusing but it is what it is
                return new int[] { map[complement], i }; // if complement exists- then return
            }
            map[nums[i]] = i;
        }

        throw new ArgumentException("No two numbers add up to the target.");
    }
}
