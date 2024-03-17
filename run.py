from coeff_analysis import find_valid_coeff_combs, gen_possible_coeff_values
from coeff_analysis import make_comb_to_appearance_rate_dict
from decision_optimization import compute_decision_order_and_expected_value


def make_xyz_combs():
    xyz1 = (70, 60, 30)
    xyz2 = (65, 65, 35)
    xyz3 = (75, 55, 30)
    xyz4 = (80, 50, 30)
    xyz5 = (70, 65, 25)
    xyz6 = (55, 70, 50)
    xyz7 = (70, 50, 45)
    return [xyz1, xyz2, xyz3, xyz4, xyz5, xyz6, xyz7]


if __name__ == '__main__':
    # define parameters
    a_ideal_value = 0.35
    b_ideal_value = 0.55
    c_ideal_value = 0.1
    a_fluctuation_value = 0.1
    b_fluctuation_value = 0.2
    c_fluctuation_value = 0.05
    a_unit = 0.02
    b_unit = 0.02
    c_unit = 0.01

    a_candidates = gen_possible_coeff_values(
        a_ideal_value, a_fluctuation_value, a_unit)
    b_candidates = gen_possible_coeff_values(
        b_ideal_value, b_fluctuation_value, b_unit)
    c_candidates = gen_possible_coeff_values(
        c_ideal_value, c_fluctuation_value, c_unit)

    valid_coeff_combs = find_valid_coeff_combs(
        a_candidates, b_candidates, c_candidates,
        min(a_unit, b_unit, c_unit))

    comb_to_appearance_rate_dict = \
        make_comb_to_appearance_rate_dict(
            valid_coeff_combs,
            (a_ideal_value, b_ideal_value, c_ideal_value),
            (a_fluctuation_value, b_fluctuation_value, c_fluctuation_value))
    xyz_combs = make_xyz_combs()

    is_minimize = True
    decision_order = compute_decision_order_and_expected_value(
        xyz_combs, comb_to_appearance_rate_dict, is_minimize)
    print(decision_order)
