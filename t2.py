import random

def get_numbers_ticket(min, max, quantity):
    # перевірка правильності введених значень
    is_invalid_number = min < 1 or max > 1000 or quantity < 1

    if is_invalid_number: 
        return []  # повертаємо порожній список, якщо введені значення некоректні
    else:
        # отримання унікальних випадкових чисел в межах від min до max
        random_numbers = random.sample(range(min, max + 1), quantity)
    
        return sorted(random_numbers)  # повертаємо відсортований список чисел

# виклик функції для перевірки
print("Ваші лотерейніі числа:", get_numbers_ticket(1, 500, 6))