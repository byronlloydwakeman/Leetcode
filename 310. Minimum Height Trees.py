from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case where the depth is 1
        if n == 1:
            return [0]

        # Build adjacency list
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # Initialize leaves
        leaves = [node for node in adjacency_list if len(adjacency_list[node]) == 1]

        # Bit confusing, there can only be one or two roots, as by definition a tree can only have one edge
        while n > 2:
            # As we're looping through leaves we need to reduce n by the number of iterations
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adjacency_list[leaf].pop()
                adjacency_list[neighbor].remove(leaf)
                if len(adjacency_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves
