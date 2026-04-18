"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        q = deque()
        seen = {}

        q.append(node)
        seen[node] = Node(node.val)

        while(len(q) > 0):
            tempNode = q.popleft()
           
            for neighborNode in tempNode.neighbors:
                if neighborNode not in seen:
                    seen[neighborNode] = Node(neighborNode.val)
                    q.append(neighborNode)
                seen[tempNode].neighbors.append(seen[neighborNode])
        return seen[node]

