def calc_objective_function_result(a, b, c, x, y, z):
    value = a * x + b * y + c * z
    return round(value, 2)


def compute_decision_order_and_expected_value(
        xyz_combs, comb_to_appearance_rate_dict, is_minimize):
    xyz_with_score_list = []
    for x, y, z in xyz_combs:
        total_value = 0
        for (a, b, c), appearance_rate in comb_to_appearance_rate_dict.items():
            value = calc_objective_function_result(a, b, c, x, y, z)
            weighted_value = value * appearance_rate
            total_value += weighted_value
        xyz_with_score_list.append(((x, y, z), round(total_value, 4)))

    # sort by total_score
    if is_minimize:
        xyz_with_score_list.sort(key=lambda item: item[1], reverse=False)
    else:
        xyz_with_score_list.sort(key=lambda item: item[1], reverse=True)

    return xyz_with_score_list
