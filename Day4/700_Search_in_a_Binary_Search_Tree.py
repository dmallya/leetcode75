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
        while root:
            if val < root.val and root.left:
                    root = root.left
            elif val > root.val and root.right:
                    root = root.right
            elif root.val == val:
                return root
            else:
                break
        return None

