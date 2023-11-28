class Monoid:
    def __init__(self, elements, mult_function):
        self.__elements = elements
        self.__mult_function = mult_function

    def multiplication(self, element_1, element_2):
        """
        Функция умножения, проверяет корректность введенных элементов,
        после чего выполняет умножение, проверяя результат
        :param element_1: Первый множитель
        :param element_2: Второй множитель
        :return: Результат умножения или строку ошибки
        """
        if element_1 not in self.__elements or element_2 not in self.__elements:
            raise Exception(f"[!] Incorrect input {element_1} or {element_2} not in {self.__elements}")
        result = self.__mult_function(element_1, element_2)
        if result not in self.__elements:
            raise Exception(
                f"[!] Incorrect monoid: {element_1} * {element_2} = {result}\n[!] But {result} not in {self.__elements}"
            )
        return result

    def check_monoid_multiplication(self):
        """
        Проверяет все возможные перемножения в множестве, дабы убедиться
        что они не выходят за само множество сложность O(n^2)
        :return: Ошибку или True
        """
        # Умножение двух элементов остается частью множества
        for i in self.__elements:
            for j in self.__elements:
                try:
                    self.multiplication(i, j)
                except Exception as err:
                    return err
        # При умножении трех элементов можно менять порядок скобок
        for i in self.__elements:
            for j in self.__elements:
                for k in self.__elements:
                    result_1 = self.__mult_function(self.__mult_function(i, j), k)  # (i * j) * k
                    result_2 = self.__mult_function(i, self.__mult_function(j, k))  # i * (j * k)
                    if result_1 != result_2:
                        raise Exception('[!] Бинарная операция не является ассоциативной!')

        return True

    def find_zero_element(self):
        """
        Выполняет поиск нейтрального элемента, сложность O(n^2)
        :return: Нейтральный элемент или None
        """
        for zero in self.__elements:
            for i in self.__elements:
                if self.multiplication(zero, i) != i or self.multiplication(i, zero) != i:
                    break
            else:
                return zero

    def get_elements(self):
        return self.__elements

    def get_mult_function(self):
        return self.__mult_function

    def __copy__(self):
        return Monoid(self.__elements, self.__mult_function)


if __name__ == "__main__":
    x = Monoid({0, 1}, lambda a, b: a * b)
    x.check_monoid_multiplication()
    print(f'zero element: {x.find_zero_element()}')
    print()
    print(x.multiplication(0, 1))
    print(x.multiplication(1, 0))
    print(x.multiplication(1, 1))
    print(x.multiplication(0, 0))
    # print(x.multiplication(1, 2))
