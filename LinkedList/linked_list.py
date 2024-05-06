from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        new_node: ListNode = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        last_node: ListNode = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    def print_ll(self) -> None:
        curr: Optional[ListNode] = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next


# #206 Reverse Linked List
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr: ListNode = head
    nxt: ListNode = head
    prev: ListNode = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_node: ListNode = ListNode()
    p_dummy: ListNode = dummy_node

    while list1 and list2:
        if list1.val <= list2.val:
            p_dummy.next = list1
            list1 = list1.next
        else:
            p_dummy.next = list2
            list2 = list2.next
        p_dummy = p_dummy.next
    if list1:
        p_dummy.next = list1
    if list2:
        p_dummy.next = list2
    return dummy_node.next


linked_list: LinkedList = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

list_node1: ListNode = ListNode(1)
list_node2: ListNode = ListNode(2)
list_node3: ListNode = ListNode(3)
list_node4: ListNode = ListNode(4)
list_node5: ListNode = ListNode(5)

list_node1.next = list_node2
list_node2.next = list_node3
list_node3.next = list_node4
list_node4.next = list_node5


print(reverseList(list_node1))
