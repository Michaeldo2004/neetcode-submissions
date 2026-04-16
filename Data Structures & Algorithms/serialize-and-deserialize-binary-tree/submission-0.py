# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        r = ""
        def dfs(node):
            nonlocal r
            if not node:
                r += ",#"
                return
            
            r += "," + str(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return r[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dummy = TreeNode()
        head = dummy
        datalist = deque(data.split(','))


        def dfs():
            nonlocal datalist
            if not datalist:
                return None
            
            temp_val = datalist.popleft()

            if temp_val != '#':
                node = TreeNode(temp_val)
                node.left = dfs()
                node.right = dfs()
                return node
            else:
                return None
        return dfs()
            


