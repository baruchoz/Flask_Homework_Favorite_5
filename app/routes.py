from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user ,logout_user
from app.forms import LoginForm, PostForm, UserInfoForm, PhonebookForm, LoginForm
from app.models import Post, Phonebook, User
from app import db



@app.route('/') 
def index():
    title = 'Blog Homepage'

    return render_template('index.html', title=title)


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

        # Check if username from the form already exists in the User table
        existing_user = User.query.filter_by(username=username).all()
        # If there is a user with that username, message them asking them to try again
        if existing_user:
            # Flash a warning message 
            flash(f'The username {username} is already registered. Please try again.', 'danger')
            # Redirect back to the register page
            return redirect(url_for('register'))        

        # Create a new user instance
        new_user = User(username, email, password)
        # Add that user to the database
        db.session.add(new_user)
        db.session.commit()
        # Flash a success message thanking them for signing up
        flash(f'Thank you {username}, you have successfully registered!', 'success')
        # Redirecting to the home page
        return redirect(url_for('index'))

    return render_template('register.html', title=title, form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title= 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        # Grab data from form
        username = form.username.data
        password = form.password.data

        # Query our User table for a user with username
        user = User.query.filter_by(username=username).first()

        # Check if the user is None or if password is incorrect
        if user is None or not user.check_password(password):
            flash('Your username or password is incorrect', 'danger')
            return redirect(url_for('login'))

        login_user(user)

        flash(f'Welcome {user.username}. You have successfully logged in.', 'success')
        return redirect(url_for('index'))

    return render_template('login.html', title=title, login_form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


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