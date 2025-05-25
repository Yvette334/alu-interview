#!/usr/bin/python3
"""Module for the rain function
"""


def rain(walls):
    """Function to find the maximum rain collected
    by a series of walls
    """
    n = len(walls)

    if n == 0:
        return 0

    total_volume = 0

    # Find the highest element to the left of each element
    highest_left = [0] * n
    highest_left[0] = walls[0]
    for i in range(1, n):
        highest_left[i] = max(highest_left[i - 1], walls[i])

    # Find the highest wall to the right of each
    highest_right = [0] * n
    highest_right[-1] = walls[-1]
    for i in range(n - 2, -1, -1):
        highest_right[i] = max(highest_right[i + 1], walls[i])

    # Calculate the accumulated water element by element
    for i in range(0, n):
        total_volume += min(highest_left[i], highest_right[i]) - walls[i]

    return total_volume
