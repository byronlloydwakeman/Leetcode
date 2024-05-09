class Solution:
    def __init__(self):
        self.sum = 0
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        def recursion(happiness_temp, k_temp):
            # Completed all the iterations
            if k_temp == 0 or len(happiness_temp) == 0:
                return

            self.sum += max(happiness_temp)
            happiness_temp.remove(max(happiness_temp))

            # Decrease all values by 1
            for index, num in enumerate(happiness_temp):
                if happiness_temp[index] > 0:
                    happiness_temp[index] = happiness_temp[index] - 1

            self.maximumHappinessSum(happiness_temp, k_temp - 1)
        
        result = recursion(happiness, k)
        print(self.sum)
        return self.sum
        
        
