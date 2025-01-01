class Node:
    """Класс узла AVL-дерева."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """Класс AVL-дерева."""
    def insert(self, root, key):
        # Вставка в поддерево
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Обновление высоты текущего узла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Балансировка узла
        balance = self.get_balance(root)

        # Левый поворот
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # Правый поворот
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # Лево-правый поворот
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Право-левый поворот
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, root):
        """Обход дерева в префиксном порядке."""
        if root:
            print(root.key, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

# Использование
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    # Пример множества
    nums = [10, 20, 30, 40, 50, 25]

    for num in nums:
        root = tree.insert(root, num)

    print("Префиксный обход сбалансированного дерева:")
    tree.pre_order(root)
