# Given two words (begin and end) 
# and a dictionary's word list, return the shortest transformation
# sequence from begin_word to end_word, such that:

# Only one letter can be changed at a time.
# Each transformation word must exist in the word list.
# Note that begin_word is not a transformed word 

# return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin and end are non empty and are not the same 

# notes:
	# The words are nodes but they are not connected to each other 
	# edges every word that has one line of difference
	# The graph will be cyclic undirected. 
		# bat -> ban -> bin -> bit -> bat

	# Is this a dense graph or a sparse graph:
		# the ratio of edges to nodes dictates whether a graph is sparse or dense.
			# A dense graph is one where any given node is connected to half of the other 
			# nodes: airports are a dense graph 

			# 235000 words where each word is at most connected to 23 other words (this is a 
			# sparse graph)

	# We are going to use breadth first search because we are looking for the shortest path.

# Queue util function 

class Queue():
	def __init__(self):
		self.queue = []
	def enqueue(self, value):
		self.queue.append(value) 
	def dequeue(self):
		if self.size() > 0:
			return self.queue.pop(0) 
		else:
			return None 
	def size(self):
		return len(self.queue)

# 2. Build the graph 

# load words from dictionary
f = open('words.txt', 'r') 
word_set = set(f.read().lower().split('\n'))
f.close()
# print(word_set)

def get_neighbors(word):

	# get same length words first 
	results = []
	list_word = list(word) 
	for i in range(len(list_word)):
		for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
			temp_word = list_word.copy()
			temp_word[i] = letter
			joined_word = ''.join(temp_word) 
			if joined_word in word_set and joined_word != word:
				results.append(joined_word)
	# Swap each letter with a letter in the alphabet 
	# if resulting word is in the word_set add to results 
	return results 

# print(get_neighbors('cat'))

# Create a counter that breaks if it goes higher than one and while loop through
# while comparing.

# Go through each word and build an adjacency list with each word one letter away.

# Create an equality function 
# def words_are_neighbors(w1, w2):
# 	list_word = list(w1) 
# 	# Go through each letter in the word
# 	for i in range(len(list_word)):
# 	# Swap with each letter in the alphabet 
# 		for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'.'p','q','r','s','t','u','v','w','x','y','z']:
# 			# Check if that equals given word
# 			temp_word = list_word.copy()
# 			temp_word[i] = letter 
# 			if ''.join(temp_word) == w2:
# 				return True
# 	return False

def words_are_neighbors(w1, w2):
	if len(w1) != len(w2):
		return False
	for i in range(len(w1)):
		if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
			return True 
	return False 


# def words_are_neighbors(word1, word2):
# 	for i in range(len(word1)):
# 		list_word1 = list(word1) 
# 		list_word2 = list(word2) 
# 		list_word1.pop(i) 
# 		list_word2.pop(i) 
# 		if list_word1 == list_word2:
# 			return True

neighbors = {}

# Go through each word
# for word in words:
# 	neighbors[word] = []
# 	# Go through each potential neighbor
# 	for potential_neighbor in words:
# 		# Add potential neighbor if it matches to the word
# 		if words_are_neighbors(word, potential_neighbor):
# 			neighbors[word].add(potential_neighbor)

# def get_neighbors(word):
# 	return neighbors[word]


# 3. traverse the graph using BFS

def word_latter(begin_word, end_word):
	# create a queue 
	q = Queue()
	# Enqueue a path to starting word 
	q.enqueue( [begin_word] )
	# Create a visited set
	visited = set()
	# While queue is not empty:
	while q.size() > 0:
		# dequeue path 
		path = q.dequeue()
		print('path', path)
		# grab the last word from the path 
		w = path[-1]
		# Check if its our target word 
		if w == end_word:
			# if so, return path 
			return path
		# Chack if its been visited 
		# if not mark as visited 
		if w not in visited:
			visited.add(w)
			for neighbor in get_neighbors(w):
				path_copy = path.copy()
				path_copy.append(neighbor)
				q.enqueue(path_copy)
			# enqueue path to each neighboring word

print(word_latter('sail', 'boat'))