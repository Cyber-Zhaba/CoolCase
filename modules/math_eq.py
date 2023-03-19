import numpy as np
import requests

print(requests.get('https://dt.miet.ru/ppo_it_final', headers={'X-Auth-Token': '38xdyf6f'}).json()['message'])


def count_velocity(v_max, w_engine, weight):
    return v_max * (w_engine / 80) * (200 / weight)


def count_population_coefficient(temperature, oxygen):
    return np.sin(-np.pi / 2 + np.pi * (temperature + 0.5 * oxygen) / 40)


def count_new_population(population, coefficient):
    return population + coefficient * population
