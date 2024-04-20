class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        columns = len(grid[0])
        rows = len(grid)
        islands = []

        def combineIslands(indicies):
            nonlocal islands
            jagged_array = []
            # First add the islands to the array
            for index in indicies:
                jagged_array.append(islands[index])

            islands = [value for index, value in enumerate(islands) if index not in indicies]

            islands.append([item for sublist in jagged_array for item in sublist])

        # Returns the index of adjacent islands, if if connects two islands, then we need to combine the arrays
        def checkAdjacent(row_index, column_index):
            # All connecting islands (could be more than one)
            island_indicies = []

            # left 
            if column_index > 0:
                for island_index, island in enumerate(islands):
                    if [row_index, column_index - 1] in island:
                        island_indicies.append(island_index)
            # right
            if column_index < columns - 1:
                for island_index, island in enumerate(islands):
                    if [row_index, column_index + 1] in island:
                        island_indicies.append(island_index)
            # top
            if row_index > 0:   
                for island_index, island in enumerate(islands):
                    if [row_index - 1, column_index] in island:
                        island_indicies.append(island_index)
            # bottom
            if row_index < rows - 1:
                for island_index, island in enumerate(islands):
                    if [row_index + 1, column_index] in island:
                        island_indicies.append(island_index)


            # Not interested if it touches the same island twice
            island_indicies = list(set(island_indicies))

            return island_indicies


        # A 1 needs an adjacent 1 to be part of an island, if not it is an island of 1
        # islands is an array of the indicies of connected lands (islands)
        # We check if the 1 is adjacent to any of the current islands, if not make a new island
        # Return the number of islands
        for row_index, el in enumerate(grid):
            for column_index, el2 in enumerate(el):
                if el2 == "1":
                    island_indices = checkAdjacent(row_index, column_index)

                    if island_indices:
                        # Add the current cell to the last island if touching multiple islands
                        islands[island_indices[-1]].append([row_index, column_index])
                        
                        # Combine islands if touching multiple
                        if len(island_indices) > 1:
                            combineIslands(island_indices)
                    else:
                        # If not adjacent to any island, create a new island
                        islands.append([[row_index, column_index]])


        return len(islands)
