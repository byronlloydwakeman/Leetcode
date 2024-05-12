class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        column_len = len(grid[0])
        row_len= len(grid)
        state = True
        for index, i in enumerate(grid):
            for index_2, i_2 in enumerate(grid[index]):
                # Check bottom
                if index + 1 < row_len:
                    if grid[index][index_2] != grid[index + 1][index_2]:
                        state = False
                        return state
                # Check right
                if index_2 + 1 < column_len:
                    if grid[index][index_2] == grid[index][index_2 + 1]:
                        state = False
                        return state        
        
        return state
                    
            
