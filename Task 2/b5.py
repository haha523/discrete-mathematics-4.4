def dfs(graph, vertex, visited):
    """
    Рекурсивный обход графа в глубину.

    :param graph: Словарь, представляющий граф. Ключи — вершины, значения — списки смежных вершин.
    :param vertex: Текущая вершина.
    :param visited: Множество посещенных вершин.
    :return: Список вершин в порядке их посещения.
    """
    visited.add(vertex)  # Пометить текущую вершину как посещенную
    order.append(vertex)  # Добавить вершину в порядок обхода

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def main():
    # Пример графа
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [6],
        6: []
    }

    start_vertex = int(input("Введите стартовую вершину: "))

    if start_vertex not in graph:
        print("Стартовая вершина отсутствует в графе.")
        return

    global order  # Порядок посещения вершин
    order = []
    visited = set()  # Множество для отслеживания посещенных вершин

    dfs(graph, start_vertex, visited)
    print("Порядок обхода:", order)


if __name__ == "__main__":
    main()
