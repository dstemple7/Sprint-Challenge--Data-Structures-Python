class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # array of all the data in the ring
        self.data = []
        # array of all the data in the ring ordered by when added to the ring
        self.history = []

    def append(self, item):
        # if the ring is not full, just add the item to the ring like a call stack, place on top
        if len(self.data) < self.capacity:
            self.data.append(item)
            self.history.append(item)
        # if the ring is full, find the oldest item and remove it from the beginning and then add new item to the end of history "stack"
        # then put the new item in the place in the ring where the old item was
        # so the history "stack" is FIFO
        # the data ring is LOFI, if that's a real thing???
        else:
            swapped = self.data.index(self.history[0])
            
            self.history.pop(0)
            self.history.append(item)
            
            self.data[swapped] = item

    def get(self):
        return self.data