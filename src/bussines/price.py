from typing import Optional
from src.models.price import Price


def get_cost_by_type(v_type: str) -> Optional[int]:
    price = Price.query.filter_by(type=v_type).first()
    return price.cost if price else None
