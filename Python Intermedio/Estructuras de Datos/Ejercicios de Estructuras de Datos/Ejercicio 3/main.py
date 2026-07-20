class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class BinaryTree:
  def __init__(self):
    self.root = None

  def set_root(self, node):
    """Establece el nodo raíz del árbol"""
    self.root = node

  def insert(self, parent_node, left_node, right_node):
    """Conecta dos nodos como hijos de un nodo padre"""
    parent_node.left = left_node
    parent_node.right = right_node
  
  def print_tree(self, node=None, depth=0):
    """Imprime el árbol recursivamente (de arriba a abajo, izquierda a derecha)"""
    if node is None:
      node = self.root
    
    if node is None:
      print("Validación: El árbol está vacío")
      return
    
    print(f"{'  ' * depth}{node.data}")
    
    if node.left:
      self.print_tree(node.left, depth + 1)
    if node.right:
      self.print_tree(node.right, depth + 1)


# Crear nodos independientes
primer_nodo = Node("Soy el primer nodo")
segundo_nodo = Node("Soy el segundo nodo")
tercer_nodo = Node("Soy el tercer nodo")
cuarto_nodo = Node("Soy el cuarto nodo")
quinto_nodo = Node("Soy el quinto nodo")

# Crear árbol binario
tree = BinaryTree()
tree.set_root(primer_nodo)

# Conectar nodos: padre, hijo izquierdo, hijo derecho
tree.insert(primer_nodo, segundo_nodo, tercer_nodo)
tree.insert(segundo_nodo, cuarto_nodo, quinto_nodo)

print("***\nÁrbol Binario:")
tree.print_tree()
print("Final del árbol\n***")