# Binary reflection

class BinRef:
    # constructor
    def __init__(self, ref_mat):
        self.relay = ref_mat.copy()
        self.dim_of_set = len(self.relay)

    # methods
    def func(self, n):
        out = []
        for rel in range(self.dim_of_set):
            if self.relay[n][rel]:
                out.append(rel)
        return out

    def is_reflexive(self):
        for rel in range(self.dim_of_set):
            if rel not in BinRef.func(self, rel):
                return False
        return True

    def is_irreflexive(self):
        for rel in range(self.dim_of_set):
            if rel in BinRef.func(self, rel):
                return False
        return True

    def is_symmetric(self):
        for row in range(self.dim_of_set):
            for col in range(row + 1, self.dim_of_set):
                if self.relay[row][col] != self.relay[col][row]:
                    return False
        return True

    def is_antisymmetric(self):
        for row in range(self.dim_of_set):
            for col in range(row + 1, self.dim_of_set):
                if self.relay[row][col] == self.relay[col][row]:
                    return False
        return True

    def is_transitive(self):
        for arg in range(self.dim_of_set):
            relation_1 = BinRef.func(self, arg)
            for ref_mid in relation_1:
                ref_fin = BinRef.func(self, ref_mid)
                for val in ref_fin:
                    if val not in relation_1:
                        return False
        return True


# --------------------------------------------------------------------------------


rel_mat1 = [[0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 0]
            ]

rel_mat2 = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
            ]

ref_1 = BinRef(rel_mat1)
ref_2 = BinRef(rel_mat2)

if ref_1.is_reflexive():
    print("The relation is reflexive")
elif ref_1.is_irreflexive():
    print("The relation is irreflexive")
else:
    print("The relation is not reflective neither irreflexive")

if ref_1.is_symmetric():
    print("The relation is symmetric")
elif ref_1.is_antisymmetric():
    print("The relation is antisymmetric")
else:
    print("The relation is asymmetric")

if ref_1.is_transitive():
    print("The relation is transitive")
else:
    print("The relation is not transitive")

print("____________________")

if ref_2.is_reflexive():
    print("The relation is reflexive")
elif ref_2.is_irreflexive():
    print("The relation is irreflexive")
else:
    print("The relation is not reflective neither irreflexive")

if ref_2.is_symmetric():
    print("The relation is symmetric")
elif ref_2.is_antisymmetric():
    print("The relation is antisymmetric")
else:
    print("The relation is asymmetric")

if ref_2.is_transitive():
    print("The relation is transitive")
else:
    print("The relation is not transitive")
