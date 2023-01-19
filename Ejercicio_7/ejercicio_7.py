import heapq
from doctest import testmod

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        heap.append(Node(char, freq))
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    return heap[0]

def build_code_table(root, code, code_table):
    if root.char:
        code_table[root.char] = code
        return
    build_code_table(root.left, code + "0", code_table)
    build_code_table(root.right, code + "1", code_table)

def compress(message, code_table):
    compressed_message = ""
    for char in message:
        compressed_message += code_table[char]
    return compressed_message

def decompress(compressed_message, root):
    message = ""
    current = root
    for bit in compressed_message:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        if current.char:
            message += current.char
            current = root
    return message

if __name__ == "__main__":
    freq_table = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09, "T": 0.15}
    root = build_huffman_tree(freq_table)
    code_table = {}
    build_code_table(root, "", code_table)
    message = "AF13M3T"
    compressed_message = compress(message, code_table)
    print("Original message:", message)
    print("Compressed message:", compressed_message)
    decompressed_message = decompress(compressed_message, root)
    print("Decompressed message:", decompressed_message)
    testmod()
