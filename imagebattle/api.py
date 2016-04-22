from flask import redirect
from imagebattle import app, db


@app.route('/choose/<int:winner>/<int:looser>', methods=['GET'])
def choose(winner, looser):
    return redirect("/", code=302)
