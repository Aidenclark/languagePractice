class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Insure that num1 is the smaller array- swap if needed
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        // Calculate the length of both of the arrays
        int m = nums1.length;
        int n = nums2.length;
        
        // Initialize the pointers for binary search
        // The left is 0 and the right is the furthest index
        int left = 0;
        int right = m;
        
        // Start the binary search loop as long as the left arrays is less than or equal two the right array
        while (left <= right) {
            // Calculate the partition points- break points in each array
            int partition1 = (left + right) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;

            // Calculate the max values on left side of partition and min values on right side of BOTH partitions 
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            
            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];
            
            // Check if partitioning is right- check if you have found the median 
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                if ((m + n) % 2 == 0) { // Check of the sum is even
                    // Take the larger and smaller values of left and right side and find median
                    return (double)(Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
                } else {
                    // But if the sum of the lengths is odd 
                    // Then just return the highest max value
                    return Math.max(maxLeft1, maxLeft2);
                }
            // If the left is bigger than the right, then move the right pointer in the binary search to the left
            } else if (maxLeft1 > minRight2) {
                right = partition1 - 1;
            // If maxLeft2 > minRight1 move the left pointer to the right
            } else {
                left = partition1 + 1;
            }
        }
        
        throw new IllegalArgumentException("Input arrays are not sorted.");
    }
}
