class Solution(object):
    def subsetsWithDup(self, nums):

        def backtrack(start, current):
            # add current subset to the final result
            result.append(list(current))
            # iterate over nums to generate all possible subsets
            for i in range(start, len(nums)):
                # 1. skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                # 2. include nums[i] in current subset and move forward
                current.append(nums[i])
                backtrack(i+1, current)
                # 3. exclude nums[i] from current subset (backtrack)
                current.pop()
        
        result = []
        # sort the numbers to handle duplicates
        nums.sort()
        # initiate backtracking
        backtrack(0, [])
        return result
