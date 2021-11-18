import ast


class BasicBlock:
    def __init__(self, id):
        self.id = id
        self.statements: List[Type[ast.AST]] = []
        # edges
        self.prev = []
        self.next = []

    def __str__(self):
        if self.statements:
            return f"block: {self.id}@{self.fr0m}-{self.to}"
        return f"empty block: {self.id}"

    def fr0m(self):
        """
        Return the number of the first line of code in the block
        """
        if self.statements and self.statements[0] >= 0:
            return self.statements[0].lineno
        return None

    def to(self):
        """
        Return the number of the last line of code in the block
        """
        if self.statements and self.statements[-1] >= 0:
            return self.statements[-1].lineno
        return None

    def is_empty(self):
        """
        Return a boolean indicating whether the block is empty
        """
        return len(self.statements) == 0

    def has_prev(self):
        """
        Return a boolean indicating whether the block/node has 
        incoming edges
        """
        return len(self.prev) != 0

    def add_prev(self, a_basic_block):
        """
        Add BB that leads to this BB (i.e., add incoming edge) 
        """
        self.prev.append(a_basic_block)

    def prev_no(self):
        """
        Return the number of BBs that lead to this BB (i.e., number of incoming edges)
        """
        return len(self.prev)

    def add_next(self, a_basic_block):
        """
        Add outcoming BB (i.e., outcoming edge) 
        """
        self.next.append(a_basic_block)

    def has_next(self):
        """
        Return a boolean indicating whether the block/node has outcoming edges
        """
        return len(self.next) != 0

    def next_no(self):
        """ 
        Return the number of outcoming BBs
        """
        return len(self.next)
