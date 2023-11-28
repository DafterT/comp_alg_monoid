from copy import copy

from monoid_1 import Monoid


def print_result(function):
    try:
        print(function())
    except Exception as err:
        print(err)


if __name__ == '__main__':
    monoid = Monoid(
        set(range(-16, 17)),
        lambda a, b: max(a, b)
    )
    print_result(lambda: monoid.multiplication(5, 10))
    print_result(lambda: monoid.multiplication(12, 0))
    print_result(lambda: monoid.multiplication(6, 3))
    print_result(lambda: monoid.multiplication(1, "Hello"))
    print_result(lambda: monoid.find_zero_element())
    print_result(lambda: monoid.check_monoid_multiplication())
    print_result(lambda: monoid.get_elements())
    print_result(lambda: monoid.get_mult_function())
    print_result(lambda: copy(monoid))
