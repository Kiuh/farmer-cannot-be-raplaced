import utils

def job():
	# TODO: this is naive and not-optimized (works for now though)
	for _ in range(get_world_size()):
		till()
		plant(Entities.Sunflower)
		if num_items(Items.Water) > 0:
			use_item(Items.Water)

		move(North)
			
	for _ in range(get_world_size()-1):
		while not can_harvest():
			do_a_flip()
		harvest()
		move(North)
	harvest()

def main():
	utils.launch_drones_per_line(job)		