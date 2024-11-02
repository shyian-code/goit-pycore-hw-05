import re
from typing import Callable

# Функція-генератор для ідентифікації та повернення дійсних чисел з тексту
def generator_numbers(text: str):

    # Знаходимо всі дійсні числа в тексті за допомогою регулярного виразу
    for match in re.finditer(r'\b\d+\.\d+\b', text):
        yield float(match.group())  # Повертаємо кожне знайдене число як float

# Функція для підсумовування чисел, отриманих від generator_numbers
def sum_profit(text: str, func: Callable):
    return sum(func(text))  # Викликаємо generator_numbers і підсумовуємо всі значення


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
