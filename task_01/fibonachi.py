def caching_fibonacci():
    # Створюємо порожній словник для кешування обчислених значень
    cache = {}

    # Внутрішня функція, яка обчислює n-те число Фібоначчі з використанням кешу
    def fibonacci(n):
        # Базові випадки: 0 або 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Якщо значення вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Якщо значення немає у кеші, обчислюємо його рекурсивно і зберігаємо у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci, яка зберігає доступ до кешу
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610