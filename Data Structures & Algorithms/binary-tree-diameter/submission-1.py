# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max to pass
        maxlen = [0]
        def sum_length(node, maxlen):
            if not node:
                return -1

            left_len = sum_length(node.left, maxlen) + 1
            right_len = sum_length(node.right, maxlen) + 1

            maxlen[0] = max(maxlen[0], left_len + right_len)

            return max(left_len, right_len)

        sum_length(root, maxlen)

        return maxlen[0]
