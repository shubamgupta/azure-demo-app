"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app
from FlaskWebProject import model

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        upcoming=model.upcoming_workshops(),
        past=model.past_workshops()
    )


@app.route('/workshop/<title>')
def workshop(title):
    workshop = model.by_title(title)
    return render_template('workshop.html', title=title, workshop=workshop)


@app.route('/series/<name>')
def series(name):
    workshops = model.by_series(name)
    return render_template('series.html', title=name, series=name, workshops=workshops)


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
