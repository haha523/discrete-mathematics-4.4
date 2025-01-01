from collections import Counter
import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(node, code="", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code
    generate_huffman_codes(node.left, code + "0", codes)
    generate_huffman_codes(node.right, code + "1", codes)
    return codes


def main():
    text = input("Введите текст: ")
    tree = build_huffman_tree(text)
    codes = generate_huffman_codes(tree)
    print("Коды Хаффмана:")
    for char, code in codes.items():
        print(f"{repr(char)}: {code}")


if __name__ == "__main__":
    main()
