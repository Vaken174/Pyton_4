import math

def generate_primes():
    current_number = 2 
    while True:
        is_current_prime = True
        # Проверяем делители от 2 до квадратного корня числа
        for potential_divisor in range(2, int(math.sqrt(current_number)) + 1):
            if current_number % potential_divisor == 0:
                is_current_prime = False
                break
        if is_current_prime:
            yield current_number
        current_number += 1

# Пример
prime_generator = generate_primes()
for _ in range(10):  # получаем первые 10 чисел
    print(next(prime_generator))