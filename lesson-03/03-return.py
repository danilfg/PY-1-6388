# calculates with args and result, recursion/factorial
def super_print(value: str) -> str:
    """
    Вывод текста с префиском 'Message'
    :param value: Значение для вывода
    :return:
    """
    output = f"Message: {value}"
    return output


# a = super_print('John')
#
# print(a)

# 5! = 1 * 2 * 3 * 4 * 5
result = 1

for x in range(5):
    result = result * x


def factorial(n: int) -> int:
    # if n <= 0:
    #     return 1
    # else:
    #     return n * factorial(n - 1)
    #
    return 1 if n <= 0 else n * factorial(n - 1)


print(factorial(5))  # 120
