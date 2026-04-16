# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        tree = {i: idx for idx, i in enumerate(inorder)} # val: index
        def dfs(i, l, r):
            if i == len(preorder):
                return
            if l > r: return

            root = TreeNode(preorder[i])
            mid = tree[preorder[i]]
            root.left = dfs(i+1, l, mid-1)
            root.right = dfs(i+1 + mid-l, mid+1, r)
            return root
        return dfs(0, 0, len(preorder)-1)


