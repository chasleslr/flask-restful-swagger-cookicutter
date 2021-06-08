from ..extensions import db


class MyModel(db.Model):
    id = db.Column(db.Integet, primary_key=True)
