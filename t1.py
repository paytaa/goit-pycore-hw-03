from datetime import datetime

def get_days_from_today(date):
    # перетворюємо рядок дати на об'єкт datetime
    input_date = datetime.strptime(date, '%Y-%m-%d').date()
    
    # отримуємо поточну дату
    today_date = datetime.now().date()
    
    # обчислюємо різницю між датами
    difference = today_date - input_date
    
    # повертаємо різницю в днях (ціле число)
    return difference.days

print(get_days_from_today('2024-09-09'))
