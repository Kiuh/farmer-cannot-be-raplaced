
import utils

def g_dir():
	x = get_pos_x()
	y = get_pos_y()
	w = get_world_size() - 1

	if x == 0 and y == 0:
		return North

	if x != 0 and y == 0:
		return West
	
	if x == w and y == 1:
		return South

	if x % 2 == 0 and y == w:
		return East
	
	if x % 2 == 1 and y == 1:
		return East
	
	if x % 2 == 0 and y < w:
		return North
	
	if x % 2 == 1 and y > 1:
		return South

	return None


def snake_move_to(x, y):
	dx = x - get_pos_x()
	dy = y - get_pos_y()

	for _ in range(10):
		while dx > 0:
			if not move(East):
				break
			dx -= 1

		while dx < 0:
			if not move(West):
				break
			dx += 1

		while dy > 0:
			if not move(North):
				break
			dy -= 1

		while dy < 0:
			if not move(South):
				break
			dy += 1

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


while True:
	clear()
	change_hat(Hats.Dinosaur_Hat)

	repeat = 8
	while repeat > 0 and can_move(g_dir()):
		next_x, next_y = measure()
		harvest()
		
		if not snake_move_to(next_x, next_y):
			break

		repeat -= 1

	while True:
		if get_entity_type() == Entities.Apple:
			next_x, next_y = measure()
			harvest()
		if not move(g_dir()):
			break


