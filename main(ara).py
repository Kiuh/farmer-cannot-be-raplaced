import Utils
import Cactus
import Carrot
import Hay
import Pumpkin
import Treasure
import WeirdSubstance
import Wood
import Sunflower

def foobar(_):
	pass

CONFIG = {
	Items.Gold: [600*10**3, Treasure.main],
	Items.Hay: [5*10**6, Hay.main],
	Items.Wood: [100*10**6, Wood.main],
	Items.Carrot: [5*10**6, Carrot.main],
	Items.Power: [10*10**3, Sunflower.main],
	Items.Pumpkin: [3*10**6, Pumpkin.main],
	Items.Cactus: [20*10**6, Cactus.main],
	Items.Weird_Substance: [10*10**3, WeirdSubstance.main],
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
