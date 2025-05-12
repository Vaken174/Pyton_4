def log_function_call(decorated_func):

    def wrapped_function(*positional_args, **keyword_args):
        # Выводим информацию о вызове функции
        print(f"Функция {decorated_func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {positional_args}")
        print(f"Именованные аргументы: {keyword_args}")

        # Вызываем оригинальную функцию
        calculation_result = decorated_func(*positional_args, **keyword_args)

        # Выводим результат
        print(f"Площадь прямоугольника: {calculation_result}")
        return calculation_result

    return wrapped_function


@log_function_call
def calculate_area(side_length, side_width):
    """Вычисляет площадь прямоугольника"""
    return side_length * side_width


# Примеры
calculate_area(5, 10)  # С позиционными аргументами
calculate_area(side_length=7, side_width=3)  # С именованными аргументами
calculate_area(4, side_width=6)  # Смешанный вариант