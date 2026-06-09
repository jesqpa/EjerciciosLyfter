class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class DoubleEndedQueue:
  def __init__(self):
    self.head = None

  def push_left (self, new_node):
    new_node.next = self.head
    self.head = new_node

  def push_right(self, new_node):
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
  
  def pop_left(self):
    if self.head is None:
      print("Validación: La cola está vacía")
      return None
    data = self.head.data
    self.head = self.head.next
    return data
  
  def pop_right(self):
    if self.head is None:
      print("Validación: La cola está vacía")
      return None
    if self.head.next is None:
      data = self.head.data
      self.head = None
      return data
    current = self.head
    while current.next.next:
      current = current.next
    data = current.next.data
    current.next = None
    return data
  
  def print_double_ended_queue(self):
    current = self.head
    print("***\nStatus de la estructura:")
    while current:
      print("-"+current.data)
      current = current.next
    print("Final de la estructura\n***")

octavo_nodo = Node("Soy el octavo nodo")
setimo_nodo = Node("Soy el séptimo nodo")
sexto_nodo = Node("Soy el sexto nodo")
quinto_nodo = Node("Soy el quinto nodo")
cuarto_nodo = Node("Soy el cuarto nodo")
tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo")
primer_nodo = Node("Soy el primer nodo")

deq = DoubleEndedQueue()
deq.push_left(primer_nodo)
deq.push_right(segundo_nodo)
deq.push_left(tercer_nodo)
deq.push_right(cuarto_nodo)
deq.push_left(quinto_nodo)
deq.push_right(sexto_nodo)
deq.push_left(setimo_nodo)
deq.push_right(octavo_nodo)

deq.print_double_ended_queue()

# deq.pop_left()
# deq.pop_left()
# deq.pop_left()
# deq.pop_left()

# deq.print_double_ended_queue()