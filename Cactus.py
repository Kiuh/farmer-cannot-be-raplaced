
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

def solve_sort_column():
	def result():
		return sort_column()
	return result

def sort_columns():
	drones = []

	for i in range(1, max_drones()):
		drones.append(spawn_drone(solve_sort_column()))
		move(East)

	solve_sort_column()()

	while get_pos_y() > 0:
		move(North)
	while get_pos_x() > 0:
		move(East)

	for drone in drones:
		wait_for(drone)

def solve_sort_rows():
	def result():
		return sort_row()
	return result

def sort_rows():
	drones = []

	for i in range(1, max_drones()):
		drones.append(spawn_drone(solve_sort_rows()))
		move(North)

	solve_sort_rows()()

	while get_pos_y() > 0:
		move(North)
	while get_pos_x() > 0:
		move(East)

	for drone in drones:
		wait_for(drone)


def main(limits):
	set_world_size(max_drones())

	while num_items(Items.Cactus) < limits[Items.Cactus] and num_items(Items.Pumpkin) > limits[Items.Pumpkin]:
		sort_columns()
		sort_rows()

		harvest()


if __name__ == "__main__":
	main()
			