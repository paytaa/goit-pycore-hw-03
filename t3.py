import re

# список різноформатних номерів 
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    # видаляємо всі символи, які не є цифрами або знаком +
    rewrited_number = re.sub(r'[^\d+\+]', '', phone_number.strip())

    # якщо номер починається з 380, додаємо + на початок
    if rewrited_number.startswith('380'):
        return '+' + rewrited_number

    # якщо номер не починається з '+', додаємо код країни +38
    if not rewrited_number.startswith('+'):
        return '+38' + rewrited_number

    # повертаємо номер у нормалізованому форматі
    return rewrited_number

# нормалізуємо всі номери з початкового списку
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# виводимо нормалізовані номери телефонів
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)