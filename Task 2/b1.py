from itertools import permutations


def find_fixed_point_permutations(n, k):
    elements = list(range(1, n + 1))
    result = []

    # Перебираем все перестановки
    for perm in permutations(elements):
        fixed_count = sum(1 for i in range(n) if perm[i] == elements[i])
        if fixed_count == k:
            result.append(perm)

    return result


def main():
    n = int(input("Введите количество элементов (n): "))
    k = int(input("Введите количество фиксированных элементов (k): "))

    if k > n or k < 0:
        print("Некорректное значение k.")
        return

    permutations_with_k_fixed = find_fixed_point_permutations(n, k)
    print(f"Найдено {len(permutations_with_k_fixed)} перестановок:")
    for perm in permutations_with_k_fixed:
        print(perm)


if __name__ == "__main__":
    main()
