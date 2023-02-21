import numpy as np
from scipy.linalg import solve
# 1.
def question1(x, y, estimate_x):
    size = len(x)
    matrix = np.zeros((size, size))
    for counter, row in enumerate(matrix):
        row[0] = y[counter]   
    num_of_points = len(x)
    for i in range(1, num_of_points):
        for j in range(1, i + 1):
            first_multiplication = (estimate_x - x[i - j]) * matrix[i][j - 1]
            second_multiplication = (estimate_x - x[i]) * matrix[i - 1][j - 1]
            denominator = x[i] - x[i - j]
            coefficient = (first_multiplication - second_multiplication) / denominator
            matrix[i][j] = coefficient
    print(matrix[num_of_points - 1][num_of_points - 1], "\n")
# 2. 
def question2and3():
    x0 = 7.2
    x1 = 7.4
    x2 = 7.5
    x3 = 7.6
    fx0 = 23.5492
    fx1 = 25.3913
    fx2 = 26.8224
    fx3 = 27.4589
    div_diff_1 = (fx1 - fx0) / (x1 - x0)
    div_diff_2 = (fx2 - fx1) / (x2 - x1)
    div_diff_3 = (fx3 - fx2) / (x3 - x2)
    div_diff_2_1 = (div_diff_2 - div_diff_1) / (x2 - x0)
    div_diff_2_2 = (div_diff_3 - div_diff_2) / (x3 - x1)
    div_diff_3_1 = (div_diff_2_2 - div_diff_2_1) / (x3 - x0)
    d = [div_diff_1, div_diff_2_1, div_diff_3_1]
    print(d, "\n")
    approx_x = 7.3
    p_x = fx0 + div_diff_1 * (approx_x - x0) + div_diff_2_1 * (approx_x - x1) * (approx_x - x0)\
          + div_diff_3_1 * (approx_x - x2) * (approx_x - x1) * (approx_x - x0)
    print(p_x, "\n")

# 4. 
def question4():
    a1 = 3.6
    a2 = 3.6
    a3 = 3.8
    a4 = 3.8
    a5 = 3.9
    a6 = 3.9
    b1 = 1.675
    b2 = 1.675
    b3 = 1.436
    b4 = 1.436
    b5 = 1.318
    b6 = 1.318
    c1 = 0
    c2 = -1.195
    c3 = (b3 - b2) / (a3 - a2)
    c4 = -1.188
    c5 = (b5 - b4) / (a5 - a4)
    c6 = -1.182
    d1 = 0
    d2 = 0
    d3 = (c3 - c2) / (a3 - a2)
    d4 = (c4 - c3) / (a4 - a2)
    d5 = (c5 - c4) / (a5 - a3)
    d6 = (c6 - c5) / (a6 - a4)
    e1 = 0
    e2 = 0
    e3 = 0
    e4 = (d4 - d3) / (a4 - a1)
    e5 = (d5 - d4) / (a5 - a2)
    e6 = (d6 - d5) / (a6 - a3)
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = (e5 - e4) / (a5 - a1)
    f6 = (e6 - e5) / (a6 - a2)
    a = np.matrix([[a1, b1, c1, d1, e1, f1], [a2, b2, c2, d2, e2, f2], [a3, b3, c3, d3, e3, f3], \
                   [a4, b4, c4, d4, e4, f4], [a5, b5, c5, d5, e5, f5], [a6, b6, c6, d6, e6, f6]])
    print(a, "\n")
# 5.    
def question5(x, y):
    size = len(x)
    matrix: np.array = np.zeros((size, size))
    matrix[0][0] = 1
    matrix[1][0] = x[1] - x[0]
    matrix[1][1] = 2 * ((x[1] - x[0]) + (x[2] - x[1]))
    matrix[1][2] = x[2] - x[1]
    matrix[2][1] = x[2] - x[1]
    matrix[2][2] = 2 * ((x[3] - x[2]) + (x[2] - x[1]))
    matrix[2][3] = x[3] - x[2]
    matrix[3][3] = 1
    print(matrix, "\n")

    c0 = 0
    c1 = (3 / (x[2] - x[1]) * (y[2] - y[1])) - (3 / (x[1] - x[0]) * (y[1] - y[0]))
    c2 = (3 / (x[3] - x[2]) * (y[3] - y[2])) - (3 / (x[2] - x[1]) * (y[2] - y[1]))
    c3 = 0
    c = np.array([c0, c1, c2, c3])
    print(c, "\n")

    f = [[matrix]]
    g = [[c0], [c1], [c2], [c3]]

    h = solve(f, g)

    print(h.T[0], "\n")

if __name__ == "__main__":
    np.set_printoptions(precision = 7, suppress = True, linewidth = 100)
    
    x = [3.6, 3.8, 3.9]
    y = [1.675, 1.436, 1.318]
    estimate_x = 3.7 
    question1(x, y, estimate_x)
    # 2 and 3
    question2and3()

    # 4
    question4()

    # 5
    x = [2, 5, 8, 10]
    y = [3, 5, 7, 9]
    question5(x, y)
