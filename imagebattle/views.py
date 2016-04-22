from random import sample

from flask import render_template
from imagebattle import app
from .models import Image


@app.route('/', methods=['GET', 'POST'])
def index():
    all_ids = Image.query.values(Image.image_id)

    left_res, right_res = sample(list(all_ids), 2)
    left_id = left_res[0]
    right_id = right_res[0]

    left = Image.query.filter(Image.image_id == left_id).one()
    right = Image.query.filter(Image.image_id == right_id).one()

    return render_template('index.html', left=left, right=right)


@app.route('/leading', methods=['GET', 'POST'])
def leading():
    return render_template('leading.html')
