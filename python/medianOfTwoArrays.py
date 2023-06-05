'''
To achive the desiredd O(log(m+n)) time complexity you need to implement binary search

It checks the length of the arrays
Then inside the loop it calculates the indices of i and j as partition points of the arrays
Then it preforms adjacent elements to determine cir the current partitioning is valid
If the partitioning is correct then it creates a median based off on it the array is odd or even 
It considers the maximum element element on the left side and the min element on the right side to find median

The runtime complexity of this is O(log(min(m,n)))- because binary seach is made on the shorter array
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2) # Assign length of arrays to m and n
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        # Checks if m is bigger than n 
        # If the condition is met then the line below perfroms simultaneous assignment (tells Python to evaluate all 
        # the expressions on the right-hand side and then assign these values to the corresponding variables named 
        # on the left-hand side.) using tuple packing and unpacking 
        # Swaps the values of nums1 and nums2 their correspoding lengths 
        # After this operation nums1 will ALWAYS be shorter
        
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        # imin is a variable the represents the minimum index 
        # imax represents the maximun index 
        # half_len presents the midpoint index
        # Setting these values is to setup the search range
        
        while imin <= imax:
            i = (imin + imax) // 2
            # Calculate the midpoint index using imin and imax
            # Ensuring that the loop continues as long as the search range is valid
            j = half_len - i
            # Calculates the midpoint index of the combined arrays 
            # The sum of the elements on the left side partition is equal to the right side
            
            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            # Checks current partitioning is invalid because an elements in nums2 on the left side 
            # is greater than an element in nums1 on the right side, SO the search range needs to be updated 
            # to the right side thus: imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            # Checks if current partitioning is invalid if nums1 on left side is greater than nums2 on right side
            # If so, then search range must be adjusted, this: imax = i -1


            else: # If the current partitioning is valid: 
                if i == 0:
                    max_of_left = nums2[j - 1]
                # If i = 0 then all elements in nums2 are on the right side of the partition 
                # So, max_of left is set to the element just before the partition of nums2: nums2[j - 1] 

                elif j == 0:
                    max_of_left = nums1[i - 1]
                # If j = 0, then all elements in nums2 are on the right side of the partition
                # So, max_of_left is set to the element right before the partition: nums1[i - 1]

                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])
                # If i or j are not 0 then, it means there are elements on both sides of the partitions in both arrays
                # So max_of_left is set to the max value between the arrays: nums1[i - 1], nums2[j - 1]
                
                if (m + n) % 2 == 1:
                    return max_of_left
                # if the total number of elements are odd, the median is the max value on the left side
                # Because there is one more element on the left side
                


                # If the total number of elements is even then this block determines the min value on the 
                # right side of the partition 
                if i == m:
                    min_of_right = nums2[j]
                # i = m checks if the partition i is at the end of nums1- meaning the elements of nums1 are on the 
                # left side of the partition
                # So, min_of_right is set to the element just after the partition in nums 2 (nums2[j])

                elif j == n:
                    min_of_right = nums1[i]
                # Checks if the partition j is at teh end of nums2- meaning the elements in nums2 are on the left side
                # of the partition 
                # So, min_of_right is set to the element just after the parition in nums1: nums1[i] 

                else:
                    min_of_right = min(nums1[i], nums2[j])
                # If i or j are not at the end of their respective arrays it means there are elements on both sides
                # of the partition in both arrays
                # So, min_of_rigth is set to the min value between nums1[i] and nums2[j]
                
                return (max_of_left + min_of_right) / 2.0
                # Finally the median of the two arrays
