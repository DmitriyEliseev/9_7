# Функция для определения простого числа
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Функция декоратор
def is_prime_decorator(func):
    def wrapper(*args):
        result = func(*args)
        if is_prime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime_decorator
def sum_three(a, b, c):
    return a + b + c

# Пример использования
result = sum_three(2, 3, 6)
print(result)
