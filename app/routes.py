from sqlalchemy.orm import session
from app import app, db
from flask import render_template, redirect, url_for, flash, session
from flask_login import login_user ,logout_user, current_user, login_required
from app.forms import AddItem, Ranger, UserInfoForm, LoginForm
from app.models import User, Item, Cart


@app.route('/') 
def index():
    title = 'Power Programmer Home'
    # posts = Post.query.all()
    
    return render_template('index.html', title=title )


# @app.route('/cart')
# @login_required 
# def cart():
    title = 'Cart'
    
    return render_template('cart.html', title=title)


@app.route('/my_account') 
@login_required 
def my_account():     
    title = 'My Account'

    return render_template('my_account.html', title=title)


@app.route('/red_ranger')
def red_ranger():
    title = 'Red Ranger Product Page'

    return render_template('red_ranger.html', title=title)


@app.route('/blue_ranger')
def blue_ranger():
    title = 'Blue Ranger Product Page'

    return render_template('blue_ranger.html', title=title)


@app.route('/green_ranger')
def green_ranger():
    title = 'Green Ranger Product Page'

    return render_template('green_ranger.html', title=title)    

@app.route('/pink_ranger')
def pink_ranger():
    title = 'Pink Ranger Product Page'

    return render_template('pink_ranger.html', title=title)
    

@app.route('/black_ranger')
def black_ranger():
    title = 'Black Ranger Product Page'

    return render_template('black_ranger.html', title=title)


@app.route('/yellow_ranger')
def yellow_ranger():
    title = 'Yellow Ranger Product Page'

    return render_template('yellow_ranger.html', title=title)    

@app.route('/power_rangers')
def power_rangers():
    title = 'Power Rangers Product Page'

    return render_template('power_rangers.html', title=title)
    

@app.route('/rita_repulsa')
def rita_repulsa():
    title = 'Rita Repulsa Product Page'

    return render_template('rita_repulsa.html', title=title)



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




@app.route('/addranger', methods=['GET', 'POST'])
@login_required
def addranger():
    ranger = Ranger()
    if ranger.validate_on_submit():
        color = ranger.color.data
        skill = ranger.skill.data
        description = ranger.description.data
        image = ranger.image.data
        price = ranger.price.data

        new_ranger = Item(color, skill, description, image, price)
        db.session.add(new_ranger)
        db.session.commit()

        flash('New Ranger Added')
        return redirect(url_for('index'))
    return render_template('add_ranger.html', form=ranger)


@app.route('/rangers')
def rangers():
    rangers = Item.query.all()
    return render_template('a_rangers_display.html', rangers=rangers)

@app.route('/ranger/<int:item_id>')
def ranger_detail(item_id):
    ranger = Item.query.get_or_404(item_id)

    form = AddItem()

    return render_template('a_ranger.html', ranger=ranger)


def cart():
    items = []
    total_hours = 0
    grand_total = 0
    index = 0

    for item in session['cart']:
        item = Item.query.filter_by(id=item['id']).first()

        hours = int(item['hours'])
        total = hours * item.price
        grand_total += total

        total_hours += hours

        items.append({'id': item.id, 'color': item.color, 'skill': item.skill, 'description': item.description, 'image': item.image, 'price': item.price, 'hours': hours, 'total': total, 'index': index })
        index += 1
    
    return items, grand_total, total_hours

   
@app.route('/additem', methods=['POST'])
@login_required
def add_item():

    if 'cart' not in session:
        session['cart'] = []

    form = AddItem()

    if form.validate_on_submit():
        
        session['cart'].append({'id': form.id.data, 'hours': form.hours.data})
        
    return redirect(url_for('index'))

    
@app.route('/cart')
@login_required
def cart():
    items, grand_total, total_hours = cart()   #tty query
    return render_template('cart.html', items=items, grand_total=grand_total, total_hours=total_hours)

@app.route('/remove-from-cart/<index>')
def remove_from_cart(index):

    del session['cart'][int(index)]

    return redirect(url_for('cart'))