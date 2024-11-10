from avl import AVLTree
import typing

class HashTableEntry[K: typing.Hashable, V]:
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

    def __ne__(self, key: K):
        return hash(self) == hash(key)

    def __eq__(self, key: K):
        return hash(self) == hash(key)

    def __lt__(self, key: K):
        return hash(self) < hash(key)
    
    def __gt__(self, key: K):
        return hash(self) > hash(key)

    def __hash__(self) -> int:
        return hash(self.key)


# Para esta implementação, como o domínio é pequeno e a função hash pode gerar mais valores que o domínio
# eu assumirei que a taxa de colisão é zero
class HashTable[K: typing.Hashable, V]:
    def __init__(self):
        self._inner_tree: AVLTree[HashTableEntry[K, V]] = AVLTree()
    
    def set(self, key: K, value: V) -> None:
        node = self._inner_tree.search(key)

        if node is not None:
            node.value.value = value
        else:
            self._inner_tree.insert(HashTableEntry(key, value))

    def get(self, key: K) -> typing.Optional[V]:
        node = self._inner_tree.search(key)
        
        if node is not None:
            return node.value.value
        
        return None
    
    def remove(self, key: K) -> None:
        return self._inner_tree.remove(key)
