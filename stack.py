"""Stack object class for a  stack data structureof fixed size that removes the
earliest object when full"""


class Stack:
    """Create a stack object of fixed size that removes the earliest
    object when full"""

    def __init__(self, stack_size: int):
        self.stack = # to complete
        self.max_size = # to complete

    def push(self, item):
        """Add item to top of stack. If full, remove item from
        bottom of stack to make space"""

    def pop(self):
        """Return and remove itme from top of stack"""

    def size(self) -> int:
        """Return number of items in stack"""

    def full(self) -> bool:
        """Return True if stack is full"""
