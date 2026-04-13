import Utils
import Cactus
import Carrot
import Hay
import Pumpkin
import Treasure
import Wood

def foobar(_):
	pass

CONFIG = {
	Items.Hay: [400000, Hay.main],
	Items.Wood: [400000, Wood.main],
	Items.Carrot: [400000, Carrot.main],
	Items.Pumpkin: [100000, Pumpkin.main],
	# Items.Cactus: [100000, Cactus.main],
	# Items.Weird_Substance: [100000, foobar],
	# Items.Gold: [100000, Treasure.main],
}
LIMITS = {}
CALLABLES = {}
for k in CONFIG:
	LIMITS[k] = CONFIG[k][0]
	CALLABLES[k] = CONFIG[k][1]

def action():
	clear()
	for k in CONFIG:
		if num_items(k) < LIMITS[k]:
			c = num_items(k)
			CALLABLES[k]()
			print(num_items(k) - c)
			return
	

if __name__ == "__main__":
	while True:
		action()
