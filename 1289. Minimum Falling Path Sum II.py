# INCOMPLETE SOLUTION
# DOESN'T WORK FOR ALL TEST CASES  
# DP solution still in progress...

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        last_column = 0
        path = []
        min_1 = 0
        for row_index, row in enumerate(grid):
            minimum = min(row)
            if row_index == 0:
                path.append(minimum)
                last_column = row.index(minimum)
            else:
                print(last_column)
                # If the minimum is in the same column
                if last_column == row.index(minimum):
                    # Get the next minimum
                    row_copy = row.copy()
                    row_copy.remove(minimum)
                    second_minimum = min(row_copy)
                    path.append(second_minimum)
                    last_column = row.index(second_minimum)
                    
                else:
                    path.append(minimum)
                    last_column = row.index(minimum)


        sum_1 = sum(path)
        path = []

        for row_index, row in enumerate(reversed(grid)):
            minimum = min(row)
            if row_index == 0:
                path.append(minimum)
                last_column = row.index(minimum)
            else:
                print(last_column)
                # If the minimum is in the same column
                if last_column == row.index(minimum):
                    # Get the next minimum
                    row_copy = row.copy()
                    row_copy.remove(minimum)
                    second_minimum = min(row_copy)
                    path.append(second_minimum)
                    last_column = row.index(second_minimum)
                    
                else:
                    path.append(minimum)
                    last_column = row.index(minimum)

        
        return min(sum(path), sum_1)

                
        
