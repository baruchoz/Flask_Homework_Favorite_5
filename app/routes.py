from app import app
from flask import render_template

@app.route('/') 
def index():
    name = 'Greetings Earthlings!'
    title = 'Baruchs Blog'
    return render_template('index.html', greeting=name, title=title)

@app.route('/favorite_5') 
def artists():
    title = 'Baruchs Favorite 5'
    artists = ['Odesza', 'Flume', 'Bonobo', 'Porter Robinson', 'Louis The Child']
    return render_template('favorite_5.html', title=title, artists=artists)
