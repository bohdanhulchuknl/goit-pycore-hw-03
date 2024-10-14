from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів між сьогоднішньою датою та заданою датою.

    Функція приймає один параметр:
    - date (str): Рядок з датою у форматі 'РРРР-ММ-ДД'.

    Функція перетворює рядок дати у об'єкт datetime, обчислює різницю між 
    сьогоднішньою датою та заданою датою, і повертає різницю у днях як ціле число.
    Якщо формат дати неправильний, функція повертає повідомлення про помилку.

    Повертає:
    - int: Кількість днів між сьогоднішньою датою та заданою датою.
    """
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta = today - input_date 
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-01-01"))
