class BinarySearchTree:
    def __init__(self, value):
        # value would be the root
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is less than root go left
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # else it will be greater and go right
        else:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value is = to the target return true
        if target == self.value:
            return True
        # else if the target is greater than value go right and repeat
        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
        # else if the less is greater than value go right and repeat
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        # else the target is not in the tree
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # loop til i get to the furthest right
        if self.right is None:
            # when it is none that would be the max
            return self.value
        else:
            # else repeat
            return self.right.get_max()