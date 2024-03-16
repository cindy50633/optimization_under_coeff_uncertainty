import numpy as np


def gen_possible_coeff_values(ideal_value, fluctuation, unit):
    """
    Generate all possible discrete values for a coefficient
    within its fluctuation range.

    Parameters:
    - ideal_value: The ideal (central) value of the coefficient.
    - fluctuation: The maximum fluctuation allowed from the ideal value.
    - unit: The step size for discretization within the fluctuation range.

    Returns:
    - A numpy array containing all discrete values within fluctuation range.
    """
    start = ideal_value - fluctuation
    end = ideal_value + fluctuation

    values = np.arange(start, end + unit, unit)    
    values = values[(values >= 0) & (values <= 1)]

    return values


def find_valid_coeff_combs(
        a_candidates, b_candidates, c_candidates,
        error_unit,
        use_appearance_rate):
    valid_coeff_combs = []
    for a in a_candidates:
        for b in b_candidates:
            c = 1.0 - a - b  # directly determine c to reduce computation
            if c >= 0 and np.any(np.isclose(c_candidates, c, atol=error_unit)):
                # round is a must to prevent rounding error
                valid_coeff_comb = (round(a, 2), round(b, 2), round(c, 2))
                valid_coeff_combs.append(valid_coeff_comb)
    return valid_coeff_combs


# Example usage:
a_candidates = gen_possible_coeff_values(0.5, 0.1, 0.05)
b_candidates = gen_possible_coeff_values(0.5, 0.2, 0.05)
c_candidates = gen_possible_coeff_values(0.1, 0.05, 0.01)
valid_coeff_combs = find_valid_coeff_combs(
    a_candidates, b_candidates, c_candidates, 0.01)


print(a_candidates)
print(b_candidates)
print(c_candidates)
print(valid_coeff_combs)
print(len(valid_coeff_combs))
