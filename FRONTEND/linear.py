from numpy import *
import matplotlib.pyplot as plt


def file2matrix(filename):
    data_file = open(filename)
    data_lines = data_file.readlines()
    number_of_lines = len(data_lines)

    data_matrix = zeros((number_of_lines, 1))

    for line_index in range(number_of_lines):
        line = data_lines[line_index].strip()
        data_matrix[line_index, :] = line[:]

    return data_matrix


def load_data(x_filename, y_filename):
    x_file = open(x_filename)
    y_file = open(y_filename)

    x_array = []
    y_array = []

    for x_line in x_file.readlines():
        x_array.append([1.0, float(x_line.strip())])
    for y_line in y_file.readlines():
        y_array.append(float(y_line.strip()))

    return x_array, y_array


def regression(x_array, y_array):
    x_matrix = mat(x_array)
    y_matrix = mat(y_array).T

    m, n = shape(x_matrix)
    max_cycles = 1500
    alpha = 0.07
    weights = ones((n, 1))
    theta = ones((n, 1))

    for cycle_index in range(max_cycles):
        for j in range(n):
            theta[j] = weights[j] - alpha / m * partial_derivative_of_h(weights, x_matrix, y_matrix, j)
        weights = [weight for weight in theta]

    return theta


def partial_derivative_of_h(weights, x_matrix, y_matrix, j):
    error = hypothesis(weights, x_matrix) - y_matrix
    m = shape(error)[0]
    for i in range(m):
        error[i] = error[i] * x_matrix[i, j]
    return sum(error)


def hypothesis(weights, x_matrix):
    return x_matrix * weights


def plot_best_fit(weights, x_matrix, y_matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_matrix[:], y_matrix[:])
    plt.xlabel('Age')
    plt.ylabel('Height')
    x = arange(0.0, 10.0, 0.1)
    y = weights[0] + weights[1] * x
    ax.plot(x, y)
    plt.show()


if __name__ == '__main__':
    
    x_array, y_array = load_data('ex2x.dat', 'ex2y.dat')

    weights = regression(x_array, y_array)
    print weights

    x_matrix = file2matrix('ex2x.dat')
    y_matrix = file2matrix('ex2y.dat')

    plot_best_fit(weights, x_matrix, y_matrix)
