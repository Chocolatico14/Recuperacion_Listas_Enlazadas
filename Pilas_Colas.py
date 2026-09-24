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

class Router:

    def __init__(self, memoryLimit):
        self.__memoryLimit = memoryLimit
        self.__packets = Queue()

    def addPacket(self, source, destination, timestamp):

        temp = Queue()
        duplicate = False

        while not self.__packets.is_empty():
            packet = self.__packets.dequeue()

            if packet[0] == source and packet[1] == destination and packet[2] == timestamp:
                duplicate = True

            temp.enqueue(packet)

        self.__packets = temp

        if duplicate:
            return False

        if self.__packets.len() >= self.__memoryLimit:
            self.__packets.dequeue()

        self.__packets.enqueue((source, destination, timestamp))

        return True

    def forwardPacket(self):

        if self.__packets.is_empty():
            return []

        packet = self.__packets.dequeue()

        return [packet[0], packet[1], packet[2]]

    def getCount(self, destination, startTime, endTime):

        temp = Queue()
        count = 0

        while not self.__packets.is_empty():
            packet = self.__packets.dequeue()

            if packet[1] == destination and startTime <= packet[2] <= endTime:
                count += 1

            temp.enqueue(packet)

        self.__packets = temp

        return count

# 2

class Editor:

    def __init__(self):
        self.__text = ""
        self.__history = Stack()

    def append(self, string):

        self.__history.push(self.__text)
        self.__text += string

    def delete(self, k):

        self.__history.push(self.__text)
        self.__text = self.__text[:-k]

    def print_char(self, k):

        print(self.__text[k - 1])

    def undo(self):

        if not self.__history.is_empty():
            self.__text = self.__history.pop()

    def get_text(self):

        return self.__text
# 3

def cafeteria(students, sandwiches):

    queue = Queue()
    stack = Stack()

    for student in students:
        queue.enqueue((student, 0))

    for sandwich in reversed(sandwiches):
        stack.push(sandwich)

    while not queue.is_empty() and not stack.is_empty():

        student = queue.dequeue()
        preference = student[0]
        retries = student[1]

        if preference == stack.top():
            stack.pop()

        else:
            if retries < 2:
                queue.enqueue((preference, retries + 1))

    return queue.len(), stack.len()

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

print(cafeteria(students, sandwiches))

students = [1, 1, 1]
sandwiches = [0, 0, 0]

print(cafeteria(students, sandwiches))

print("PUNTO 4")

print(postfija("43+"))
print(postfija("35x83+-"))