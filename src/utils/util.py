from flask import jsonify
from datetime import datetime


def output_json(data: dict):
    return jsonify(data)


def date_to_datetime(date: str) -> datetime:
    d = datetime.strptime(date, '%Y-%m-%d')
    return d

