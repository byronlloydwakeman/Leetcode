class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def calculateListTotal(subset):
            result = subset[0]
            for num in subset[1:]:
                result ^= num
            return result

        result = 0
        def backtrack(start, path):
            nonlocal result
            if len(path) != 0:
                result += calculateListTotal(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return result

