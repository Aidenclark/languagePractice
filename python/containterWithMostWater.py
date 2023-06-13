# https://chat.openai.com/?model=text-davinci-002-render-sha

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1 # we ensure that the right pointer initially points to the last vertical line in the array
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
