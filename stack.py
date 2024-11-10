import typing

class Node[T]:
    def __init__(self, value: T):
        self.value: T = value
        self.next: typing.Optional[Node[T]] = None

class Stack[T]:
    def __init__(self):
        self.top: typing.Optional[Node[T]] = None
        self._size: int = 0

    # Adiciona um produto à pilha
    def push(self, item) -> None:
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size += 1

    # Retorna o tamanho da pilha
    def __len__(self) -> int:
        return self._size

    # Retorna se a pilha está vazia ou não
    def empty(self) -> bool:
        return len(self) == 0
    
    # Remove e retorna o produto do topo da pilha
    def pop(self) -> typing.Optional[T]:
        if self.empty():
            return None
        node = self.top
        self.top = self.top.next
        self._size -= 1
        return node.value
    
    # Retorna o produto do topo da pilha
    def peek(self) -> typing.Optional[T]:
        if self.empty():
            return None
        return self.top.value
        
    # Exibe os elementos da pilha
    def print(self) -> None:
        if len(self) == 0:
            return None
        s = ''
        p = self.top

        while p:
            s += str(p.value) + '\n'
            p = p.next
        
        print(s)
    

