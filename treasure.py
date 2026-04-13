from utils import INVERTED_DIRS
clear()

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
					if dfs_to_first_not_blocked(INVERTED_DIRS[d]):
						return True
					move(INVERTED_DIRS[d])
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

def permutations(lst):
    if len(lst) <= 1:
        return [lst]
    
    result = []
    for i in range(len(lst)):
        current = lst[i]
        remaining = lst[:i] + lst[i+1:]
        
        for p in permutations(remaining):
            result.append([current] + p)
    
    return result


dirs = [South, North, East, West]
DIRS = permutations(dirs)
print(len(DIRS))

def solve(limits, i):
	def result():
		return work(limits, i, DIRS[i])
	return result

def main(limits):
	drones = min(len(DIRS), max_drones())
	for i in range(1, drones):
		spawn_drone(solve(limits, i))	
	solve(limits, 0)()
