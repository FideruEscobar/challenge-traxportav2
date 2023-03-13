from datetime import datetime

from src.models.price import Price
from src.models.holiday import Holiday
from src import db
from app import app as app

jour = Price(type='Jour', cost=190)
night = Price(type='Night', cost=19)

christmas = Holiday(name='Christmas', date=datetime(2020, 12, 25).date(), day=25, month=12)
new_year = Holiday(name='New Year', date=datetime(2021, 1, 1).date(), day=1, month=1)


with app.app_context():
    db.create_all()
    db.session.add(jour)
    db.session.add(night)
    db.session.add(christmas)
    db.session.add(new_year)
    db.session.commit()
