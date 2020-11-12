from .extensions import db


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donator = db.Column(db.String(100))
    address = db.Column(db.String(200), nullable=True)
    item = db.Column(db.String(200))
    dismount = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime())
    collected = db.Column(db.Boolean, default=False)

    def __init__(self, donator, item, date, dismount=False, address=''):
        self.donator = donator
        self.address = address
        self.item = item
        self.dismount = dismount
        self.date = date
        self.collected = False
