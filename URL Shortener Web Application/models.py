from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512), nullable=False)
    short_id = db.Column(db.String(6), unique=True, nullable=False)

    def __init__(self, original_url, short_id):
        self.original_url = original_url
        self.short_id = short_id
