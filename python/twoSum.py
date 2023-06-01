class Solution(object):
    def twoSum(self, nums, target):
        number_dictionary = {} # emtpy dictionary to store number and indices 
                               # Indicies (an alphabetical list of names, subjects, etc., with references to the places where they occur,)

        for i, num in enumerate(nums): # enumerate over list, tracking (i) & (num)
                                                                                                                                           
            complement = target - num # complement = number of something

            if complement in number_dictionary: # if the complement number exsits in the dictionary
                return [number_dictionary[complement], i] # then return the indicies as a list 
            number_dictionary[num] = i # store current num as a key that acts as an index in the dictionary
            
            # [number_dictionary[complement_2], i] = [0, 1].
            
            '''
            i=0, num=2                      complement_1 = 9 - 2 = 7
            i=1, num=7    ----------->      complement_2 = 9 - 7 = 2         ----------->   Is complement in dictionary?          ----------->   number_dictionary = {
            i=2, num=11                     complement_3 = 9 - 11 = -2                              Yes? ---> Go it if statement                    2: 0,
            i=3, num=15                     complement_4 = 9 - 15 = -6                                                                              7: 1              }
            ''' 

nums = [2, 7, 11, 15]
target = 9

solution = Solution() # create instance becaause of the class
indices = solution.twoSum(nums, target) # call it by creating "indices"
print(indices)
