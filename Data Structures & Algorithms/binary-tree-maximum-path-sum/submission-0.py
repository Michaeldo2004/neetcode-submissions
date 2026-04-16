# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        glb_max = -float("inf")
        def dfs(node):
            nonlocal glb_max
            if not node:
                return 0
            l_gain = max(dfs(node.left), 0)
            r_gain = max(dfs(node.right), 0)
            glb_max = max(glb_max, node.val + l_gain + r_gain)


            return node.val + max(l_gain, r_gain)
        dfs(root)
        return glb_max