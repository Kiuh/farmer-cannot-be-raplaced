import utils

def job():
	for _ in range(10):
		for _ in range(get_world_size()-1):
			use_item(Items.Fertilizer)
			harvest()
			move(North)
		use_item(Items.Fertilizer)
		harvest()

def main():
	utils.launch_drones_per_line(job)			