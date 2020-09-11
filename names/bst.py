class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return (f'{self.storage}')

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # value is passed in but needs to be put into a node
        # new node is created unattached to self, i.e. the root node
        # need to determine where to attach new node to root node
        
        #if the value to be inserted is less than the root's value
        if value < self.value:
            # and if there's nothing to the left of the node
            if self.left is None:
                # then create a new node with the value in it
                self.left = BSTNode(value)
            else:
                # insert the value into a node at the leftmost of the tree
                self.left.insert(value)
        else:
            # if there's nothing to the right of the node
            if self.right is None:
                # then createa a new node with the value in it
                self.right = BSTNode(value)
            else:
                # insert the value into a node at the rightmost of the tree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root's value is the target
        if self.value == target:
            return True
        # otherwise, is the root's value greater than the target
        elif self.value > target:
            # then look in left side of the tree
            if self.left:
                # return if the left side of the tree contains the target T/F
                return self.left.contains(target)
            else:
                return False
        # otherwise is the root's value less than the target
        elif self.value < target:
            # then look in the right side of the tree
            if self.right:
                # return if the right side of the tree containts the target T/F
                return self.right.contains(target)
            else:
                return False
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # can run to check if there's something to the right of a node
        if self.right:
            # then do it again and say on the self.right check if something to the right and again and again
            return self.right.get_max()
        # once there is not, that's the max
        else:
            # if self.right is none, that means it's a 1 node tree and the root is the max value
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # base case, call for_each to the root node, otherwise it won't ever start
        fn(self.value)
        # this calls the side of the tree to the right of the root
        if self.right:
            # this says for each, run the fn, which returns the value
            self.right.for_each(fn)
        # this calls the side of the tree to the left of the root
        if self.left:
            # this says for each, run the fn, which returns the value
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Maryam says think of this as left -> center -> right vs. others CRL and RLC
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # queue
        q = Queue()
        c = self
        while c:
            if c is None:
                return
            if c != None:
                print(c.value)
            if c.left:
                q.enqueue(c.left)
            if c.right:
                q.enqueue(c.right)
            c = q.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # stack
        s = Stack()
        c = self
        while c:
            if c is None:
                return
            if c != None:
                print(c.value)
            if c.left:
                s.push(c.left)
            if c.right:
                s.push(c.right)
            c = s.pop()