import sqlite3

from utils.input_matrix import input_matrix_bt, correct_fraction
from utils.OOP import Matrix

stroka_ERO = (
        "Введите нужную операцию в виде:\n1 2 (для d) - умножение стоки 1 на 2\n1 2 3 (для l) - вычесть из первой строки вторую умноженную на три\n1 2 t (для t) - поменять местами первую и вторую строки" + '\n'
        + "Дроби вводить ввиде 1/3")


def start_opertions_tb(m, s):
    m = Matrix(input_matrix_bt(m))
    test = s.split()
    if "t" in test:
        if not all((int(float(i)) <= len(m.matrix) and int(float(i)) <= len(m.matrix[0])) for i in test[:2]):
            print("U is dobanytay")
            return None
    elif len(test) == 2:
        i = test[0]
        if not (int(float(i)) <= len(m.matrix) and int(float(i)) <= len(m.matrix[0])):
            print("U is dobanytay")
            return None
    elif len(test) == 3:
        if not all((int(float(i)) <= len(m.matrix) and int(float(i)) <= len(m.matrix[0])) for i in test[:2]):
            print("U is dobanytay")
            return None

    # print(888)
    # if all(True if "/" in i else (int(float(i)) <= len(m.matrix) and int(float(i)) <= len(m.matrix[0])) for i in test):
    #     print(999)
    #     pass
    # else:
    #     return None
    if len(s.split()) in (1, 2, 3, 4):
        m.matrix = [*correct_fraction(s)]
        # print(correct_fraction(s))
        # conn = sqlite3.connect("mat.sql")
        # cursor = conn.cursor()
        # print(m.show_entry(), r'{m.show_entry()}', "3454345")
        # cursor.execute(f'INSERT INTO mat (matrix) VALUES ("%s")' % (m.show_entry()))
        # conn.commit()
        # cursor.close()
        # conn.close()
        return m.show()
