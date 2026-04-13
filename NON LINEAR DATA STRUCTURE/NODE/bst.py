class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def count_leaves(root):
    if root is None:
        return 0
    if root.left is none and root.right is none:
        return 1
    return count_leaves(root)