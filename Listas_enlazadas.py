class NodeD:

    __slots__ = ("__value","__next","__prev")

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def __str__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @value.setter
    def value(self, new_value):
        if new_value is None:
            raise TypeError("El nodo no puede contener valores nulos")
        self.__value = new_value

    @next.setter
    def next(self, new_next):
        if new_next is not None and not isinstance(new_next,NodeD):
            raise TypeError("El next de un nodo, solo puede ser None ó un objeto tipo nodo")
        self.__next = new_next

    @prev.setter
    def prev(self, new_prev):
        if new_prev is not None and not isinstance(new_prev,NodeD):
            raise TypeError("El next de un nodo, solo puede ser None ó un objeto tipo nodo")
        self.__prev = new_prev




class dlinkedlist:

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
        if new_head is not None and not isinstance(new_head,NodeD):
            raise TypeError("La cabeza de una lista enlazada, solo puede ser None ó un objeto tipo nodo")
        self.__head = new_head

    @tail.setter
    def tail(self, new_tail):
        if new_tail is not None and not isinstance(new_tail,NodeD):
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
        return ' <--> '.join(result)


    def prepend(self, new_value):
        new_node = NodeD(new_value)

        new_node.next = self.__head
        if self.__head is None:
            self.__tail = new_node
        else:
            self.__head.prev = new_node

        self.__head = new_node
        self.__size += 1

    def append(self, new_value):
        new_node = NodeD(new_value)

        if self.__head is None:
            self.__head = new_node
        else:
            self.__tail.next = new_node

        new_node.prev = self.__tail
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
            new_node = NodeD(new_value)
            prev_node = self.getNodebyIndex(index-1)
            next_node = prev_node.next
            print("prev_node", prev_node)
            print("new_node", new_node)
            print("next_node",next_node)

            print("new_node.next antes", new_node.next)
            new_node.next = next_node
            print("new_node.next despues", new_node.next)
            print("prev_node.next antes", prev_node.next)
            prev_node.next = new_node
            print("prev_node.next despues", prev_node.next)
            new_node.prev = prev_node
            print("new_node.prev despues", new_node.prev)
            print("next_node.prev antes", next_node.prev)
            next_node.prev = new_node
            print("next_node.prev despues", next_node.prev)

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
            self.__head.prev = None
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
            prev_tail = self.__tail.prev
            print("prev_tail :", prev_tail)
            prev_tail.next = None

            self.__tail = prev_tail
            self.__size -= 1


        return temp_value

#Punto 1

class Tren:

    def __init__(self, vagon):
        self.lista = dlinkedlist()
        self.lista.append(vagon)

        self.vagon_actual = self.lista.head

    def mover_siguiente(self):
        if self.vagon_actual and self.vagon_actual.next:
            self.vagon_actual = self.vagon_actual.next
            print(f"Se avanzo al vagon: {self.vagon_actual.value}")
        else:
            print(f"No hay vagon siguiente, permanece en el vagon: {self.vagon_actual.value}")

    def mover_anterior(self):
        if self.vagon_actual and self.vagon_actual.prev:
            self.vagon_actual = self.vagon_actual.prev
            print(f"Se devolvio al vagon: {self.vagon_actual.value}")
        else:
            print(f"No hay vagon anterior, permanece en el vagon: {self.vagon_actual.value}")

    def acomplar_vagon(self, nuevo_vagon):
        if self.vagon_actual is None:
            self.lista.append(nuevo_vagon)
            self.vagon_actual = self.lista.head
            return

        nuevo_nodo = NodeD(nuevo_vagon)
        nodo_siguiente = self.vagon_actual.next

        nuevo_nodo.prev = self.vagon_actual
        nuevo_nodo.next = nodo_siguiente

        self.vagon_actual.next = nuevo_nodo

        if nodo_siguiente is not None:
            nodo_siguiente.prev = nuevo_nodo
        else:
            self.lista.tail = nuevo_nodo

        self.lista.size += 1
        print(f"Vagon {nuevo_vagon} acoplado correctamente")

    def desacoplar_vagon_actual(self):
        if self.vagon_actual is None:
            print("El tren esta vacio")
            return None

        nodo_eliminar = self.vagon_actual
        siguiente_nodo = self.vagon_actual.next
        nodo_anterior = self.vagon_actual.prev

        if nodo_anterior:
            nodo_anterior.next = siguiente_nodo
        else:
            self.lista.head = siguiente_nodo

        if siguiente_nodo:
            siguiente_nodo.prev = nodo_anterior
        else:
            self.lista.tail = nodo_anterior

        self.lista.size -= 1

        if siguiente_nodo:
            self.vagon_actual = siguiente_nodo
        elif nodo_anterior:
            self.vagon_actual = nodo_anterior
        else:
            self.vagon_actual = None

        print(f"Vagon {nodo_eliminar.value} desacoplado")

    def vagon_inicio(self):
        if self.vagon_actual is None or self.vagon_actual is self.lista.head:
            return

        nodo = self.vagon_actual

        if nodo.prev:
            nodo.prev.next = nodo.next
        if nodo.next:
            nodo.next.prev = nodo.prev
        else:
            self.lista.tail = nodo.prev

        nodo.prev = None
        nodo.next = self.lista.head
        self.lista.head.prev = nodo
        self.lista.head = nodo

    def vagon_final(self):
        if self.vagon_actual is None or self.vagon_actual is self.lista.tail:
            return

        nodo = self.vagon_actual

        if nodo.next:
            nodo.next.prev = nodo.prev
        if nodo.prev:
            nodo.prev.next = nodo.next
        else:
            self.lista.head = nodo.next

        nodo.next = None
        nodo.prev = self.lista.tail
        self.lista.tail.next = nodo
        self.lista.tail = nodo

    def __str__(self):
        if self.vagon_actual:
            vagon_str = str(self.vagon_actual.value)
        else:
            "Ninguno"

        return (f"Estado del Tren: {self.lista} | Vagon Actual: {vagon_str}")

#Punto 2

def fusionar_segmentos(lista):

    if lista.head is None:
        return None

    current = lista.head
    suma = 0

    nuevo_head = None
    ultimo = None

    while current is not None:

        if current.value != 0:
            suma += current.value

        else:
            if suma > 0:
                current.value = suma

                if nuevo_head is None:
                    nuevo_head = current

                if ultimo is not None:
                    ultimo.next = current
                    current.prev = ultimo

                ultimo = current
                suma = 0

        current = current.next

    if ultimo is not None:
        ultimo.next = None
        lista.tail = ultimo

    lista.head = nuevo_head

    return lista


#Punto 3

def eliminar_duplicados(lista):
    if lista.head is None:
        return None
    
    current = lista.head

    while current is not None:

        siguiente = current.next
        buscador = current.next
        repetido = False

        while buscador is not None:

            if buscador.value == current.value:
                repetido = True
                break

            buscador = buscador.next

        if repetido:

            if current.prev is not None:
                current.prev.next = current.next

            if current.next is not None:
                current.next.prev = current.prev

            if current == lista.head:
                lista.head = current.next

            if current == lista.tail:
                lista.tail = current.prev

        current = siguiente

    return lista

#Punto 4

def rotar_maximo(lista):

    if lista.head is None:
        return None

    maximo = lista.head
    current = lista.head.next

    while current is not None:
        if current.value > maximo.value:
            maximo = current
        current = current.next

    if maximo == lista.head:
        return lista

    anterior = maximo.prev
    vieja_head = lista.head

    anterior.next = None
    maximo.prev = None

    lista.tail.next = vieja_head
    vieja_head.prev = lista.tail

    lista.head = maximo
    lista.tail = anterior

    return lista
        
        


   

            
            
            
    
        
