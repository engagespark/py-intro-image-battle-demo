from imagebattle import db


class Image(db.Model):
    image_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, unique=True)
    ups = db.Column(db.Integer)
    totals = db.Column(db.Integer)

    def __init__(self, url):
        self.url = url
        self.ups = 0
        self.totals = 0
