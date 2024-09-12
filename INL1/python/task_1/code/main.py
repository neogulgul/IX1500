import os

from Coord import *

def find_sequences(current, characters, depth, is_valid):
	found = []

	if is_valid(current):
		if depth <= 0:
			found.append(current)
		else:
			for c in characters:
				found += find_sequences(current + c, characters, depth - 1, is_valid)

	return found

def is_valid_a(sequence):
	# a) How many such paths are there from (0, 3) to (7, 2)?
	u_count = 0
	l_count = 0

	for c in sequence:
		match c:
			case 'U': u_count += 1
			case 'L': l_count += 1
		if u_count > 3 or l_count > 4:
			return False

	return True

def is_valid_b(sequence):
	# b) How many paths from (0, 3) to (7, 2) touch or cross x-axis at least once?
	start = Coord(0, 3)
	stop  = Coord(7, 2)

	current = start
	touched_x_axis = False
	for c in sequence:
		match c:
			case 'U': current.move(1,  1)
			case 'L': current.move(1, -1)
		if current.y == 0:
			touched_x_axis = True

	if not touched_x_axis:
		x_coord_of_earliest_x_axis_touch = current.x + current.y
		if x_coord_of_earliest_x_axis_touch > 5:
			return False

	if current.x == stop.x:
		return current.y == stop.y and touched_x_axis

	return True;

def is_valid_c(sequence):
	# c) How many paths from (0, 3) to (7, 2) never touch or cross x-axis?
	start = Coord(0, 3)
	stop  = Coord(7, 2)

	current = start
	for c in sequence:
		match c:
			case 'U': current.move(1,  1)
			case 'L': current.move(1, -1)
		if current.y == 0:
			return False

	if current.x == stop.x:
		return current.y == stop.y

	return True

def is_valid_d(sequence):
	# d) How many paths from (7, 6) to (20, 5) never touch or cross x-axis?
	start = Coord(7, 6)
	stop  = Coord(20, 5)

	current = start
	for c in sequence:
		match c:
			case 'U': current.move(1,  1)
			case 'L': current.move(1, -1)
		if current.y == 0:
			return False

	if current.x == stop.x:
		return current.y == stop.y

	return True

def subtask(letter, moves, is_valid):
	print(letter + ")")
	sequences = find_sequences("", "UL", moves, is_valid)
	print("Paths:", len(sequences))

	filepath = "data/" + letter + ".dat"
	try:
		with open(filepath, "w") as file:
			for sequence in sequences:
				file.write(f"{sequence}\n")
		print(f"Successfully wrote sequences to: {filepath}")
	except IOError as e:
		print(f"Failed to write sequences to: {filepath}")

if __name__ == "__main__":
	os.makedirs("data", exist_ok=True)
	subtask("a", 7, is_valid_a)
	subtask("b", 7, is_valid_b)
	subtask("c", 7, is_valid_c)
	subtask("d", 13, is_valid_d)
