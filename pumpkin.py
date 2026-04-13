import utils


def job():
	for _ in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		move(North)

	pumpkin_count = 0

	while pumpkin_count < get_world_size():
		pumpkin_count = 0
		for _ in range(get_world_size()):
			if get_entity_type() == Entities.Dead_Pumpkin:
				harvest()
				plant(Entities.Pumpkin)
				continue
			if can_harvest():
				pumpkin_count += 1
			move(North)

def main():
	utils.launch_drones_per_line(job)
	harvest()

