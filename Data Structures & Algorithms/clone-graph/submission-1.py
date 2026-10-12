"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node: Optional['Node']):
            node_cpy = Node(node.val)
            visited[node.val] = node_cpy
            for adj in node.neighbors:
                if adj.val in visited:
                    adj_cpy = visited[adj.val]
                else:
                    adj_cpy = dfs(adj)
                
                node_cpy.neighbors.append(adj_cpy)
                # 也會改到 visited[node.val] 的 value

            return node_cpy

        if node is None:
            return None

        return dfs(node)