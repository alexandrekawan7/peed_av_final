import typing

class Node[T]:
    def __init__(self, value: T) -> None:
        self.value = value
        self.left: typing.Optional[Node[T]] = None
        self.right: typing.Optional[Node[T]] = None
        self.node_height: int = 1

class AVLTree[T]:
    def __init__(self) -> None:
        self.root: typing.Optional[Node[T]] = None

    def bigger(self, a: T, b: T) -> T:
        return a if a > b else b

    def node_height(self, node: Node[T]) -> int:
        if node is None:
            return 0
        return node.node_height

    def balance_factor(self, node: Node[T]) -> int:
        if node is None:
            return 0
        return self.node_height(node.left) - self.node_height(node.right)

    def left_rotate(self, node: Node) -> Node:
        aux = node.right
        node.right = aux.left
        aux.left = node
        node.node_height = (
            self.bigger(self.node_height(node.left), self.node_height(node.right)) + 1
        )
        aux.node_height = (
            self.bigger(self.node_height(aux.left), self.node_height(aux.right)) + 1
        )
        return aux

    def right_rotate(self, node: Node) -> Node:
        aux = node.left
        node.left = aux.right
        aux.right = node
        node.node_height = (
            self.bigger(self.node_height(node.left), self.node_height(node.right)) + 1
        )
        aux.node_height = (
            self.bigger(self.node_height(aux.left), self.node_height(aux.right)) + 1
        )
        return aux

    def left_right_rotate(self, node: Node) -> Node:
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def right_left_rotate(self, node: Node) -> Node:
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    def _insert(self, node: Node, value) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        elif value == node.value:
            return node
        else:
            # unreachable
            return node

        node.node_height = (
            self.bigger(self.node_height(node.left), self.node_height(node.right)) + 1
        )

        return self.balance(node)

    def insert(self, value: T) -> None:
        self.root = self._insert(self.root, value)

    def balance(self, node: Node) -> Node:
        bf = self.balance_factor(node)

        if bf > 1:
            if self.balance_factor(node.left) >= 0:
                return self.right_rotate(node)
            else:
                return self.left_right_rotate(node)
        elif bf < -1:
            if self.balance_factor(node.right) <= 0:
                return self.left_rotate(node)
            else:
                return self.right_left_rotate(node)
        return node

    def search(self, value: T) -> typing.Optional[Node[T]]:
        

        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
        return None

    def successor_node(self, node: Node) -> Node:
        current = node.right
        while current and current.left:
            current = current.left
        return current

    def _remove(self, node: Node, value: T) -> Node:
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self.successor_node(node)
            node.value = successor.value
            node.right = self._remove(node.right, successor.value)

        node.node_height = (
            self.bigger(self.node_height(node.left), self.node_height(node.right)) + 1
        )
        return self.balance(node)

    def remove(self, value: T) -> None:
        if not self.search(value):
            return
        self.root = self._remove(self.root, value)

    def _in_order(self, node: Node) -> None:
        if node is not None:
            self._in_order(node.left)
            print(node.value)
            self._in_order(node.right)

    def in_order(self) -> None:
        self._in_order(self.root)

    def _pre_order(self, node: Node) -> None:
        if node is not None:
            print(node.value)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def pre_order(self) -> None:
        self._pre_order(self.root)

    def _post_order(self, node: Node) -> None:
        if node is not None:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node.value)

    def post_order(self) -> None:
        self._post_order(self.root)

