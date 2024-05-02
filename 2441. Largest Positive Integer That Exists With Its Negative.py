class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        if not nums:
            return 0

        not_found = True
        while not_found:
            if len(nums) == 0:
                return -1
            temp_max = max(nums)
            print(temp_max)
            if temp_max * -1 in nums :
                not_found = False
                return temp_max
            else:
                nums.remove(temp_max)
        
