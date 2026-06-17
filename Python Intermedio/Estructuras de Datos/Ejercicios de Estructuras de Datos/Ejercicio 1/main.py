class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Stack:
  def __init__(self):
    self.head = None

  def push(self, new_node):
    new_node.next = self.head
    self.head = new_node

  def pop(self):
    if self.head is None:
      print("Validación: La pila está vacía")
      return None
    data = self.head.data
    self.head = self.head.next
    return data
  
  def print_stack(self):
    current = self.head
    print("***\nStatus de la pila:")
    while current:
      print("-"+current.data)
      current = current.next
    print("Final de la pila\n***")

  def bubble_sort(self):
    if self.head is None:
      return
    swapped = True
    while swapped:
      swapped = False
      current = self.head
      while current.next:
        if current.data > current.next.data:
          current.data, current.next.data = current.next.data, current.data
          swapped = True
        current = current.next

tercer_nodo = Node("3")
segundo_nodo = Node("2", tercer_nodo)
primer_nodo = Node("1", segundo_nodo)

stack = Stack()
stack.push(primer_nodo)
stack.push(segundo_nodo)
stack.push(tercer_nodo)

# stack.print_stack()

# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

stack.print_stack()

print("Ordenamiento")
stack.bubble_sort()
stack.print_stack()