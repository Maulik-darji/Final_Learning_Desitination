class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.Next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.Next = node2
node2.Next = node3

node3.previous = node2
node2.previous = node1

current = node1
previous = None

print("Printing Forward")
while current is not None:
    print(current.data)
    current = current.Next


print("Printing Backwards")
current = node3
while current is not None:
    print(current.data)
    current = current.previous