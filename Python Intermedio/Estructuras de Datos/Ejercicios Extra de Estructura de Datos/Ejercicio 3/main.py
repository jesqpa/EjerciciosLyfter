class Node:
  data: str

  def __init__(self, data, fore=None, next=None):
    self.data = data
    self.fore = fore
    self.next = next

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, node):
    if self.head is None:
      self.head = node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = node
      node.fore = current
  
  def prepend(self, node):
    node.next = self.head
    if self.head:
      self.head.fore = node
    self.head = node

  def delete(self, data_to_remove):
    current = self.head
    while current:
      if current.data == data_to_remove:
        # Si es el primer nodo (head)
        if current == self.head:
          self.head = current.next
          if self.head:
            self.head.fore = None
        # Si está en el medio o al final
        else:
          current.fore.next = current.next
          if current.next:
            current.next.fore = current.fore
        return True # Se eliminó exitosamente
      current = current.next
    return False # No se encontró el nodo

  def print_forward(self):
    current = self.head
    print("***\nImpresión hacia adelante (Forward):")
    if not current:
      print("La lista está vacía")
    while current:
      print("- " + current.data)
      current = current.next
    print("Final de la lista\n***")

  def print_backward(self):
    current = self.head
    print("***\nImpresión hacia atrás (Backward):")
    if not current:
      print("La lista está vacía")
      print("Final de la lista\n***")
      return
      
    # 1. Llegar hasta el último nodo de la lista
    while current.next:
      current = current.next
      
    # 2. Recorrer hacia atrás usando el puntero 'fore'
    while current:
      print("- " + current.data)
      current = current.fore
    print("Final de la lista\n***")


octavo_nodo = Node("Soy el octavo nodo")
setimo_nodo = Node("Soy el séptimo nodo")
sexto_nodo = Node("Soy el sexto nodo")
quinto_nodo = Node("Soy el quinto nodo")
cuarto_nodo = Node("Soy el cuarto nodo")
tercer_nodo = Node("Soy el tercer nodo")
segundo_nodo = Node("Soy el segundo nodo")
primer_nodo = Node("Soy el primer nodo")

# Probando la lista doblemente enlazada
dll = DoublyLinkedList()

# Agregando nodos
dll.append(primer_nodo)
dll.append(segundo_nodo)
dll.append(tercer_nodo)
dll.append(cuarto_nodo)

print("Estado inicial:")
dll.print_forward()
dll.print_backward()

# Eliminando un nodo del medio
print("Eliminando 'Soy el segundo nodo'...")
dll.delete("Soy el segundo nodo")
dll.print_forward()
dll.print_backward()

# Eliminando el head (primer nodo)
print("Eliminando 'Soy el primer nodo'...")
dll.delete("Soy el primer nodo")
dll.print_forward()
