from math import sin
from math import pi
import sympy
import requests

req = requests.get('https://dt.miet.ru/ppo_it_final', headers={'X-Auth-Token': '38xdyf6f'}).json()['message']
print(req)


def count_velocity(v_max, w_engine, weight):
    return v_max * (w_engine / 80) * (200 / weight)


def count_population_coefficient(temperature, oxygen):
    return sin(-pi / 2 + pi * (temperature + 0.5 * oxygen) / 40)


def count_new_population(population, coefficient):
    return population + coefficient * population


def count_needed_kp(now_pop, need_pop):
    return need_pop / now_pop - 1


def count_route_max_speed(points: dict) -> list:
    ox_all = []
    for element in points['points']:
        min_ = -1
        max_ = 1
        while abs(min_ - max_) > 0.00001:
            now = (min_ + max_) / 2
            now_weight = 200
            distance = element['distance']
            now_population = 8
            days = 0
            while distance > 0:
                v = count_velocity(2, 79, now_weight)
                now_weight += count_new_population(now_population, now) - now_population
                now_population = count_new_population(now_population, now)
                distance -= v
                days += 1

            if now_population < element['SH']:
                min_ = now
            elif now_population > element['SH']:
                max_ = now

            # print(days, now_population, now)

        need_k = now
        t = 5
        ox = sympy.Symbol('ox')
        eq_k = sympy.sin(-sympy.pi / 2 + sympy.pi * (t + 0.5 * ox) / 40) - need_k
        ox_now_ = min(sympy.solve(eq_k))
        ox_all.append(ox_now_)

    route = []
    for element in points['points']:
        fuel = 0
        now_weight = 200
        distance = element['distance']
        now_population = 8
        days = 0
        t_delta = (max(ox_all) - ox_all[points['points'].index(element)]) / 0.5
        w_omega = 79 - t_delta
        t = 5 + t_delta
        now = count_population_coefficient(t, min(ox_all))
        while distance > 0:
            v = count_velocity(2, w_omega, now_weight)
            now_weight += count_new_population(now_population, now) - now_population
            now_population = count_new_population(now_population, now)
            if now_population >= element['SH']:
                t = 1
                now = count_population_coefficient(t, min(ox_all))
                w_omega = 80
            distance -= v
            days += 1
            fuel += w_omega + t
        route.append({'ox': min(ox_all), 'sh': now_population, 'days': days,
                      'fuel': fuel, 'credits_need': round(min(ox_all) * 7 + fuel * 10)})
    return route


for i in range(len(req)):
    print(f'---------------route: {i}-----------------')
    print(*count_route_max_speed(req[i]), sep='\n')
    print(f'------------------------------------------')
