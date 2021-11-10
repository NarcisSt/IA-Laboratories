import numpy as np

TRAINING_FILE_INFO_PATH = "./data.txt"


def read_data_from_file():
    f = open(TRAINING_FILE_INFO_PATH, "r")
    for x in f:
        print(x, end="")


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_derivative(z):
    return sigmoid(z) * (1.0 - sigmoid(z))


if __name__ == '__main__':
    learning_rate = float(input("Enter the learning rate: "))
    max_error = float(input("Enter the max error: "))
    max_epoch = float(input("Enter the max number of epochs: "))
    print("The function is: ")
    read_data_from_file()
