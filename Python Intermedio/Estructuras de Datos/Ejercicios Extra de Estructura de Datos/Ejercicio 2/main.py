class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node

    def __init__(self):
        self.head = None

    def insert_back(self, node): # Inserta a la izquierda
        node.next = self.head
        self.head = node

    def insert_front(self, node): # Inserta a la derecha
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def delete(self, data_to_remove):
        if self.head is None:
            print("Validación: La lista está vacía")
            return False

        if self.head.data == data_to_remove:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == data_to_remove:
                current.next = current.next.next
                return True
            current = current.next

        print(f"Validación: No se encontró '{data_to_remove}'")
        return False

    def print_all(self):
        current = self.head
        print("***\nStatus de la lista:")
        if not current:
            print("La lista está vacía")
        while current:
            print(f"- {current.data}") 
            current = current.next
        print("Final de la lista\n***")


third_node = Node("Soy el tercer nodo")
second_node = Node("Soy el segundo nodo")
first_node = Node("Soy el primer nodo")
fourth_node = Node("Soy el cuarto nodo")

ll1 = LinkedList()
ll1.insert_front(third_node)
ll1.insert_front(second_node)
ll1.insert_front(first_node)
ll1.insert_back(fourth_node)

ll1.print_all()

ll1.delete("Soy el segundo nodo")
ll1.print_all()