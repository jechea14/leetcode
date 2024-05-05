class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    def print_ll(self) -> None:
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next
