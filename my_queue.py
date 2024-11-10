import typing

class Node[T]:
    def __init__(self, data: T):
        self.data = data
        self.next: typing.Optional[Node[T]] = None
        
class Queue[T]:
    def __init__(self):
        self.first: typing.Optional[T] = None
        self.last: typing.Optional[T] = None
        self._size = 0
        
    def push(self, elem: T) -> None:
        node = Node(elem)
        
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
            
        if self.first is None:
            self.first = node
        self._size += 1
        
    def pop(self) -> typing.Optional[T]:
        if self.empty():
            return None
        elem = self.first.data
        self.first = self.first.next
        
        if self.first  is None:
            self.last = None
            
        self._size -= 1
        return elem
    
    def peek(self) -> typing.Optional[T]:
        if self.empty():
            return None
        return self.first.data
        
        
    def __len__(self) -> int:
        return self._size
    
    def empty(self) -> bool:
        return len(self) == 0
    
    def __repr__(self):
        if self.empty():
            return 'Empty queue'
        
        self._size += 1
        
        s = ''
        p = self.first
        while p:
            s += str(p.data)
            p = p.next
            if p:
                s+= ' -> '
        return s 
    
