def add_matrix(a, b):
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result

def print_matrix(m):
    for row in m:
        for value in row:
            print(f"{value:4}", end="")
        print()

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[2, 4, 6],
     [1, 3, 5],
     [7, 9, 8]]

print("Matrix A:")
print_matrix(A)
print("Matrix B:")
print_matrix(B)
print("A + B:")
print_matrix(add_matrix(A, B))
