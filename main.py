import math

import numpy as np
from govnocode import double_interval_for_ms, double_interval_for_sv

# COLORS
C_RED = '\033[91m'  # 🟥
C_YELLOW = '\033[93m'  # 🟨
C_END = '\033[0m'  # ⬜

variant = 120 % 11 + 11 * 2
print(f'{C_RED}Variant:{C_END} {variant}')

n = 134
mu = 0
sigma = 1.7

numbers = np.random.normal(mu, sigma, n)
print(numbers)

ta_map = {
    0.2: 0.253,
    0.5: 0.674,
    0.8: 1.282,
    0.95: 1.96,
    0.99: 2.576,
}

get_interval_length = lambda a, b: b - a

data = {
    0.2: get_interval_length(*double_interval_for_ms(numbers, 0.2)),
    0.5: get_interval_length(*double_interval_for_ms(numbers, 0.5)),
    0.8: get_interval_length(*double_interval_for_ms(numbers, 0.8)),
    0.95: get_interval_length(*double_interval_for_ms(numbers, 0.95)),
    0.99: get_interval_length(*double_interval_for_ms(numbers, 0.99)),
}

data2 = {
    1.0: get_interval_length(*double_interval_for_sv(numbers, 1.0)),
    0.2: get_interval_length(*double_interval_for_sv(numbers, 0.2)),
    0.1: get_interval_length(*double_interval_for_sv(numbers, 0.1)),
    0.5: get_interval_length(*double_interval_for_sv(numbers, 0.05)),
    0.02: get_interval_length(*double_interval_for_sv(numbers, 0.02)),
    0.01: get_interval_length(*double_interval_for_sv(numbers, 0.01)),
}

data3 = {
    150: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 150), 0.95)),
    200: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 200), 0.95)),
    250: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 250), 0.95)),
    300: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 300), 0.95)),
    350: get_interval_length(*double_interval_for_ms(np.random.normal(mu, sigma, 350), 0.95)),
}

data4 = {
    150: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 150), 0.05)),
    200: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 200), 0.05)),
    250: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 250), 0.05)),
    300: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 300), 0.05)),
    350: get_interval_length(*double_interval_for_sv(np.random.normal(mu, sigma, 350), 0.05)),
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


print(f"Correlation coefficient is {get_correlation_coefficient(data)}")
print(f"Correlation coefficient is {get_correlation_coefficient(data2)}")
print(f"Correlation coefficient is {get_correlation_coefficient(data3)}")
print(f"Correlation coefficient is {get_correlation_coefficient(data4)}")
