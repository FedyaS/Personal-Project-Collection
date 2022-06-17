import time
import math


def f(x, y):
    return x + y


def Euler(xn, h, yn):
    yn1 = yn + (h * f(xn, yn))
    xn1 = xn + h

    return (xn1, yn1)


def runge_kutta(xn, h, yn):
    xn1 = xn + h
    k1 = f(xn, yn)
    k2 = f(xn + (0.5 * h), yn + (0.5 * h * k1))
    k3 = f(xn + (0.5 * h), yn + (0.5 * h * k2))
    k4 = f(xn1, yn + (h * k3))

    k = (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    yn1 = yn + h * k

    return xn1, yn1

actual = 2 * math.pow(math.e, 10) - 10 - 1
print("Actual")
print(10, ": ", actual)


def Euler_run():
    h = 0.001
    x1 = 0
    y1 = 1
    xgoal = 10
    runs = int((xgoal - x1) / h)

    start = time.time()

    xn = x1
    yn = y1
    for i in range(runs):
        xn, yn = Euler(xn, h, yn)

    end = time.time()

    print("Euler")
    print(end - start)
    print(xn, ": ", yn)
    error = (yn - actual) / actual
    print("Error: ", error)


def runge_kutta_run():
    h = 0.001
    xn = 0
    yn = 1
    xgoal = 10
    runs = int((xgoal - xn)/h)

    start = time.time()
    for i in range(runs):
        xn, yn = runge_kutta(xn, h, yn)

    end = time.time()

    print("Range-Kutta")
    print(end - start)
    print(xn, ": ", yn)
    error = (yn - actual) / actual
    print("Error: ", error)


Euler_run()
runge_kutta_run()

