class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head: Node

    def __init__(self, head):
        self.head = head    

    def enqueue(self, node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node

    def dequeue(self):
        current_node = self.head
        if self.head:
          self.head = self.head.next
        return current_node.data
          
    def print_all(self):
        current_node = self.head
        print("***\nStatus de la cola:")
        while current_node is not None:
            print("-"+current_node.data)
            current_node = current_node.next
        print("Final de la cola\n***")

first_node = Node("Primero")
q1 = Queue(first_node)
# my_queue.print_structure()

second_node = Node("Segundo")
q1.enqueue(second_node)

third_node = Node("Tercero")
q1.enqueue(third_node)

forth = Node("Cuarto")
q1.enqueue(forth)

q1.print_all()

q1.dequeue()

q1.print_all()
