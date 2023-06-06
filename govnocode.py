import math
import numpy as np

ta_map = {
    0.2: 0.253,
    0.5: 0.674,
    0.8: 1.282,
    0.95: 1.96, 0.99: 2.576,
}

xi_map = {
    0.995: 67.33,
    0.99: 70.06,
    0.975: 74.22,
    0.95: 77.93,
    0.9: 82.36,
    0.5: 99.33,
    0.1: 118.5,
    0.05: 124.3,
    0.025: 129.56,
    0.01: 135.81,
    0.005: 140.17,
}


def double_interval_for_ms(arr, ta):
    n = len(arr)
    S = 0
    for i in range(n):
        S += arr[i] * arr[i]
    S /= n - 1
    average = np.average(arr)
    S -= average * average
    ta = ta_map[ta]
    u1 = average - ta * math.sqrt(S) / math.sqrt(n)
    u2 = average + ta * math.sqrt(S) / math.sqrt(n)
    return u1, u2


def double_interval_for_sv(arr, xi):
    n = len(arr)
    S = 0
    for i in range(n):
        S += arr[i] * arr[i]
    S /= n - 1
    average = np.average(arr)
    S -= average * average
    xi_1 = xi_map[xi / 2]
    xi_2 = xi_map[round(1 - xi / 2, 3)]
    u1 = S * (n - 1) / xi_1
    u2 = S * (n - 1) / xi_2
    return math.sqrt(u1), math.sqrt(u2)
