class Node:

  __slots__ = ("__value","__next")

  def __init__(self, value):
    self.__value = value
    self.__next = None

  def __str__(self):
    return str(self.__value)

  @property
  def value(self):
    return self.__value

  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise TypeError("El nodo no puede contener valores nulos")
    self.__value = new_value

  @property
  def next(self):
    return self.__next

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next,Node):
      raise TypeError("El next de un nodo, solo puede ser None ó un objeto tipo nodo")
    self.__next = new_next



class slinkedlist:

  __slots__ = ("__head","__tail","__size")

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0


  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self, new_head):
    if new_head is not None and not isinstance(new_head,Node):
      raise TypeError("La cabeza de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
    self.__head = new_head

  @tail.setter
  def tail(self, new_tail):
    if new_tail is not None and not isinstance(new_tail,Node):
      raise TypeError("La cola de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
    self.__tail = new_tail

  @size.setter
  def size(self, new_size):
    if new_size < 0 and not isinstance(new_size,int):
      raise TypeError("El tamaño de una lista enlazada, solo puede ser un numero entero mayor ó igual a cero")
    self.__size = new_size

  def __iter__(self):
    cur_node = self.__head

    while cur_node:
      yield cur_node
      cur_node = cur_node.next

  def __str__(self):
    result = [str(temp_node.value) for temp_node in self]
    return ' --> '.join(result)


  def prepend(self, new_value):
    new_node = Node(new_value)

    new_node.next = self.__head
    if self.__head is None:
      self.__tail = new_node
    self.__head = new_node

    self.__size += 1

  def append(self, new_value):
    new_node = Node(new_value)

    if self.__head is None:
      self.__head = new_node
    else:
      self.__tail.next = new_node

    self.__tail = new_node
    self.__size += 1

  def getbyIndex(self, index):

    if not isinstance(index,int) or index > self.__size -1 or index < -1:
      raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

    if index == 0:
      return self.head.value
    elif index == -1 or index == self.__size -1:
      return self.__tail.value
    else:
      index_temp = 0

      for cur_node in self:
        if index_temp == index:
          return cur_node.value
        index_temp += 1


  def getNodebyIndex(self, index):

      if not isinstance(index,int) or index > self.__size -1 or index < -1:
        raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")

      if index == 0:
        return self.head
      elif index == -1 or index == self.__size -1:
        return self.__tail
      else:
        index_temp = 0

        for cur_node in self:
          if index_temp == index:
            return cur_node
          index_temp += 1


  def InsertbyIndex(self, index, new_value):

    if not isinstance(index,int) or index > self.__size or index < -1:
        raise TypeError("el parametro indice esta por fuera de rango ó es un valor del tipo incorrecto")


    if index == 0:
       self.prepend(new_value)
    elif index == -1 or index == self.__size:
       self.append(new_value)
    else:
        new_node = Node(new_value)
        prev_node = self.getNodebyIndex(index-1)
        print("prev_node", prev_node)
        print("new_node", new_node)

        new_node.next = prev_node.next
        prev_node.next = new_node
        self.__size += 1


  def searchvalue(self, value_to_find):
        for cur_node in self:
          if value_to_find == cur_node.value:
            return True

        return False

  def set_newvalue(self, value, new_value):
        for cur_node in self:
          if value == cur_node.value:
            cur_node.value = new_value

        return False

  def popfirst(self):
    if self.__head is None:
      raise TypeError("No hay elementos para retornar")
    elif self.__head is self.__tail:
      temp_value = self.__head.value
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      temp_value = self.__head.value
      self.__head = self.__head.next
      self.__size -= 1

    return temp_value


  def pop(self):
    if self.__head is None:
      raise TypeError("No hay elementos para retornar")
    elif self.__head is self.__tail:
      temp_value = self.__head.value
      self.__head = None
      self.__tail = None
      self.__size = 0
    else:
      temp_value = self.__tail.value

      for cur_node in self:
        if cur_node.next is self.__tail:
          prev_tail = cur_node

      prev_tail.next = None
      self.__tail = prev_tail
      self.__size -= 1

    return temp_value
class Queue:

  def __init__(self):
    self.__q = slinkedlist()

  def __str__(self):
    result = [str(nodo.value) for nodo in self.__q]
    return '--'.join(result)

  def enqueue(self,e):
    self.__q.append(e)
    return True

  def dequeue(self):
    if not self.is_empty():
      return self.__q.popfirst()
    else:
      raise TypeError("La cola esta vacia, no hay elementos para desencolar")

  def first(self):
    if not self.is_empty():
      #return self.__q.getbyIndex(0)
      return self.__q.head.value
    else:
      raise TypeError("La cola esta vacia, no hay elementos para leer")

  def is_empty(self):
    return self.__q.size == 0

  def len(self):
    return self.__q.size

class Stack:

  def __init__(self):
    self.__s = slinkedlist()

  def __str__(self):
    result = [str(nodo.value) for nodo in self.__s ]
    return '||'.join(result)

  def push(self,e):
    self.__s.append(e)
    return True

  def pop(self):
    if not self.is_empty():
      return self.__s.pop()
    else:
      raise TypeError("La pila esta vacia, no hay elementos para desapilar")

  def top(self):
    if not self.is_empty():
      #return self.__q.getbyIndex(0)
      return self.__s.tail.value
    else:
      raise TypeError("La pila esta vacia, no hay elementos para leer")

  def is_empty(self):
    return self.__s.size == 0

  def len(self):
    return self.__s.size
class Paquete:

    def __init__(self, source: int, destination: int, timestamp: int) -> None:
        self.source: int = source
        self.destination: int = destination
        self.timestamp: int = timestamp

    def __str__(self) -> str:
        return f"({self.source},{self.destination},{self.timestamp})"


class Router:

    def __init__(self, limiteMemoria: int):
        self.limiteMemoria: int = limiteMemoria
        self.cola: Queue = Queue()

    def agregarPaquete(self, source: int, destination: int, timestamp: int) -> bool:
        nuevo: Paquete = Paquete(source, destination, timestamp)
        n: int = self.cola.len()
        encontrado: bool = False
        contador: int = 0

        while contador < n:

            actual: Paquete = self.cola.dequeue()

            if actual.source == nuevo.source and actual.destination == nuevo.destination and actual.timestamp == nuevo.timestamp:
                encontrado = True

            self.cola.enqueue(actual)
            contador += 1

        if encontrado:
            return False

        if self.cola.len() >= self.limiteMemoria:
            self.cola.dequeue()

        self.cola.enqueue(nuevo)

        return True

    def reenviarPaquete(self) -> list[int]:
        if self.cola.is_empty():
            return []

        paquete: Paquete = self.cola.dequeue()

        return [paquete.source, paquete.destination, paquete.timestamp]

    def contarPaquetes(self, destination: int, startTime: int, endTime: int) -> int:
        n: int = self.cola.len()
        contador: int = 0
        total: int = 0

        while contador < n:

            actual: Paquete = self.cola.dequeue()

            if actual.destination == destination and startTime <= actual.timestamp <= endTime:
                total += 1

            self.cola.enqueue(actual)
            contador += 1

        return total
# 2

class Operacion:

    def __init__(self, tipo: str, valor: str) -> None:
        self.tipo: str = tipo
        self.valor: str = valor


class Editor:

    def __init__(self):
        self.texto: str = ""
        self.pila: Stack = Stack()

    def agregarTexto(self, texto: str) -> None:
        operacion: Operacion = Operacion("append", self.texto)
        self.pila.push(operacion)

        self.texto += texto

    def eliminarTexto(self, cantidad: int) -> None:
        operacion: Operacion = Operacion("delete", self.texto)
        self.pila.push(operacion)

        self.texto = self.texto[:-cantidad]

    def imprimirCaracter(self, posicion: int) -> None:
        print(self.texto[posicion - 1])

    def deshacer(self) -> None:
        if not self.pila.is_empty():
            operacion: Operacion = self.pila.pop()
            self.texto = operacion.valor
# 3

class Estudiante:

    def __init__(self, preferencia: int, intentosRestantes: int) -> None:
        self.preferencia: int = preferencia
        self.intentosRestantes: int = intentosRestantes

def simularCafeteria(students: list[int], sandwiches: list[int]) -> tuple[int, int]:

    cola = Queue()
    pila = Stack()

    for pref in students:
        cola.enqueue(Estudiante)(pref, 2)

    for sandwich in reversed(sandwiches):
        pila.push(sandwich)

    noComieron = 0

    while not cola.is_empty() and not pila.is_empty():
        estudiante = cola.dequeue()
        if estudiante.preferencia == pila.top():
            pila.pop()
        else:
            estudiante.intentosRestantes -= 1
            if estudiante.intentosRestantes > 0:
                cola.enqueue(estudiante)
            else:
                noComieron += 1

    noComieron += cola.len()

    return noComieron, pila.len()
# 4

def postfija(s):

    stack = Stack()

    for character in s:

        if character.isdigit():
            stack.push(int(character))

        else:
            second = stack.pop()
            first = stack.pop()

            if character == "+":
                result = first + second

            elif character == "-":
                result = first - second

            elif character == "x":
                result = first * second

            elif character == "*":
                result = first * second

            elif character == "/":
                result = first / second

            stack.push(result)

    return stack.pop()
print("PUNTO 1")

router = Router(3)

print(router.addPacket(1, 10, 100))
print(router.addPacket(2, 20, 200))
print(router.addPacket(3, 10, 300))
print(router.addPacket(1, 10, 100))
print(router.getCount(10, 50, 350))
print(router.forwardPacket())
print(router.forwardPacket())
print(router.forwardPacket())
print(router.forwardPacket())

router = Router(3)

router.addPacket(1, 10, 100)
router.addPacket(2, 20, 200)
router.addPacket(3, 10, 300)
router.addPacket(4, 30, 400)

print("PUNTO 2")

editor = Editor()

editor.append("abc")
print(editor.get_text())

editor.append("xy")
print(editor.get_text())

editor.print_char(4)

editor.delete(3)
print(editor.get_text())

editor.print_char(2)

editor.undo()
print(editor.get_text())

editor.print_char(5)

editor.undo()
print(editor.get_text())

print("PUNTO 3")

students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]

print(simularCafeteria(students, sandwiches))

students = [1, 1, 1]
sandwiches = [0, 0, 0]

print(simularCafeteria(students, sandwiches))

print("PUNTO 4")

print(postfija("43+"))
print(postfija("35x83+-"))