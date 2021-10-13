from app import app
from flask import render_template
from app.forms import PhonebookForm, UserInfoForm



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

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register Account'
    register_form = UserInfoForm()
    if register_form.validate_on_submit():
        print('Hello this form has been submitted correctly')
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        print(username, email, password)
        
    return render_template('register.html', title=title, form=register_form)

@app.route('/register_phone_number', methods=['GET', 'POST'])
def Register_Phone_Number():
    title = 'Register Phone Number'
    register_phone_form = PhonebookForm()
    if register_phone_form.validate_on_submit():
        print(('Hello this phonebook form has been submitted correctly'))
        first_name = register_phone_form.first_name.data
        last_name = register_phone_form.last_name.data
        phone_number = register_phone_form.phone_number.data
        print(first_name, last_name, phone_number)

    return render_template('register_phone_number.html', title=title, phonebook_form=register_phone_form)