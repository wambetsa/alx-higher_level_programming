#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        s_len = len(matrix[i])
        for j in range(s_len):
            if j != s_len - 1:
                end_char = ' '
            else:
                end_char = ''
            print("{:d}".format(matrix[i][j]), end=end_char)
        print("")
