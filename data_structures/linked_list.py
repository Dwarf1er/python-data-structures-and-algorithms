class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None) -> None:
        if value is not None:
            new_node: Node = Node(value)
            self.head: Node = new_node
            self.tail: Node = new_node
            self.length: int = 1
        else:
            self.head: Node = None
            self.tail: Node = None
            self.length: int = 0

    def prepend(self, value) -> bool:
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def append(self, value) -> bool:
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        if self.length == 0:
            return None
        else:
            pointer: Node = self.head
            removed_node: Node = self.tail
            while pointer.next is not self.tail and pointer.next is not None:
                pointer = pointer.next
            self.tail = pointer
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return removed_node
    
    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        else:
            removed_node: Node = self.head
            self.head = self.head.next
            removed_node.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return removed_node
        
    def get(self, index: int) -> Node:
        if index < 0 or index > self.length:
            return None
        else:
            pointer: Node = self.head
            for _ in range(index):
                pointer = pointer.next
            return pointer
        
    def set(self, index: int, value) -> Node:
        pointer: Node = self.get(index)
        if pointer:
            pointer.value = value
            return True
        return False
    
    def print_linked_list(self) -> None:
        pointer: Node = self.head
        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next