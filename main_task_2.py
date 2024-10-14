import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Генерує набір унікальних випадкових чисел у заданому діапазоні.

    Функція приймає три параметри:
    - min (int): Мінімальне можливе число у наборі (не менше 1).
    - max (int): Максимальне можливе число у наборі (не більше 1000).
    - quantity (int): Кількість чисел, які потрібно вибрати (значення між min і max).

    Функція перевіряє коректність параметрів. Якщо параметри не відповідають заданим обмеженням, 
    функція повертає пустий список і виводить повідомлення про помилку. Якщо параметри коректні, 
    функція генерує вказану кількість унікальних випадкових чисел у заданому діапазоні, сортує їх 
    і повертає відсортований список.

    Повертає:
    - list: Відсортований список унікальних випадкових чисел.
    """
    error_message = None
    if min < 1:
        error_message = "!> Переконайтеся, що мінімальне значення не менше 1."
    elif max > 1000:
        error_message = "!> Переконайтеся, що максимальне значення не більше 1000."
    elif quantity < 1:
        error_message = "!> Переконайтеся, що кількість принаймні 1."
    elif quantity > (max - min + 1):
        error_message = "!> Переконайтеся, що кількість не перевищує діапазон між мінімальним і максимальним значенням."

    if error_message:
        print(error_message)
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    sorted_numbers = sorted(numbers)
    return sorted_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers_check_0 = get_numbers_ticket(0, 49, 6)
lottery_numbers_check_1001 = get_numbers_ticket(1, 1001, 6)
lottery_numbers_check_quantity_least_1 = get_numbers_ticket(0, 49, 0)
lottery_numbers_check_quantity_between_min_max = get_numbers_ticket(1, 2, 3)