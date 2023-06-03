from flask import Blueprint, abort, render_template, request, flash, redirect, url_for, current_app
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import text
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        current_app.logger.warning("User login failed")
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.show_restaurants'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        current_app.logger.debug("User email already exists")
        return redirect(url_for('auth.signup'))
    
    is_admin = False  # Default value for is_admin flag

    # Change this to your admin email
    if email == 'admin@example.com':  # Change to your desired admin email
        is_admin = True

    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'),
                    is_admin=is_admin)  # Use the updated is_admin value

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.show_restaurants'))

@auth.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('You are not authorized to access the admin portal.')
        return redirect(url_for('main.show_restaurants'))
    users = User.query.all()
    return render_template('adminUsers.html', users=users)

@auth.route('/admin/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        abort(403)  # Return a forbidden error if the current user is not an admin

    user = User.query.get(user_id)
    if user:
        if user.email == current_user.email:
            flash('You cannot delete your own account.')
        else:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully.')
    else:
        flash('User not found.')

    return redirect(url_for('auth.admin'))



# See https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login for more information
