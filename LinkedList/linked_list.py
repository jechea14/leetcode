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
    # create a dummy node to return the result linked list
    dummy_node: ListNode = ListNode()
    # pointer for dummy node to append nodes and traverse
    p_dummy: ListNode = dummy_node

    while list1 and list2:
        # compare list values
        if list1.val <= list2.val:
            # append list1 to the dummy linked list
            p_dummy.next = list1
            # move list1 pointer to the next node
            list1 = list1.next
        else:
            # append list2 to the dummy linked list
            p_dummy.next = list2
            # move list2 pointer to the next node
            list2 = list2.next
        # move the dummy pointer to the next node as well
        p_dummy = p_dummy.next

    # when one list is valid
    # if a certain list is not None, put the remaining nodes into dummy linked list
    if list1:
        p_dummy.next = list1
    if list2:
        p_dummy.next = list2
    return dummy_node.next


# #141 Linked List Cycle
def hasCycle(head: Optional[ListNode]) -> bool:
    # edge cases
    if head is None:
        return False
    if head.next is None:
        return False

    # start the pointers in the beginning
    fast: ListNode = head
    slow: ListNode = head

    # go through linked list while fast and fast.next are not null
    # fast.next avoids any out of bounds error
    while fast and fast.next:
        # fast pointer goes twice as fast than slow
        # slow pointer goes normally
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# #2 Add Two Numbers
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # create a dummy node to append and return results
    dummy: ListNode = ListNode()
    curr: ListNode = dummy
    sum_tens: int = 0

    # sum_tens continues the loop for the carry numbers
    while l1 or l2 or sum_tens:
        # get the vals, becomes 0 if the node is None
        val1: int = l1.val if l1 else 0
        val2: int = l2.val if l2 else 0

        # add the vals for the sum along with the carry
        sum: int = val1 + val2 + sum_tens
        sum_ones: int = sum % 10
        sum_tens = sum // 10

        # create a node of result and append to result linked list
        curr.next = ListNode(sum_ones)

        # move both pointers and dummy node pointer
        # the lists becomes None if the next node doesn't exist, set up for val variables
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next


# #143 Reorder List
def reorderList(head: Optional[ListNode]) -> None:
    # find middle using fast and slow pointers
    fast: ListNode = head.next
    slow: ListNode = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    nxt: ListNode = slow.next
    prev = slow.next = None
    while nxt:
        tmp = nxt.next
        nxt.next = prev
        prev = nxt
        nxt = tmp

    # merge the two halfs
    first: ListNode = head
    second: ListNode = prev
    while second:
        tmp1: ListNode = first.next
        tmp2: ListNode = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


linked_list: LinkedList = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

list_node1: ListNode = ListNode(2)
list_node2: ListNode = ListNode(4)
list_node3: ListNode = ListNode(3)
list_node4: ListNode = ListNode(-4)
list_node5: ListNode = ListNode(5)

list_node_1: ListNode = ListNode(5)
list_node_2: ListNode = ListNode(6)
list_node_3: ListNode = ListNode(4)
list_node_4: ListNode = ListNode(-4)
list_node_5: ListNode = ListNode(5)

list_node1.next = list_node2
list_node2.next = list_node3

list_node_1.next = list_node_2
list_node_2.next = list_node_3


# print(reverseList(list_node1))
# print(hasCycle(list_node1))
print(addTwoNumbers(list_node1, list_node_1))
