class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert given value into the tree
    def insert(self, value):
        # check left side
        # check if value is less than the root
        if value < self.value:
            # move to the left and check if None
            if self.left is None:
                # insert node
                self.left = BSTNode(value)
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # check right side
        # check if value is greater than the root
        else:
            # move to the right and check if None
            if self.right is None:
                # insert node
                self.right = BSTNode(value)
            else:
                # call insert on the root's right node
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if self.value is target
        if self.value == target:
            return True
        # check left side
        # check if the target is less than the root
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        # check tight side
        else:
            # check if there's no child to the right
            if not self.right:
                return False
            else:
                return self.right.contains(target)
