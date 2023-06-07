import math

import numpy as np
from govnocode import double_interval_for_ms, double_interval_for_sv

# COLORS
C_RED = '\033[91m'  # 🟥
C_YELLOW = '\033[93m'  # 🟨
C_GREEN = '\033[92m'  # 🟩
C_END = '\033[0m'  # ⬜

variant = 120 % 11 + 11 * 2
print(f'{C_RED}Variant:{C_END} {variant}')

n = 134
mu = 0
sigma = 1.7

numbers = np.random.normal(mu, sigma, n)
get_interval_length = lambda a, b: b - a

left_ms, right_ms = double_interval_for_ms(numbers, 0.95)
left_sv, right_sv = double_interval_for_sv(numbers, 0.95)

print(f'{C_RED}Довірчі інтервали для математичного сподівання:{C_END} {left_ms} ≤ µ ≤ {right_ms}')
print(f'{C_RED}Довірчі інтервали для середньоквадратичного відхилення:{C_END} {left_sv} ≤ σ ≤ {right_sv}')

data = {
    0.01: get_interval_length(*double_interval_for_ms(numbers, 0.01)),
    0.1: get_interval_length(*double_interval_for_ms(numbers, 0.1)),
    0.2: get_interval_length(*double_interval_for_ms(numbers, 0.2)),
    0.3: get_interval_length(*double_interval_for_ms(numbers, 0.3)),
    0.4: get_interval_length(*double_interval_for_ms(numbers, 0.4)),
    0.5: get_interval_length(*double_interval_for_ms(numbers, 0.5)),
    0.75: get_interval_length(*double_interval_for_ms(numbers, 0.75)),
    0.8: get_interval_length(*double_interval_for_ms(numbers, 0.8)),
    0.95: get_interval_length(*double_interval_for_ms(numbers, 0.95)),
    0.99: get_interval_length(*double_interval_for_ms(numbers, 0.99)),
    0.999: get_interval_length(*double_interval_for_ms(numbers, 0.999)),
}

data2 = {
    0.01: get_interval_length(*double_interval_for_sv(numbers, 0.01)),
    0.1: get_interval_length(*double_interval_for_sv(numbers, 0.1)),
    0.2: get_interval_length(*double_interval_for_sv(numbers, 0.2)),
    0.3: get_interval_length(*double_interval_for_sv(numbers, 0.3)),
    0.4: get_interval_length(*double_interval_for_sv(numbers, 0.4)),
    0.5: get_interval_length(*double_interval_for_sv(numbers, 0.5)),
    0.75: get_interval_length(*double_interval_for_sv(numbers, 0.75)),
    0.8: get_interval_length(*double_interval_for_sv(numbers, 0.8)),
    0.95: get_interval_length(*double_interval_for_sv(numbers, 0.95)),
    0.99: get_interval_length(*double_interval_for_sv(numbers, 0.99)),
    0.999: get_interval_length(*double_interval_for_sv(numbers, 0.999)),
}

data3 = {
    30: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 30), 0.95)),
    50: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 50), 0.95)),
    100: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 100), 0.95)),
    150: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 150), 0.95)),
    200: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 200), 0.95)),
    250: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 250), 0.95)),
    300: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 300), 0.95)),
    350: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 350), 0.95)),
}

data4 = {
    30: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 30), 0.95)),
    50: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 50), 0.95)),
    100: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 100), 0.95)),
    150: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 150), 0.95)),
    200: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 200), 0.95)),
    250: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 250), 0.95)),
    300: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 300), 0.95)),
    350: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 350), 0.95)),
}


def closure_subtracted_value(subtraction_value):
    return lambda x: x - subtraction_value


def get_correlation_coefficient(data):
    to_second_power = lambda x: x ** 2
    get_mathematical_expectation = lambda arr: sum(map(lambda x: x * (1 / len(arr)), list(arr)))

    x = list(data.keys())
    y = list(data.values())

    M_x = get_mathematical_expectation(x)
    M_y = get_mathematical_expectation(y)

    xyu = [xyu1 * xyu2 for xyu1, xyu2 in
           zip(list(map(closure_subtracted_value(M_x), x)), list(map(closure_subtracted_value(M_y), y)))]
    cov_xy = get_mathematical_expectation(xyu)

    x_standard_deviation = math.pow(sum(map(to_second_power, x)) / (len(x) - 1) - M_x ** 2, 0.5)
    y_standard_deviation = math.pow(sum(map(to_second_power, y)) / (len(y) - 1) - M_y ** 2, 0.5)

    return cov_xy / (x_standard_deviation * y_standard_deviation)


print(f"{C_YELLOW}\nДовірчі інтервали для різних значень рівня довіри {C_END}")
print(f"{C_GREEN}Для середнього значення {C_END}")
for key in data.keys():
    i, j = double_interval_for_ms(numbers, key)
    print(f"{key}: {i} ≤ µ ≤ {j}, довжина інтервалу: {get_interval_length(i, j)}")
print(f"{C_GREEN}Для середнього квадратичного відхилення {C_END}")
for key in data2.keys():
    i, j = double_interval_for_sv(numbers, key)
    print(f"{key}: {i} ≤ σ ≤ {j}, довжина інтервалу: {get_interval_length(i, j)}")

print(f"{C_YELLOW}\nДовірчі інтервали для різних розмірів вибірки {C_END}")
print(f"{C_GREEN}Для середнього значення {C_END}")
for key in data3.keys():
    i, j = double_interval_for_ms(np.random.normal(mu, sigma, key), 0.95)
    print(f"{key}: {i} ≤ µ ≤ {j}, довжина інтервалу: {get_interval_length(i, j)}")
print(f"{C_GREEN}Для середнього квадратичного відхилення {C_END}")
for key in data4.keys():
    i, j = double_interval_for_sv(np.random.normal(mu, sigma, key), 0.95)
    print(f"{key}: {i} ≤ σ ≤ {j}, довжина інтервалу: {get_interval_length(i, j)}")


print(f"{C_RED}\nКоефіцієнт кореляції {C_END}")
print(f"{C_YELLOW}\nДля різних значень рівня довіри {C_END}")
print(f"{C_GREEN}Для середнього значення {C_END}")
print(get_correlation_coefficient(data))
print(f"{C_GREEN}Для середнього квадратичного відхилення {C_END}")
print(get_correlation_coefficient(data2))
print(f"{C_YELLOW}\nДля різних розмірів вибірки {C_END}")
print(f"{C_GREEN}Для середнього значення {C_END}")
print(get_correlation_coefficient(data3))
print(f"{C_GREEN}Для середнього квадратичного відхилення {C_END}")
print(get_correlation_coefficient(data4))



