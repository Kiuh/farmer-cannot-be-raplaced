# noqa F403

from __builtins__ import *
from utils import fly_to, quicksort


def plant_sunflowers(length):
    petals = []
    for _ in range(7, 15 + 1):
        petals.append([])

    for idx in range(length):
        if get_ground_type() != Grounds.Soil:
            till()
        plant(Entities.Sunflower)
        use_item(Items.Water)
        petal_count = measure()
        petals[petal_count - 7].append(get_pos_y())

        move(North)

    return petals


def spawn_plant_task(length):
    def inner():
        return plant_sunflowers(length)

    return inner


def spawn_harvest_task(petals):
    def inner():
        harvest_sunflowers(petals)

    return inner


def harvest_sunflowers(petals):
    x = get_pos_x()
    petals = quicksort(petals)
    for y in petals:
        fly_to(x, y)
        harvest()


def main():
    clear()
    drones_count = min(get_world_size(), max_drones())
    handlers = []
    for _ in range(drones_count - 1):
        handlers.append(spawn_drone(spawn_plant_task(get_world_size())))
        move(East)

    main_drone_petal_measurements = plant_sunflowers(get_world_size())
    move(East)

    drone_petal_measurements = []
    for handler in handlers:
        drone_petal_measurements.append(wait_for(handler))

    for petal_count in range(8, 0 - 1, -1):
        for measurements in drone_petal_measurements:
            spawn_drone(spawn_harvest_task(measurements[petal_count]))
            move(East)

        harvest_sunflowers(main_drone_petal_measurements[petal_count])
        move(East)
        


if __name__ == "__main__":
    main()
