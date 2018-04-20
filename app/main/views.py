from . import main
from flask import render_template


@main.route('/')
def index():
    title = "Mai Blog"
    return render_template('index.html', title=title)
