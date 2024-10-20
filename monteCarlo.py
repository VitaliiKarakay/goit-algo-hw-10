import numpy as np


def monte_carlo_integration(f, a, b, max_y, N=100000):
    x_random = np.random.uniform(a, b, N)
    y_random = np.random.uniform(0, max_y, N)

    points_under_curve = np.sum(y_random < f(x_random))
    area_mc = (b - a) * max_y * (points_under_curve / N)

    return area_mc
