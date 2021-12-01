def matrix_value(a, row, colomn):
    result = a[row][colomn]
    return result


def matrix_plus(a, b):
    result = [[a[i][j]+b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
    return result


def matrix_min(a, b):
    result = [[a[i][j] - b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
    return result


def matrix_multiplication(a, b):
    columns_a = len(a[0])
    rows_a = len(a)
    columns_b = len(b[0])
    rows_b = len(b)

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum_value = 0
                for k in range(columns_a):
                    sum_value += a[x][k] * b[k][y]
                result_matrix[x][y] = sum_value
        return result_matrix

    else:
        return None
