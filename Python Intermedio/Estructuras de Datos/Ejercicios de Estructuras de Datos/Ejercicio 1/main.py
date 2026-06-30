class Node:
  data: str

  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class Queue:
  def __init__(self):
    self.head = None  # Lista vacía por defecto

  def enqueue(self, data):
    """
    Método para agregar elementos a la cola.
    RECEBE el DATO DIRECTAMENTE, no un nodo.
    """
    # Crear el nodo internamente
    new_node = Node(data)

    # Caso 1: La cola está vacía
    if self.head is None:
      self.head = new_node
    # Caso 2: La cola tiene elementos
    else:
      current = self.head
      # Moverse hasta el último nodo
      while current.next:
        current = current.next
      # Conectar el nuevo nodo al final
      current.next = new_node

  def dequeue(self):
    """
    Método para eliminar el elemento del inicio de la cola.
    """
    if self.head is None:
      print("Validación: La cola está vacía")
      return None

    data = self.head.data
    self.head = self.head.next
    return data

  def print_queue(self):
    """Imprime los elementos de la cola"""
    current = self.head
    print("***\nStatus de la cola:")
    if not current:
      print("La cola está vacía")
    while current:
      print("- " + current.data)
      current = current.next
    print("Final de la cola\n***")


# --- CASO 1: Cola vacía ---

print("========== CASO 1: Cola vacía ==========")
queue1 = Queue()  # ✅ Crear cola vacía
queue1.print_queue()  # Imprimir

# Agregar elementos con enqueue
queue1.enqueue("primer dato")
queue1.enqueue("segundo dato")
queue1.enqueue("tercer dato")

print("\nDespués de agregar 3 elementos:")
queue1.print_queue()


# --- CASO 2: Cola no vacía ---

print("\n========== CASO 2: Cola no vacía ==========")
queue2 = Queue()  # ✅ Crear cola vacía
queue2.enqueue("a")
queue2.enqueue("b")
queue2.enqueue("c")

print("Estado inicial:")
queue2.print_queue()

print("\nDequeue (quitar elemento del inicio):")
queue2.dequeue()  # Elimina "a"
queue2.print_queue()

print("\nDequeue (otra vez):")
queue2.dequeue()  # Elimina "b"
queue2.print_queue()


# --- CASO 3: Cola vacía al intentar dequeue ---

print("\n========== CASO 3: Cola vacía al dequeue ==========")
queue3 = Queue()
queue3.enqueue("Solo un dato")

print("Estado antes de dequeue:")
queue3.print_queue()

print("\nDequeue:")
queue3.dequeue()  # Elimina el dato

print("\nEstado después de dequeue:")
queue3.print_queue()

print("\nIntentar dequeue cuando está vacía:")
queue3.dequeue()  # ❌ Muestra mensaje de validación
queue3.print_queue()