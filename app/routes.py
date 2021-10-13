from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import PostForm, UserInfoForm, PhonebookForm
from app.models import Post, Phonebook, User
from app import db



@app.route('/') 
def index():
    name = 'Greetings Earthlings!'
    title = 'Blog Homepage'

    return render_template('index.html', greeting=name, title=title)


@app.route('/favorite_5') 
def artists():
    title = 'Favorite 5'
    artists = ['Odesza', 'Flume', 'Bonobo', 'Porter Robinson', 'Louis The Child']

    return render_template('favorite_5.html', title=title, artists=artists)


@app.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register'
    register_form = UserInfoForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).all()
        if existing_user:
            # Flash a warning message 
            flash(f'The username {username} is already registered. Please try again.', 'danger')
            # Redirect back to the register page
            return redirect(url_for('register'))        

        new_user = User(username, email, password)

        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you {username}, you have successfully registered!', 'success')

        return redirect(url_for('index'))

    return render_template('register.html', title=title, form=register_form)


@app.route('/register_phone_number', methods=['GET', 'POST'])
def Register_Phone_Number():
    title = 'Phonebook'
    register_phone_form = PhonebookForm()
    if register_phone_form.validate_on_submit():
        print(('Hello this phonebook form has been submitted correctly'))
        first_name = register_phone_form.first_name.data
        last_name = register_phone_form.last_name.data
        phone_number = register_phone_form.phone_number.data
        address = register_phone_form.address.data
        print(first_name, last_name, phone_number, address)
        
        new_phonebook = Phonebook(first_name, last_name, phone_number, address)

        db.session.add(new_phonebook)
        db.session.commit()

    return render_template('register_phone_number.html', title=title, phonebook_form=register_phone_form)

@app.route('/createpost', methods=['GET', 'POST'])
def createpost():
    title = 'Create Post'
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_post = Post(title, content, user_id=1)

        db.session.add(new_post)
        db.session.commit()

    return render_template('createpost.html', title=title, form=form)