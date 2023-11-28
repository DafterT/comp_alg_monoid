from monoid_2 import Monoid


if __name__ == "__main__":
    x = Monoid(list, lambda a, b: a + b, [])
    print(x.multiplication([1,2,3], [4,5,6]))
    print(x.multiplication([1,2,3,4,5,6], []))
    print(x.multiplication([], []))
    try:
        print(x.multiplication([], 255))
    except Exception as e:
        print(e)