class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_ll(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next


add_nums1 = LinkedList()
add_nums1.append(2)
add_nums1.append(4)
add_nums1.append(3)

add_nums2 = LinkedList()
add_nums2.append(5)
add_nums2.append(6)
add_nums2.append(4)

add_nums1.print_ll()
