"""
IS597 Spring 2025 - Final Project
F1 Logistics using Monte Carlo Simulation: Core Functions
Author: Rahul Balasubramani(rahulb6) & Anushree Udhayakumar(au11)
"""

import random
import matplotlib.pyplot as plt

def pert_sample(min_val, mode_val, max_val):
    """
    Generate a sample from a simplified PERT distribution using the mode.

    :param min_val: float, worst-case value
    :param mode_val: float, most likely value
    :param max_val: float, best-case value
    :return: float, a sample from the PERT distribution

    >>> s = pert_sample(0.4, 0.8, 1.0)
    >>> 0.4 <= s <= 1.0
    True
    """
    if not (min_val <= mode_val <= max_val):
        raise ValueError("Invalid PERT parameters: min <= mode <= max must hold.")

    alpha = 4 * (mode_val - min_val) / (max_val - min_val) + 1
    beta = 4 * (max_val - mode_val) / (max_val - min_val) + 1
    sample = random.betavariate(alpha, beta)
    return min_val + sample * (max_val - min_val)


if __name__ == "__main__":

    print("Testing PERT distribution sampling...")
    min_val, mode_val, max_val = 0.4, 0.8, 1.0

    for i in range(10):
        sample = pert_sample(min_val, mode_val, max_val)
        print(f"Sample {i+1}: {sample:.4f}")
