def boolean_function_to_canonical_form(truth_table):
    n = len(truth_table).bit_length() - 1  # Количество переменных
    terms = []

    # Генерация всех возможных комбинаций переменных
    for i in range(len(truth_table)):
        if truth_table[i] == 1:  # Проверяем, равен ли элемент 1
            term = []
            for j in range(n):
                if (i >> j) & 1:  # Проверяем j-ый бит числа i
                    term.append(f"x{j}")  # Переменная в положительной форме
                else:
                    term.append(f"x{j}'")  # Переменная в отрицательной форме
            terms.append(" * ".join(term))

    # Объединяем термы в каноническую форму
    canonical_form = " + ".join(terms) if terms else "0"
    return canonical_form

def main():
    # Пример таблицы истинности для булевой функции
    # Функция: f(0, 0) = 0, f(0, 1) = 1, f(1, 0) = 1, f(1, 1) = 0
    truth_table = [0, 1, 1, 0]  # f(0,0), f(0,1), f(1,0), f(1,1)

    # Находим каноническую форму
    canonical_form = boolean_function_to_canonical_form(truth_table)

    # Выводим результат
    print("Каноническая форма булевой функции:", canonical_form)

if __name__ == "__main__":
    main()