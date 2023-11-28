from monoid_2 import Monoid

if __name__ == "__main__":
    x = Monoid(str, lambda a, b: a + b, "")
    print(x.multiplication("Компьютерная ", "алгебра"))
    print(x.multiplication("Компьютерная алгебра", ""))
    print(x.multiplication("", ""))
    print(x.multiplication("Hello", "world"))
    try:
        print(x.multiplication("Numns algebra", 255))
    except Exception as e:
        print(e)
