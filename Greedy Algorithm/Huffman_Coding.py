import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def encode(node, prefix, huff_dict):
    if node is None:
        return
    if node.left is None and node.right is None:
        huff_dict[node.char] = prefix
    encode(node.left, prefix + '0', huff_dict)
    encode(node.right, prefix + '1', huff_dict)

def huffman_coding(data):
    freq_dict = {}
    for char in data:
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1

    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    huff_dict = {}
    encode(heap[0], '', huff_dict)
    return huff_dict

# Example usage:
data = "this is an example for huffman encoding"
huff_dict = huffman_coding(data)
for char, freq in sorted(huff_dict.items(), key=lambda x: x[1]):
    print(f"{char}: {freq}")
