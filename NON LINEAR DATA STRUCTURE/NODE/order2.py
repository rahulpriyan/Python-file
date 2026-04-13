class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
root3=node(10)
root3.left=node(5)
root3.right=node(12)
root3.left.left=node(3)
root3.left.right=node(8)
root3.right.right=node(20)
print("postorder traversal(numbers):")
postorder(root3)
print("\n")