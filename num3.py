def append_and_print_even_lines(new_content, file_path):
    
    # Открываем файл в режиме добавления
    with open(file_path, 'a') as output_file:
        output_file.write(new_content + '\n')  # Записываем текст с новой строки

    # Читаем содержимое
    with open(file_path, 'r') as input_file:
        all_lines = input_file.readlines()  # Получаем все строки файла

    # Выводим строки с четными индексами (1,3,5.. при нумерации с 0)
    filtered_lines = [
        line_content.strip() 
        for line_number, line_content in enumerate(all_lines) 
        if line_number % 2 != 0
    ]
    
    for filtered_line in filtered_lines:
        print(filtered_line)

# Пример
append_and_print_even_lines("Hello World!", "example.txt")