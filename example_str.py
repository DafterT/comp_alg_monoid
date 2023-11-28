from copy import copy

from monoid_2 import Monoid


def print_result(function):
    try:
        print(function())
    except Exception as err:
        print(err)


if __name__ == "__main__":
    monoid = Monoid(
        str,
        lambda a, b: a + b,
        ""
    )
    print_result(lambda: monoid.multiplication("Компьютерная ", "алгебра"))
    print_result(lambda: monoid.multiplication("Компьютерная алгебра", ""))
    print_result(lambda: monoid.multiplication("", ""))
    print_result(lambda: monoid.multiplication("Hello", "world"))
    print_result(lambda: monoid.multiplication("Numns algebra", 255))
    print_result(monoid.get_elements_type)
    print_result(monoid.get_mult_function)
    print_result(monoid.zero_element)
    print_result(lambda: copy(monoid))