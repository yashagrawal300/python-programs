'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1


        value = -1


        while start<= end:
            mid = (start+end)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
                value = mid
                
                
        return value+1
