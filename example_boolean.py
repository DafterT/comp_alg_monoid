from copy import copy

from monoid_1 import Monoid


def print_result(function):
    try:
        print(function())
    except Exception as err:
        print(err)


if __name__ == '__main__':
    monoid = Monoid(
        {True, False},
        lambda a, b: a or b
    )
    print_result(lambda: monoid.multiplication(True, False))
    print_result(lambda: monoid.multiplication(False, False))
    print_result(lambda: monoid.multiplication(True, True))
    print_result(lambda: monoid.multiplication(False, "Hello"))
    print_result(lambda: monoid.find_zero_element())
    print_result(lambda: monoid.check_monoid_multiplication())
    print_result(lambda: monoid.get_elements())
    print_result(lambda: monoid.get_mult_function())
    print_result(lambda: copy(monoid))
