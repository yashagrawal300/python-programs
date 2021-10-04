# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
	        return True

        stack, result = [], []
        while stack or root:
        	if root:
        		stack.append(root)
        		root = root.left
        	else:
        		root = stack.pop()
        		result.append(root.val)
        		root = root.right

        previous = result[0]
        for index in range(1, len(result)):
        	if previous >= result[index]:
        		return False
        	previous = result[index]
        return True
