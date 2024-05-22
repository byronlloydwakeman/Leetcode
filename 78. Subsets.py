class Solution:
    def __init__(self):
        self.result = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            self.result.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return self.result
