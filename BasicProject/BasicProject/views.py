"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from BasicProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cred_user = request.form["username"]
        cred_pass = request.form["psw"]

        if (cred_user == 'user') and (cred_pass == "pass"):
            return render_template(
                'services.html',
                title='Services',
                year=datetime.now().year,
                message='Welcome: ' + cred_user)
    else:
        return render_template(
            'services.html',
            title='Services',
            year=datetime.now().year,
            message='Welcome: Please login.')

    return render_template(
        'services.html',
        title='Services',
        year=datetime.now().year,
        message='Welcome: Please login.')


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

@app.route('/services')
def services():
    """Renders the services page."""
    fake_service = 'air supply'
    fake_delivery = ' the atmosphere'
    return render_template(
        'services.html',
        title='Services',
        year=datetime.now().year,
        message='Our services include: ' + fake_service + ' delivered via ' + fake_delivery
    )

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')

""" @app.route('/hello/<name>' incomplete) """
