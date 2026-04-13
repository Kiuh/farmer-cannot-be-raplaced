
def launch_drones_per_column(job):
	amount = min(get_world_size(), max_drones())
	set_world_size(amount)

	handlers = []
	for i in range(1, amount):
		handlers.append(spawn_drone(job))
		move(East)
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
