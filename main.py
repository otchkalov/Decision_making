# Binary reflection

relay = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0],
]


def get_dim(mat):
    return len(mat)


def func(n, mat):
    dim_of_set = get_dim(mat)
    out = []
    for rel in range(dim_of_set):
        if mat[n][rel]:
            out.append(rel)
    return out


def is_reflexive(mat):
    dim_of_set = get_dim(mat)
    for rel in range(dim_of_set):
        if rel not in func(rel, mat):
            return False
    return True


def is_irreflexive(mat):
    dim_of_set = get_dim(mat)
    for rel in range(dim_of_set):
        if rel in func(rel, mat):
            return False
    return True


def is_symmetric(mat):
    dim_of_set = get_dim(mat)
    for row in range(dim_of_set):
        for col in range(row + 1, dim_of_set):
            if mat[row][col] != mat[col][row]:
                return False
    return True


def is_antisymmetric(mat):
    dim_of_set = get_dim(mat)
    for row in range(dim_of_set):
        for col in range(row + 1, dim_of_set):
            if mat[row][col] == mat[col][row]:
                return False
    return True


def is_transitive(mat):
    dim_of_set = get_dim(mat)
    for arg in range(dim_of_set):
        relation_1 = func(arg, mat)
        for ref_mid in relation_1:
            ref_fin = func(ref_mid, mat)
            for val in ref_fin:
                if val not in relation_1:
                    return False
    return True


if is_reflexive(relay):
    print("The relation is reflexive")
elif is_irreflexive(relay):
    print("The relation is irrreflexive")
else:
    print("The relation is not reflective neither irrreflexive")

if is_symmetric(relay):
    print("The relation is symmetric")
elif is_antisymmetric(relay):
    print("The relation is antisymmetric")
else:
    print("The relation is asymmetric")

if is_transitive(relay):
    print("The relation is transitive")
else:
    print("The relation is not transitive")
