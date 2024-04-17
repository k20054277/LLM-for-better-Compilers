
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Function to create a linked list
def create_linked_list():
    nodes = []
    head = Node()
    nodes.append(head)
    node1 = Node("First")
    nodes.append(node1)
    head.next = node1
    node2 = Node("Second")
    nodes.append(node2)
    node1.next = node2
    return nodes

# Function to print a linked list
def print_linked_list(nodes):
    current = nodes[0]
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    linked_list = create_linked_list()
    print("Linked List:")
    print_linked_list(linked_list)

    # Checking for None in the linked list
    current = nodes[0]
    while current is not None:
        if current is nodes[-1]:  # last node
            print(f"The last node data is: {current.data}")
            break
        current = current.next

    # Iterating through the linked list using iter() and next() functions
    iterator = iter(linked_list)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass
