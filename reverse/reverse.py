class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if self.head is none, the list is empty, so just break
        if self.head is None:
            return

        # if self.head is not none, the list is not empty so do this
        if self.head is not None:
            # first capture the value for the original next to the current node's current next
            ogNext = node.get_next()
            # then set the vext value for the current node to it's previous value
            node.set_next(prev)

        # if the ogNext value is not None, i.e. it was captured above, do this. if it is none, break
        if ogNext is not None:
            # set the new head value to the original node's next value. So if starting on 1, set the new list's head value to 2 and then per above, the new head's previous value will be 1
            self.head = ogNext
            # recurse and start again with 2 as the node which will set 3 as old next, then 3 will set 2 as previous, and continue until it gets to 5 which will get_next of None so then this recursion will stop
            self.reverse_list(ogNext, node)
