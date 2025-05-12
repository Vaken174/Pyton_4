from math import factorial

# Список квадратов первых 10 натуральных чисел
squared_numbers = [num**2 for num in range(1, 11)]
print(f"1. {squared_numbers}")

# Словарь дней недели
week_days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
day_number_mapping = {day: idx+1 for idx, day in enumerate(week_days)}
print(f"2. {day_number_mapping}")

# Множество тегов библиотек в нижнем регистре
tech_libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
unique_lowercase_tags = {lib.lower() for lib in tech_libraries}
print(f"3. {unique_lowercase_tags}")

# Список четных чисел
number_sequence = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [num for num in number_sequence if num % 2 == 0]
print(f"4. {even_numbers}")

# Словарь факториалов
factorial_values = {number: factorial(number) for number in range(1, 6)}
print(f"5. {factorial_values}")