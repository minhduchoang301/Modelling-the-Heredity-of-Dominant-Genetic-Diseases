from typing import List

class Model:
    """
    We will use the tree ADT to model the problem at hand. The data required for
    this ADT is a set of nodes, where:
    • each node represents one member of the family.
    • each node contains the health status of that family member with respect to
    a particular
    dominant genetic disease.
    • all nodes in the same level belong to the same generation.
    • the root o second layer, his/her grandparents’ nodes are in the third
    layer, and so on.
    """
    storage: List[List[int]]
    gen: int

    def __init__(self, generation: int):
        self.storage = []
        self.gen = generation
        for i in range(1,generation+1):
            self.storage.append([0 for j in range(i+1)])

    def insert(self, j: int):
        i = -1
        while i < -self.gen and self.storage[i][j] == 0:
            self.storage[i][j] = 1
            i -= 1
            j = j // 2

    def delete(self, j: int):
        i = - 1
        while i < -self.gen and self.storage[i][j] != 0:
            self.storage[i][j] = 0
            i -= 1
            j = j // 2
