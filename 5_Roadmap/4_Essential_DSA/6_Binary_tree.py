# Binary Tree Node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the Binary Tree

root = Node(10)

root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)
root.left.right = Node(50)


# Inorder Traversal
# Left -> Root -> Right

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data)
    inorder(root.right)


# Preorder Traversal
# Root -> Left -> Right

def preorder(root):
    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)


# Postorder Traversal
# Left -> Right -> Root

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data)


# Call all three traversals

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)