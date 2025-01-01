def boolean_function_to_sknf(truth_table):
    n = len(truth_table).bit_length() - 1  # Количество переменных
    clauses = []

    # Генерация всех возможных комбинаций переменных
    for i in range(len(truth_table)):
        if truth_table[i] == 0:
            clause = []
            for j in range(n):
                if (i >> j) & 1:  # Проверяем j-ый бит числа i
                    clause.append(f"x{j}'")  # Переменная в отрицательной форме
                else:
                    clause.append(f"x{j}")  # Переменная в положительной форме
            clauses.append(" + ".join(clause))

    # Объединяем конъюнкции в СКНФ
    sknf = " * ".join(f"({clause})" for clause in clauses) if clauses else "1"
    return sknf

def main():
    # Пример таблицы истинности для булевой функции
    # Функция: f(0, 0) = 0, f(0, 1) = 1, f(1, 0) = 1, f(1, 1) = 0
    truth_table = [0, 1, 1, 0]  # f(0,0), f(0,1), f(1,0), f(1,1)

    # Находим СКНФ
    sknf = boolean_function_to_sknf(truth_table)

    # Выводим результат
    print("СКНФ булевой функции:", sknf)

if __name__ == "__main__":
    main()