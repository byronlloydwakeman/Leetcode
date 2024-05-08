from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000" # Creating a start point
        
        # Function to generate neighboring lock combinations
        def get_neighbors(lock):
            neighbors = []
            for i in range(4):
                for move in (-1, 1):
                    new_digit = (int(lock[i]) + move) % 10
                    new_lock = lock[:i] + str(new_digit) + lock[i+1:]
                    neighbors.append(new_lock)
            return neighbors
        
        # Initialize BFS
        queue = deque([(start, 0)])
        # Adding the deadends to the queue makes sure they don't get explored further
        visited = set(deadends)
        visited.add(start)
        
        # Perform BFS
        while queue:
            current_lock, moves = queue.popleft()
            # If we've found the correct combo
            if current_lock == target:
                return moves
            for neighbor in get_neighbors(current_lock):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, moves + 1))
        
        # If target lock cannot be reached
        return -1
