import utils

def job():
	for _ in range(get_world_size()):
		till()
		odd = (get_pos_x()+get_pos_y()) % 2 != 0
		if odd:
			plant(Entities.Tree)
			if num_items(Items.Water) > 0:
				use_item(Items.Water)
		else:
			plant(Entities.Bush)
		move(North)
			
	for _ in range(get_world_size()-1):
		while not can_harvest():
			do_a_flip()
		harvest()
		move(North)
	harvest()

def main():
	utils.launch_drones_per_line(job)			