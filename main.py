"""Matrix calculator, by Edmond Wong 
This program have the user input two matrices and provides the options to either
add, subtract, or multiply them. (Given requirements for specified operation are fulfilled.)
"""
import sys

def create_matrix():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements rowwise (Integers only): ")
    for num_rows in range(rows):
        list = []
        for num_columns in range(columns):
            list.append(int(input()))
        matrix.append(list)
    return matrix


def matrix_addition(matrix_1, matrix_2):
    matrix = []
    for row in range(len(matrix_1)):
        list = []
        for item in range(len(matrix_1[row])):
            list.append(matrix_1[row][item] + matrix_2[row][item])
        matrix.append(list)   
    return matrix


def matrix_subtraction(matrix_1, matrix_2):
    matrix = []
    for row in range(len(matrix_1)):
        list = []
        for item in range(len(matrix_1[row])):
            list.append(matrix_1[row][item] - matrix_2[row][item])
        matrix.append(list)   
    return matrix


def scalar_multiplication(matrix_1):
    matrix = []
    scalar = float(input("Input scalar: "))
    for row in range(len(matrix_1)):
        list = []
        for item in range(len(matrix_1[row])):
            list.append(matrix_1[row][item] * scalar)
        matrix.append(list)
    return matrix


def matrix_multiplication(matrix_1, matrix_2):
    matrix = []
    list = []
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            sum = 0
            for k in range(len(matrix_2)):
                    sum += (matrix_1[i][k] * matrix_2[k][j])
            list.append(sum)
        matrix.append(list)
        list = []
    return matrix


def get_num_row(matrix):
    count = 0
    for row in matrix:
        count += 1
    return count


def get_num_col(matrix):
    count = 0
    for item in matrix[0]:
        count += 1
    return count

        
def matrix_calculator():
    print("""Welcome to Edmond's Matrix Calculator 
    
    Enter the number associated with the matrix operation you wish to perform:
        1. Addition
        2. Subtraction
        3. Scalar Multiplication
        4. Matrix Multiplication """)

    while True:
        user_input = input("> ")
        if user_input not in ("1", "2", "3", "4"):
            print("You entered an invalid value! Please enter one of the following numbers: (1) (2) (3) (4)")
        else:
            break
        
    if user_input == "1":
        matrix_1 = create_matrix()
        matrix_2 = create_matrix()
        print(f"Matrix 1: {matrix_1}")
        print(f"Matrix 2: {matrix_2}")
        if get_num_row(matrix_1) == get_num_row(matrix_2) and get_num_col(matrix_1) == get_num_col(matrix_2):
            sum = matrix_addition(matrix_1, matrix_2)
            print(f"Their Sum: {sum}")
        else:
            sys.exit("Unable to add the two matrices. In order to add two matrices, they must be the same size (Equal number of rows and columns). Please run the program again with this in mind.")
    elif user_input == "2":
        matrix_1 = create_matrix()
        matrix_2 = create_matrix()
        print(f"Matrix 1: {matrix_1}")
        print(f"Matrix 2: {matrix_2}")
        if get_num_row(matrix_1) == get_num_row(matrix_2) and get_num_col(matrix_1) == get_num_col(matrix_2):
            difference = matrix_subtraction(matrix_1, matrix_2)
            print(f"Their Difference: {difference}")
        else:
            sys.exit("Unable to subtract the two matrices. In order to subtract two matrices, they must be the same size (Equal number of rows and columns). Please run the program again with this in mind.")
    elif user_input == "3":
        matrix_1 = create_matrix()
        print(f"Matrix: {matrix_1}")
        scalar_product = scalar_multiplication(matrix_1)
        print(f"Product of Matrix and Scalar: {scalar_product}")
    elif user_input == "4":
        matrix_1 = create_matrix()
        matrix_2 = create_matrix()
        print(f"Matrix 1: {matrix_1}")
        print(f"Matrix 2: {matrix_2}")
        if get_num_col(matrix_1) == get_num_row(matrix_2):
            matrix_product = matrix_multiplication(matrix_1, matrix_2)
            print(f"Product of Matrix 1 and 2: {matrix_product}")
        else:
            sys.exit("Unable to multiply the two matrices. Matrix 1 must have the same number of columns as Matrix 2 have rows. Please run the program again with this in mind.")


############# RUNNING PROGRAM #############

if __name__ == "__main__":
    matrix_calculator()   
    