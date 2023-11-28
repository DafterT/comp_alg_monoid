from monoid_2 import Monoid

if __name__ == "__main__":
    x = Monoid(int, lambda a, b: a * b, 1)
    print(x.multiplication(0, 1))
    print(x.multiplication(1, 0))
    print(x.multiplication(1, 1))
    print(x.multiplication(6, 2))
    try:
        print(x.multiplication([], 255))
    except Exception as e:
        print(e)
