# Binary reflection

import json


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

    def is_asymmetric(self):
        if BinRef.is_antisymmetric(self) and BinRef.is_irreflexive(self):
            return True
        else:
            return False

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


variant = "var2"
with open('tasks.json', 'r') as f:
    data = json.load(f)
rel_mat1 = data[variant]
ref_1 = BinRef(rel_mat1)

print(variant)
for i in range(len(rel_mat1)):
    print(rel_mat1[i])

if ref_1.is_reflexive():
    print("The relation is reflexive")
else:
    print("The relation is NOT reflexive")
if ref_1.is_irreflexive():
    print("The relation is irreflexive")
else:
    print("The relation is NOT irreflexive")

if ref_1.is_symmetric():
    print("The relation is symmetric")
else:
    print("The relation is NOT symmetric")
if ref_1.is_antisymmetric():
    print("The relation is antisymmetric")
else:
    print("The relation is NOT antisymmetric")
if ref_1.is_asymmetric():
    print("The relation is asymmetric")
else:
    print("The relation is NOT asymmetric")

if ref_1.is_transitive():
    print("The relation is transitive")
else:
    print("The relation is NOT transitive")

print("____________________")
