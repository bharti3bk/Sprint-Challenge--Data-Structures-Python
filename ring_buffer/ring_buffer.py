from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
       
         # If we reach the capacity of the buffer set the current pointer back to the beginning
        if self.current_oldest is None:
            self.current_oldest = self.storage.head
        #Is there anything in our list yet? If not add the first item and 
        #capacity full case
        if self.storage.length == self.capacity and self.current_oldest == self.storage.head: #yes?
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current_oldest = self.current_oldest.next
                 # set value
                 #move current_oldest
        elif self.storage.length == self.capacity and self.current_oldest == self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current_oldest = self.storage.head
                 #set value
                #set current oldnest 
                #capacity not full case
        #insert item and intialize current oldest value
        elif self.storage.length >= self.capacity:
            self.current_oldest.insert_before(item)
            self.storage.length += 1
            temp = self.current_oldest.next
            self.storage.delete(self.current_oldest)
            self.current_oldest = temp
        else: #No?
                self.storage.add_to_tail(item)

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


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
