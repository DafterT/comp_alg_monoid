class Monoid:
    def __init__(self, elements_type, mult_function, zero_element):
        self.__elements_type = elements_type
        self.__mult_function = mult_function
        self.__zero_element = zero_element

    def multiplication(self, element_1, element_2):
        """
        Функция умножения, проверяет корректность введенных элементов,
        после чего выполняет умножение, проверяя результат
        :param element_1: Первый множитель
        :param element_2: Второй множитель
        :return: Результат умножения или ошибка
        """
        if type(element_1) is not self.__elements_type or type(element_2) is not self.__elements_type:
            raise Exception(f"[!] Incorrect input {element_1} or {element_2} not is {self.__elements_type}")
        result = self.__mult_function(element_1, element_2)
        if type(result) is not self.__elements_type:
            raise Exception(
                f"[!] Incorrect monoid: {element_1} * {element_2} = {result}\n[!] But {result} not is {self.__elements_type}"
            )
        return result

    def get_elements_type(self):
        return self.__elements_type

    def get_mult_function(self):
        return self.__mult_function

    def zero_element(self):
        return self.__zero_element

    def __copy__(self):
        return Monoid(self.__elements_type, self.__mult_function, self.__zero_element)


if __name__ == "__main__":
    x = Monoid(int, lambda a, b: a * b, 1)
    print(x.multiplication(0, 1))
    print(x.multiplication(1, 0))
    print(x.multiplication(1, 1))
    print(x.multiplication(6, 2))
    # print(x.multiplication(1, 2))
