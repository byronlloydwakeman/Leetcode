class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def get_max_in_3_by_3(center_x, center_y):
            # Top left going clock-wise
            return max([grid[center_x - 1][center_y + 1],
            grid[center_x][center_y + 1],
            grid[center_x + 1][center_y + 1], 
            grid[center_x + 1][center_y], 
            grid[center_x + 1][center_y - 1], 
            grid[center_x][center_y - 1], 
            grid[center_x - 1][center_y - 1], 
            grid[center_x - 1][center_y],
            grid[center_x][center_y]]) # Center

        # Get the coords of the 3x3 origins
        m = len(grid)
        new_matrix = []
        for i in range(1, m - 1):
            new_matrix.append([])
            for j in range(1, m - 1):
                print(f"i - {i}, j - {j}")
                new_matrix[i - 1].append(get_max_in_3_by_3(i, j))
        
        print(new_matrix)
        return new_matrix

