from copy import copy

from monoid_2 import Monoid


def print_result(function):
    try:
        print(function())
    except Exception as err:
        print(err)


if __name__ == "__main__":
    monoid = Monoid(
        int,
        lambda a, b: a * b,
        1
    )
    print_result(lambda: monoid.multiplication(0, 1))
    print_result(lambda: monoid.multiplication(1, 0))
    print_result(lambda: monoid.multiplication(1, 1))
    print_result(lambda: monoid.multiplication(6, 2))
    print_result(monoid.get_elements_type)
    print_result(monoid.get_mult_function)
    print_result(monoid.zero_element)
    print_result(lambda: copy(monoid))