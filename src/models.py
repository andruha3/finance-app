from . import db


class Companies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(16), nullable=False)
    Date = db.Column(db.String(16), nullable=False)
    Open = db.Column(db.Float, nullable=False)
    High = db.Column(db.Float, nullable=False)
    Low = db.Column(db.Float, nullable=False)
    Close = db.Column(db.Float, nullable=False)
    Adj_Close = db.Column(db.Float, nullable=False)
    Volume = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return {"Name": self.Name, "Date": self.Date}
