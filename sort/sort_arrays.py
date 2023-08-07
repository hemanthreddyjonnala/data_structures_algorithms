from typing import List

class Sort:
    def insertion_sort(self, nums: List[int]) -> List[int]: 
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
    
    def selection_sort(self, nums: List[int]) -> List[int]: 
        """ Selection Sort"""       
        n = len(nums)
        for i in range(n):
            swap_index = i
            for j in range(i+1, n):
                # identify the swap position and swap the values
                if nums[j]<nums[swap_index]:
                    swap_index = j
            nums[swap_index], nums[i] = nums[i], nums[swap_index]
        return nums
                
nums = [5,2,3,1]

sort_object = Sort()

print(f"insertion sort: {sort_object.insertion_sort(nums)}")
print(f"slection sort: {sort_object.selection_sort(nums)}")