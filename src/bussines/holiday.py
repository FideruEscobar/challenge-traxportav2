from typing import Optional
from src.models.holiday import Holiday


def get_holiday_by_date(day: int, month: int) -> Optional[int]:
    holiday = Holiday.query.filter(Holiday.day == day).filter(Holiday.month == month).first()
    return holiday.id if holiday else None

