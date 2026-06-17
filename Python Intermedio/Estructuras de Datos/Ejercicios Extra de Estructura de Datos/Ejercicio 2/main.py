class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head    

    def insert_front(self, node):
        node.next = self.head
        self.head = node

    
    def insert_back(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    
    def delete(self):
        if self.head is None:
            print("Validación: La lista está vacía")
            return
        self.head = self.head.next

    def print_all(self):
        current = self.head
        print("***\nStatus de la lista:")
        while current:
            print("-"+current.data)
            current = current.next
        print("Final de la lista\n***")


fourth_node = Node("Soy el cuarto nodo")
third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo") 
first_node = Node("Soy el primer nodo")

ll1 = LinkedList(first_node)
ll1.insert_back(second_node)
ll1.insert_back(third_node)
ll1.insert_back(fourth_node)

ll1.print_all()
ll1.delete()
ll1.print_all()