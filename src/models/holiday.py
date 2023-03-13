from src import db


class Holiday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)

    def __int__(self, name, date, day, month):
        self.name = name
        self.date = date
        self.day = day
        self.month = month

    def __repr__(self):
        return '<Holiday %s: %s>' % (self.name, self.date, self.day, self.month)
