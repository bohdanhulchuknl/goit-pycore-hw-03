import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    error_message = None
    if min < 1:
        error_message = "Ensures that min is at least 1."
    elif max > 1000:
        error_message = "Ensures that max does not exceed 1000."
    elif quantity < 1:
        error_message = "Ensures that quantity is at least 1."
    elif quantity > (max - min + 1):
        error_message = "Ensures that quantity does not exceed the range between min and max."

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