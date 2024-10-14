from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    """
    Визначає, кого з колег потрібно привітати з днем народження на наступному тижні, включаючи поточний день.
    Якщо день народження припадає на вихідний, дата привітання переноситься на наступний робочий день.

    Параметри:
    users (list): Список словників, де кожен словник містить ключі 'name' (ім'я користувача) та 'birthday' (день народження у форматі 'рік.місяць.дата').

    Повертає:
    list: Список словників, де кожен словник містить ключі 'name' (ім'я користувача) та 'congratulation_date' (дата привітання у форматі 'рік.місяць.дата').
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:  # 5 - Saturday, 6 - Sunday
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.10.19"},
    {"name": "Jane Smith", "birthday": "1990.10.20"},
    {"name": "Bohdan Hulchuk", "birthday": "1990.10.15"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)