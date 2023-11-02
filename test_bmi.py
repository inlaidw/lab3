import Lab2.exercise1.bmi as bmi


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.2, 30)
    assert (result == 0)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.2, 50)
    assert (result == 1)


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.2, 5)
    assert (result == -1)
