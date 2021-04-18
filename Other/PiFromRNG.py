import random
import math


def func():
    return random.random()


def estimate_pi(n):
    yellow = 0
    red = 0
    for i in range(n):
        x, y = func(), func()
        dist = math.sqrt((x**2) + (y**2))
        if dist <= 1:
            red += 1
        else:
            yellow += 1

    pi = 4 * red / (red + yellow)

    return pi


trials = [10**x for x in range(0, 10)]
for n in trials:
    pi = estimate_pi(n)
    space = ' '
    est = round(pi, 5)
    print(f"Pi Estimation: 10^{round(math.log(n, 10), 0)} generations \t {est}{(6-len(str(est)))*space} \t Residual: {round(math.pi - pi, 5)}")