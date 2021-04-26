import os
import sys


def get_first_digit(number):
    while number >= 10:
        number = (number/10)
        number = number//1
        number = int(number)
    return number

# os.chdir('C:\\Users\\fedse\\PycharmProjects\\First_Project\\venv')
# city_populations = os.path.join('C:\\Users\\fedse\\PycharmProjects\\First_Project\\venv', 'CityPopulationsUSA.txt')
# Using relative paths instead


name = "Euler.txt"
data_list = filter(None, open(name, "r").read().splitlines())

first_digits = []


def get_all_first_digits():
    for population in data_list:
        first_digit = get_first_digit(int(population))
        first_digits.append(first_digit)


def calc_distribution(data):
    results = [0 for i in range(10)]
    for x in data:
        results[0] += 1
        results[x] += 1

    return results


get_all_first_digits()
distribution = calc_distribution(first_digits)

print(first_digits)

for i in range(1, len(distribution)):
    print(f'{i}: {round(100*distribution[i]/distribution[0], 2)}%')