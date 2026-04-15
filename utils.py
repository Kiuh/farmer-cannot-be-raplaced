INVERTED_DIRS = {North: South, South: North, East: West, West: East}

def launch_drones_per_line(job, spawn_dir = East):
	amount = min(get_world_size(), max_drones())
	set_world_size(amount)

	handlers = []
	for i in range(1, amount):
		handlers.append(spawn_drone(job))
		move(spawn_dir)
	job()

	for h in handlers:
		wait_for(h)

def move_to(x, y):
	dx = x - get_pos_x()
	dy = y - get_pos_y()

	while dx > 0:
		if not move(East):
			return False
		dx -= 1

	while dx < 0:
		if not move(West):
			return False
		dx += 1

	while dy > 0:
		if not move(North):
			return False
		dy -= 1

	while dy < 0:
		if not move(South):
			return False
		dy += 1

	return True

def fly_to(x, y):
	dx = x - get_pos_x()
	dy = y - get_pos_y()

	y_dir = North
	x_dir = East
	if dy < 0:
		y_dir = INVERTED_DIRS[y_dir]
	if dx < 0:
		x_dir = INVERTED_DIRS[x_dir]

	if abs(dy) > get_world_size() // 2:
		y_dir = INVERTED_DIRS[y_dir]
	if abs(dx) > get_world_size() // 2:
		x_dir = INVERTED_DIRS[x_dir]

	while get_pos_y() != y:
		move(y_dir)
	while get_pos_x() != x:
		move(x_dir)


def quicksort(list):
	if len(list) <= 1:
		return list
	pivot = list[len(list) // 2]
	left = []
	right = []
	middle = []
	for x in list:
		if x < pivot:
			left.append(x)
		elif x > pivot:
			right.append(x)
		else:
			middle.append(x)

	return quicksort(left) + middle + quicksort(right)