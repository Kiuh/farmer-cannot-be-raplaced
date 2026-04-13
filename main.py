import Utils
import Treasure
import Treasure

hay_limit = 5000
wood_limit = 3000
carrot_limit = 3000

def action():
	if can_harvest():
		harvest()
	
	if num_items(Items.Hay) < hay_limit:
		Utils.hay()
	elif num_items(Items.Wood) < wood_limit:
		Utils.wood()
	elif num_items(Items.Carrot) < carrot_limit:
		Utils.carrot()
	else:
		Utils.pumpkin()
	
def moveH(i):
	if i % 2 == 0:
		move(East)
	else:
		move(West)

def harvestH(i):
	for j in range(0, get_world_size() - 1):
		action()
		moveH(i)
	action()
	move(North)

if __name__ == "__main__":
	clear()
	while True:
		for i in range(0, get_world_size()):
			harvestH(i)
