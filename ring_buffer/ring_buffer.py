from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # add the value to dll
        if self.storage.length < self.capacity:
            # add to tail
            self.storage.add_to_tail(item)

        elif self.storage.length == self.capacity:

            self.storage.add_to_tail(item)
            self.storage.remove_from_head()


    # returns all of the elements in the buffer in a list in their given order
    # it should NOT return any None values
    

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here 
        # getting the current value from head
        current = self.storage.head

        # loop till end of list
        while current:
            # add the current value to list
            list_buffer_contents.append(current.value)
            # set up next value
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
