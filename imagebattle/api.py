from flask import redirect
from imagebattle import app, db
from .models import Image


@app.route('/choose/<int:winner_id>/<int:looser_id>', methods=['GET'])
def choose(winner_id, looser_id):
    winner = Image.query.filter_by(image_id=winner_id).one()
    looser = Image.query.filter_by(image_id=looser_id).one()
    winner.ups += 1
    winner.totals+=1
    looser.totals+=1
    db.session.commit()
    return redirect("/", code=302)
