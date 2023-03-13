import math
from src.utils.util import output_json, date_to_datetime
from src.bussines.price import get_cost_by_type
from src.bussines.holiday import get_holiday_by_date
from src.bussines.constants import JOUR, children, young, older_adult


def get_ticket_price(payload):
    v_type = payload['type']
    age = payload['age']
    date = payload['date']
    is_younger = False

    # Get price of ticket
    cost = get_cost_by_type(v_type)
    if not cost:
        return output_json({'error': 'something failed'})

    # Validate time
    if v_type == JOUR:
        # Check if people is children
        if check_age(age, children):
            cost = 0
        # Check if people is younger
        elif check_age(age, young):
            cost = cost * 0.7
            is_younger = True
        # Check if people is older adult
        elif check_age_older_adult(age):
            cost = cost * 0.75
        if is_monday(date) and not is_younger:
            if not is_holiday(date):
                # Discount
                cost = cost * (1 - 35/100)
    else:
        if check_age(age, children):
            cost = 0
        elif check_age_older_adult(age):
            cost = cost * 0.40

    return output_json({'cost': math.ceil(cost), 'message': 'success'})


def check_age(age: int, age_limit: int) -> bool:
    return bool(age < age_limit)


def check_age_older_adult(age: int) -> bool:
    return bool(age > older_adult)


def is_holiday(date: str) -> bool:
    day = date_to_datetime(date).day
    month = date_to_datetime(date).month
    return bool(get_holiday_by_date(day, month))


def is_monday(date) -> bool:
    return bool(date_to_datetime(date).weekday() == 0)






