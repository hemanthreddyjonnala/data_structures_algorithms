from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: 
        """ Insertion Sort """       
        for i in range(1, len(nums)):
            a = nums[i]
            j = i-1
            while j>=0 and nums[j]>a:
                # loop will continue till the sub array got sorted.
                # print(f"i:{i}, j:{j}, {nums[j]}>{a}, {nums}")
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = a
        return nums
                
nums = [5,2,3,1]

sort_object = Solution()

print(sort_object.sortArray(nums))