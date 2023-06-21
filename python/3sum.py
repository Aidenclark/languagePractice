def threeSum(nums):
    nums.sort()  # Sort the input array in ascending order
    result = []  # Initialize an empty list to store the triplets
    n = len(nums)  # Get the length of the sorted array

    for i in range(n - 2):  # Iterate through the array until the third-to-last element
        if i > 0 and nums[i] == nums[i - 1]:
            # Skip duplicates to avoid duplicate triplets
            continue

        left = i + 1  # Set the left pointer to the next element after i
        right = n - 1  # Set the right pointer to the last element

        while left < right:  # Loop until the pointers cross each other
            total = nums[i] + nums[left] + nums[right]  # Calculate the sum of the triplet

            if total < 0:  # If the sum is less than zero, increment the left pointer
                left += 1
            elif total > 0:  # If the sum is greater than zero, decrement the right pointer
                right -= 1
            else:  # If the sum is zero, found a triplet that satisfies the condition
                result.append([nums[i], nums[left], nums[right]])  # Add the triplet to the result list

                # Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1  # Move the left pointer forward
                right -= 1  # Move the right pointer backward

    return result  # Return the list of triplets
