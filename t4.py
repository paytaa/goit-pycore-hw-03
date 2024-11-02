from datetime import timedelta, datetime

# список користувачів з їхніми днями народження
users = [
    {"full_name": "John Doe", "birthday": "1985.11.5"},
    {"full_name": "Jane Smith", "birthday": "1990.11.7"},
    {"full_name": "Jane Smith 2", "birthday": "1990.1.12"}
]

def get_upcoming_birthdays(users):
    # отримуємо сьогоднішню дату
    today = datetime.today().date()
    # встановлюємо кінцеву дату через 7 днів від сьогодні
    end_date = today + timedelta(days=7)
    # список для зберігання користувачів з ДР на цьому тіжні
    upcoming_birthdays = []

    for user in users:
        # конвертуємо рядок у дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # змінюємо рік дня народження на поточний рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # якщо день народження вже минув, змінюємо його на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        # перевірка чи ДР потрапляє у проміжок цього тижня
        if today <= birthday_this_year <= end_date:
            day_of_week = birthday_this_year.weekday()  # визначаємо день тижня
            if day_of_week in (5, 6):  # субота або неділя
                delta_days = 7 - day_of_week  # обчислюємо, скільки днів додати до понеділка
                message_date = birthday_this_year + timedelta(days=delta_days)
            else:
                message_date = birthday_this_year

            # додаємо інформацію про користувача у список
            upcoming_birthdays.append({
                "full_name": user["full_name"],
                "congratulation_date": message_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# отримуємо список днів народження на цьому тижні
upcoming_birthdays = get_upcoming_birthdays(users)
print("This week birthdays:", upcoming_birthdays)
