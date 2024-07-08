# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    subtree = []
    found = False

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        if val < root.val and root.left:
                self.searchBST(root.left, val)
        if val > root.val and root.right:
                self.searchBST(root.right, val)
        if not root.left and not root.right and root.val != val:
            return []

