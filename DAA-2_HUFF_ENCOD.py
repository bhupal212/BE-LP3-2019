# Practical 2
# Huffman Encoding Algorithm

import heapq

class MinHeapNode:
	def __init__(self, data, freq):
		self.data = data
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		return self.freq < other.freq

class HuffmanCoding:
	@staticmethod
	def print_codes(root, str_code):
		if root is None:
			return
		if root.data != '$':
			print(f"{root.data}: {str_code}")
		HuffmanCoding.print_codes(root.left, str_code + "0")
		HuffmanCoding.print_codes(root.right, str_code + "1")

	@staticmethod
	def huffman_code(data, freq):
		min_heap = []
		for i in range(len(data)):
			heapq.heappush(min_heap, MinHeapNode(data[i], freq[i]))
		    
		while len(min_heap) > 1:
			left = heapq.heappop(min_heap)
			right = heapq.heappop(min_heap)
			temp = MinHeapNode('$', left.freq + right.freq)
			temp.left = left
			temp.right = right
			heapq.heappush(min_heap, temp)

		HuffmanCoding.print_codes(min_heap[0], "")

def main():
	data = ['A', 'B', 'C', 'D']
	freq = [23, 12, 34, 10]
	HuffmanCoding.huffman_code(data, freq)

if __name__ == "__main__":
	main()
