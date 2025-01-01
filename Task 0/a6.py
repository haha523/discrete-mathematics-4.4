def boolean_function_to_sdnf(truth_table):
    n = len(truth_table).bit_length() - 1  # Количество переменных
    terms = []

    # Генерация всех возможных комбинаций переменных
    for i in range(len(truth_table)):
        if truth_table[i] == 1:
            term = []
            for j in range(n):
                if (i >> j) & 1:  # Проверяем j-ый бит числа i
                    term.append(f"x{j}")  # Переменная в положительной форме
                else:
                    term.append(f"x{j}'")  # Переменная в отрицательной форме
            terms.append(" * ".join(term))

    # Объединяем термы в СДНФ
    sdnf = " + ".join(terms) if terms else "0"
    return sdnf

def main():
    # Пример таблицы истинности для булевой функции
    # Функция: f(0, 0) = 1, f(0, 1) = 1, f(1, 0) = 0, f(1, 1) = 0
    truth_table = [1, 1, 0, 0]  # f(0,0), f(0,1), f(1,0), f(1,1)

    # Находим СДНФ
    sdnf = boolean_function_to_sdnf(truth_table)

    # Выводим результат
    print("СДНФ булевой функции:", sdnf)

if __name__ == "__main__":
    main()