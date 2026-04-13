
import Utils

def job():
	for _ in range(get_world_size()):
		till()
		plant(Entities.Carrot)
		use_item(Items.Water)
		move(North)

	for _ in range(10):
		for _ in range(get_world_size()-1):
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
				use_item(Items.Water)
			move(North)
		if can_harvest():
			harvest()
			plant(Entities.Carrot)

def main():
	Utils.launch_drones_per_line(job)			