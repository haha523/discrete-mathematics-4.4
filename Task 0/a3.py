def intersection_of_sets(sets):
    # Начинаем с первого множества
    intersected_set = sets[0]
    # Находим пересечение со всеми остальными множествами
    for s in sets[1:]:
        intersected_set &= s  # Пересечение
    return intersected_set

def main():
    # Задайте n множеств (пример)
    sets = [
        {1, 2, 3, 4},
        {2, 3, 5},
        {3, 2, 6}
    ]

    # Находим пересечение множеств
    result = intersection_of_sets(sets)

    # Выводим результат
    print("Пересечение множеств:", result)

if __name__ == "__main__":
    main()