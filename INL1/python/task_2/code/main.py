import copy
import os

class Symbol:
	def __init__(self, letter, count):
		self.letter = letter
		self.count = count

def find_sequences(symbol_list, is_valid, current = ""):
	found = []

	if is_valid(current):
		for i in range(len(symbol_list)):
			symbol_list_copy = copy.deepcopy(symbol_list)
			symbol = symbol_list_copy[i]
			if (symbol.count > 0):
				symbol.count -= 1
				found += find_sequences(symbol_list_copy, is_valid, current + symbol.letter)
		if len(found) == 0:
			found.append(current)

	return found

def valid_test(current):
	if len(current) == 0:
		return True
	a_count = 0
	b_count = 0
	for c in current:
		match c:
			case 'A': a_count += 1
			case 'B': b_count += 1
	return a_count > b_count

if __name__ == "__main__":
	symbol_list = [
		Symbol('A', 9),
		Symbol('B', 2)
	]
	sequences = find_sequences(symbol_list, valid_test)

	print("Paths:", len(sequences))

	os.makedirs("data", exist_ok=True)

	filepath = "data/task.dat"
	try:
		with open(filepath, "w") as file:
			for sequence in sequences:
				file.write(f"{sequence}\n")
		print(f"Successfully wrote sequences to: {filepath}")
	except IOError as e:
		print(f"Failed to write sequences to: {filepath}")
