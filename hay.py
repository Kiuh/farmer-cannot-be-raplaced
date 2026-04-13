import utils

def job():
	for _ in range(10):
		for _ in range(get_world_size()-1):
			harvest()
			move(North)
		harvest()

def main():
	utils.launch_drones_per_line(job)			