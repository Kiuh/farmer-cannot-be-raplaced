import Utils

def sort_column():
	a = 0

	while a < get_world_size() :
		while get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)

		if get_pos_y() != 0 and measure() < measure(South):
			swap(South)
			a = 0	

		a += 1

		move(North)

def sort_row():
	a = 0

	while a < get_world_size() :
		while get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)

		if get_pos_x() != 0 and measure() < measure(West):
			swap(West)
			a = 0	

		a += 1

		move(East)


def main():
	Utils.launch_drones_per_line(sort_column)
	Utils.launch_drones_per_line(sort_row, North)

	harvest()