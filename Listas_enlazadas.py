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
        nodo_siguiente = self.vagon_actual.next # C (porque no hemos guardado todavia X)

        nuevo_nodo.prev = self.vagon_actual  # B
        nuevo_nodo.next = nodo_siguiente # C

        self.vagon_actual.next = nuevo_nodo # X

        if nodo_siguiente is not None:
            nodo_siguiente.prev = nuevo_nodo # X
        else:
            self.lista.tail = nuevo_nodo # X LA COLA DEL TREN PORQUE NO HAY SIGUIENTE

        self.lista.size += 1
        print(f"Vagon {nuevo_vagon} acoplado correctamente")

    def desacoplar_vagon_actual(self):
        if self.vagon_actual is None:
            print("El tren esta vacio")
            return None

        nodo_eliminar = self.vagon_actual  # B
        siguiente_nodo = self.vagon_actual.next # C
        nodo_anterior = self.vagon_actual.prev # A

        if nodo_anterior:
            nodo_anterior.next = siguiente_nodo # A - C
        else:
            self.lista.head = siguiente_nodo # C seria la cabeza

        if siguiente_nodo:
            siguiente_nodo.prev = nodo_anterior # C TIRANDO A 
        else:
            self.lista.tail = nodo_anterior

        self.lista.size -= 1

        if siguiente_nodo:
            self.vagon_actual = siguiente_nodo # C seria el actual
        elif nodo_anterior:
            self.vagon_actual = nodo_anterior # A seria el actual
        else:
            self.vagon_actual = None

        print(f"Vagon {nodo_eliminar.value} desacoplado")

    def vagon_inicio(self):
        if self.vagon_actual is None or self.vagon_actual is self.lista.head:
            return

        nodo = self.vagon_actual

        if nodo.prev: # B
            nodo.prev.next = nodo.next # C
        if nodo.next: # D
            nodo.next.prev = nodo.prev # C 
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
            nodo.next.prev = nodo.prev # C - A
        if nodo.prev:
            nodo.prev.next = nodo.next # A - C
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

        if repetido: #AQUI EL REPETIDO ES B.. entonces..

            if current.prev is not None: # B is not none
                current.prev.next = current.next # A - C

            if current.next is not None: # B is not none
                current.next.prev = current.prev # C - A

            if current == lista.head: # si era la cabeza el duplicado, se pone en el siguiente
                lista.head = current.next

            if current == lista.tail: # lo mismo
                lista.tail = current.prev

        current = siguiente

    return lista

#Punto 4

def rotar_maximo(lista):

    if lista.head is None:
        return None

    maximo = lista.head # 4 maximo
    current = lista.head.next # 8 current

    while current is not None:
        if current.value > maximo.value: # 4 y 8, maximo 8 y luego 8-10, maximo 10
            maximo = current
        current = current.next

    if maximo == lista.head:
        return lista

    anterior = maximo.prev
    vieja_head = lista.head

    anterior.next = None
    maximo.prev = None # se rompe la conexion

    lista.tail.next = vieja_head # 4 y 5
    vieja_head.prev = lista.tail # 5 y 4 

    lista.head = maximo # 10 head
    lista.tail = anterior # 5 tail

    return lista
        
# ============================================================
# PRUEBAS PUNTO 1
# ============================================================

print("\n========== PUNTO 1 - CASO 1 ==========")

tren1 = Tren("A")
tren1.acomplar_vagon("B")
tren1.acomplar_vagon("C")

print(tren1)

tren1.mover_siguiente()
print(tren1)

tren1.acomplar_vagon("X")
print(tren1)

tren1.mover_anterior()
print(tren1)

tren1.desacoplar_vagon_actual()
print(tren1)


print("\n========== PUNTO 1 - CASO 2 ==========")

tren2 = Tren("1")
tren2.acomplar_vagon("2")
tren2.acomplar_vagon("3")
tren2.acomplar_vagon("4")

print(tren2)

tren2.mover_siguiente()
tren2.mover_siguiente()

print(tren2)

tren2.vagon_inicio()
print(tren2)

tren2.mover_siguiente()
tren2.vagon_final()
print(tren2)


# ============================================================
# PRUEBAS PUNTO 2
# ============================================================

print("\n========== PUNTO 2 - CASO 1 ==========")

lista1 = dlinkedlist()

lista1.append(2)
lista1.append(3)
lista1.append(0)
lista1.append(5)
lista1.append(4)
lista1.append(0)
lista1.append(7)

print("Antes:", lista1)

fusionar_segmentos(lista1)

print("Despues:", lista1)


print("\n========== PUNTO 2 - CASO 2 ==========")

lista2 = dlinkedlist()

lista2.append(10)
lista2.append(5)
lista2.append(0)
lista2.append(1)
lista2.append(2)
lista2.append(3)
lista2.append(0)
lista2.append(8)
lista2.append(2)

print("Antes:", lista2)

fusionar_segmentos(lista2)

print("Despues:", lista2)


# ============================================================
# PRUEBAS PUNTO 3
# ============================================================

print("\n========== PUNTO 3 - CASO 1 ==========")

lista3 = dlinkedlist()

lista3.append(4)
lista3.append(7)
lista3.append(4)
lista3.append(9)
lista3.append(7)

print("Antes:", lista3)

eliminar_duplicados(lista3)

print("Despues:", lista3)


print("\n========== PUNTO 3 - CASO 2 ==========")

lista4 = dlinkedlist()

lista4.append(5)
lista4.append(2)
lista4.append(8)
lista4.append(5)
lista4.append(2)
lista4.append(10)
lista4.append(8)

print("Antes:", lista4)

eliminar_duplicados(lista4)

print("Despues:", lista4)


# ============================================================
# PRUEBAS PUNTO 4
# ============================================================

print("\n========== PUNTO 4 - CASO 1 ==========")

lista5 = dlinkedlist()

lista5.append(4)
lista5.append(8)
lista5.append(2)
lista5.append(10)
lista5.append(5)

print("Antes:", lista5)

rotar_maximo(lista5)

print("Despues:", lista5)


print("\n========== PUNTO 4 - CASO 2 ==========")

lista6 = dlinkedlist()

lista6.append(7)
lista6.append(3)
lista6.append(15)
lista6.append(6)
lista6.append(9)

print("Antes:", lista6)

rotar_maximo(lista6)

print("Despues:", lista6)
            
            
    
        
