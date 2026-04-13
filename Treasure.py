
clear()

def empty_dict():
	result = dict()
	for i in range(0, get_world_size() ** 2):
		result[i] = 0
	return result

def inv_dir(dir):
	if dir == South:
		return North
	if dir == East:
		return West
	if dir == West:
		return East
	if dir == North:
		return South

def move_back(dir):
	if dir == South:
		return move(North)
	if dir == East:
		return move(West)
	if dir == West:
		return move(East)
	if dir == North:
		return move(South)

def move_pos(pos, dir):
	if dir == South:
		return pos - 1
	if dir == East:
		return pos + get_world_size()
	if dir == West:
		return pos - get_world_size()
	if dir == North:
		return pos + 1

def rand_dir(dirs):
	i = random() * 4 // 1
	return dirs[i]

blocks = set()

def num_can_move(dirs):
	pos = get_pos_x() * get_world_size() + get_pos_y()
	result = 0
	for d in dirs:
		if not can_move(d) or move_pos(pos, d) in blocks:
			result += 1
	return result

def work(limits, bot_index, dirs):
	global blocks
	
	blocks = set()

	def dfs_to_first_not_blocked(back_dir=None):
		global blocks
		if get_entity_type() == Entities.Treasure and can_harvest():
			harvest()
			blocks = set()
		for d in dirs:
			if d != back_dir:
				pos = get_pos_x() * get_world_size() + get_pos_y()
				next_pos = move_pos(pos, d)
				if next_pos not in blocks and can_move(d):
					return move(d)
				if move(d):
					if dfs_to_first_not_blocked(inv_dir(d)):
						return True
					move_back(d)
		return False

	while num_items(Items.Gold) < limits[Items.Gold] and num_items(Items.Weird_Substance) > limits[Items.Weird_Substance]:
		if get_entity_type() == Entities.Grass:
			plant(Entities.Bush)
			substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
			use_item(Items.Weird_Substance, substance)
		
		if get_entity_type() == Entities.Treasure and can_harvest():
			harvest()
			blocks = set()

		pos = get_pos_x() * get_world_size() + get_pos_y()
		blocks.add(pos)

		dir = None

		for d in dirs:
			next_pos = move_pos(pos, d)
			if next_pos not in blocks and can_move(d):
				dir = d

		if dir == None:
			dfs_to_first_not_blocked()
		else:
			move(dir)



DIRS = [
	[South, East, West, North],
	[South, East, North, West],
	[South, West, East, North],
	[South, West, North, East],
	[South, North, East, West],
	[South, North, West, East],
	
	[West, East, South, North],
	[West, East, North, South],
	[West, South, East, North],
	[West, South, North, East],
	[West, North, East, South],
	[West, North, South, East],
	
	[East, West, South, North],
	[East, West, North, South],
	[East, South, West, North],
	[East, South, North, West],
	[East, North, West, South],
	[East, North, South, West],
	
	[North, West, South, East],
	[North, West, East, South],
	[North, South, West, East],
	[North, South, East, West],
	[North, East, West, South],
	[North, East, South, West],
]

def solve(limits, i):
	def result():
		return work(limits, i, DIRS[i])
	return result

def main(limits):
	for i in range(1, max_drones()):
		spawn_drone(solve(limits, i))	
	solve(limits, 0)()


if __name__ == "__main__":
	main()