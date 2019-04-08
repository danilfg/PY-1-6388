# simple callable
def super_print(value: str) -> None:  # void
    """
    Вывод текста с префиском 'Message'
    :param value: Значение для вывода
    :return: ничего не возвращает
    """
    output = f"Message: {value}"
    print(output)


super_print("John Doe")
super_print(100)
