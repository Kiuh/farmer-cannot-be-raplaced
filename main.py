import utils
import cactus
import carrot
import hay
import pumpkin
import treasure
import weird_substance
import wood
import sunflower

def foobar(_):
	pass

CONFIG = {
	Items.Hay: [10*10**6, hay.main],
	Items.Wood: [100*10**6, wood.main],
	Items.Carrot: [70*10**6, carrot.main],
	Items.Power: [10*10**3, sunflower.main],
	Items.Pumpkin: [30*10**6, pumpkin.main],
	Items.Cactus: [20*10**6, cactus.main],
	Items.Weird_Substance: [10*10**3, weird_substance.main],
	Items.Gold: [10*10**6, treasure.main],
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
			if k == Items.Gold:
				CALLABLES[k](LIMITS)
			else:
				CALLABLES[k]()
			print(num_items(k) - c)
			return
	

if __name__ == "__main__":
	while True:
		action()
