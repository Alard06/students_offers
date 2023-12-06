def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print('Невозможно выполнить умножение матриц: неправильные размерности.')
        return None
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))] # создаем матрицу-результат
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j] # вычисляем каждый элемент матрицы-результата
    return result


matrix1 = [[1, 2], [3, 4], [5, 6], [7, 8]], [[7, 8, 9], [10, 11, 12]]
matrix2 = [[7, 8], [10, 11]]
result = multiply_matrices(matrix1, matrix2)
print(result)
if result:
    for row in result:
        print(row)



def test_multiply_matrices():
    assert multiply_matrices([[1, 2], [3, 4], [5, 6]], [[7, 8, 9], [10, 11, 12]]) == [[27, 30, 33],
                                                                                      [61, 68, 75],
                                                                                      [95, 106, 117]]
    assert multiply_matrices([[1, 2], [3, 4], [5, 6], [7, 8]], [[7, 8, 9], [10, 11, 12]]) is None

    print('OK')
test_multiply_matrices()