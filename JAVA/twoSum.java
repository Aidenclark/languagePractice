import java.util.HashMap; // hashmap is the best lookup of numbers and their indicies
                          // in java this it makes the dictionary library obsolete 

// NOTE: how the pseudo code is basically the same:
// Create dictionary --> create complement --> iterate through array with IF ...
public class Solution {
    public static int[] twoSum(int[] nums, int target) { // [] indicates array of ints
        // create a HashMap to store the numbers and their indices
        HashMap<Integer, Integer> map = new HashMap<>(); // for hashmap you need to declare both data types

        // iterate through the array- this is standard procedure in java to iterate
        for (int i = 0; i < nums.length; i++) {
            // calculate the complement of the current number
            int complement = target - nums[i];

            // if the complement exists in the HashMap, we found the solution
            if (map.containsKey(complement)) { // map is apart of hashmap
                // Return the indices of the two numbers
                return new int[]{map.get(complement), i}; // you need to make a new int on the fly
                // of coruse you get the complement and its spot (i) in the index
            }

            // add the current number and its index to the HashMap
            map.put(nums[i], i);
        }

        // if no solution is found, throw an exception
        throw new IllegalArgumentException("No two numbers add up to the target.");
    }

    public static void main(String[] args) { // if you remeber your training- this is the entry point of the program (main)
        // you can accept strings, but are not using it in this case
        
        // test the twoSum method
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] indices = twoSum(nums, target);
        System.out.println("Indices: " + indices[0] + ", " + indices[1]);
    }
}
