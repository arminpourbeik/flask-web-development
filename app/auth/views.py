from flask import render_template, redirect, url_for, request, flash

from flask_login import login_user, login_required, logout_user

from .. import db
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models.user import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user=user, remember=form.remember_me.data)
            next_ = request.args.get('next')
            if next_ is None or not next_.startswith('/'):
                next_ = url_for('main.index')
            return redirect(next_)
        flash('Invalid username or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

