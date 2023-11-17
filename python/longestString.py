class Solution:
    def intersect(self, nums1, nums2):
      
        counts1 = {}
        counts2 = {}

        for num in nums1:
            counts1[num] = counts1.get(num, 0) + 1

        for num in nums2:
            counts2[num] = counts2.get(num, 0) + 1

        intersection = []
        for num in counts1:
            if num in counts2:
                intersection.extend([num] * min(counts1[num], counts2[num]))

        return intersection
