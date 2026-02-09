# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: In-order traversal to get sorted values
        sorted_nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # Step 2: Recursively build a balanced tree
        def build_tree(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            root = sorted_nodes[mid]
            
            # Recursively build left and right subtrees
            root.left = build_tree(l, mid - 1)
            root.right = build_tree(mid + 1, r)
            
            return root
        
        return build_tree(0, len(sorted_nodes) - 1)
