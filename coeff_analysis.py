import numpy as np


def calc_individual_appearance_rate(
        current_value, ideal_value, fluctuation_value, min_score=0.6):
    diff = abs(current_value - ideal_value)
    if diff >= fluctuation_value:
        return min_score

    # use linear relationship to map score
    # the smaller the diff, the higher the score
    score = 1 - (1 - min_score) * (diff / fluctuation_value)

    return round(score, 4)


def make_comb_to_appearance_rate_dict(
        combs, ideal_values, fluctuation_values, min_score=0.6):
    comb_to_appearance_rate_dict = {}
    ideal_a, ideal_b, ideal_c = ideal_values
    fluctuation_a, fluctuation_b, fluctuation_c = fluctuation_values
    for (a, b, c) in combs:
        a_appearance_rate = calc_individual_appearance_rate(
            a, ideal_a, fluctuation_a, min_score)
        b_appearance_rate = calc_individual_appearance_rate(
            b, ideal_b, fluctuation_b, min_score)
        c_appearance_rate = calc_individual_appearance_rate(
            c, ideal_c, fluctuation_c, min_score)

        combined_rate = \
            a_appearance_rate * b_appearance_rate * c_appearance_rate
        comb_to_appearance_rate_dict[(a, b, c)] = round(combined_rate, 2)
    return comb_to_appearance_rate_dict


def gen_possible_coeff_values(ideal_value, fluctuation_value, unit):
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
    start = ideal_value - fluctuation_value
    end = ideal_value + fluctuation_value

    values = np.arange(start, end + unit, unit)
    values = values[(values >= 0) & (values <= 1)]

    return values


def find_valid_coeff_combs(
        a_candidates, b_candidates, c_candidates,
        error_unit):
    valid_coeff_combs = []
    for a in a_candidates:
        for b in b_candidates:
            c = 1.0 - a - b  # directly determine c to reduce computation
            if c >= 0 and np.any(np.isclose(c_candidates, c, atol=error_unit)):
                # round is a must to prevent rounding error
                valid_coeff_comb = (round(a, 2), round(b, 2), round(c, 2))
                valid_coeff_combs.append(valid_coeff_comb)
    return valid_coeff_combs


if __name__ == '__main__':

    # Example usage:
    a_candidates = gen_possible_coeff_values(0.5, 0.1, 0.05)
    b_candidates = gen_possible_coeff_values(0.5, 0.2, 0.05)
    c_candidates = gen_possible_coeff_values(0.1, 0.05, 0.01)
    valid_coeff_combs = find_valid_coeff_combs(
        a_candidates, b_candidates, c_candidates, 0.01)

    comb_to_appearance_rate_dict = \
        make_comb_to_appearance_rate_dict(
            valid_coeff_combs,
            (0.5, 0.5, 0.1),
            (0.1, 0.2, 0.05))
