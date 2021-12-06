from typing import List
import numpy as np


def simulate_growth(initial_population: List[int], days_to_simulate) -> np.ndarray:
    population_vector = np.zeros(shape=(9, 1))

    for timer in initial_population:
        population_vector[timer] += 1

    update_rule = np.asmatrix(
        data=[
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    )

    return np.linalg.matrix_power(update_rule, days_to_simulate) @ population_vector

if __name__ == '__main__':
    file_path = 'inp-day6.txt'

    initial_population: List[int] = [int(timer) for timer in open(file_path, 'r').readline().split(',')]

    print(
        'The answer to part one is {}'.format(
            np.sum(
                simulate_growth(
                    initial_population=initial_population,
                    days_to_simulate=80
                )
            )
        )
    )

    print(
        'The answer to part two is {}'.format(
            np.sum(
                simulate_growth(
                    initial_population=initial_population,
                    days_to_simulate=256
                )
            )
        )
    )