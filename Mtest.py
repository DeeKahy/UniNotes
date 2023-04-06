class ListNode:
    def __init__(self, key, next_node=None):
        self.key = key
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key):
        if not self.head:
            self.head = ListNode(key)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(key)

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.key))
            current = current.next
        return "->".join(elements)


def reverse_list(L):
    prev = None
    current = L.head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    L.head = prev


# Test case
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original Linked List:")
print(linked_list)

reverse_list(linked_list)

print("\nReversed Linked List:")
print(linked_list)
