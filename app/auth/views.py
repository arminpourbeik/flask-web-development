from flask import render_template, redirect, url_for, request, flash

from flask_login import login_user, login_required, logout_user

from . import auth
from .forms import LoginForm
from ..models.user import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user=user, remember=form.remember_me.data)
            next_ = request.args.get('next')
            if next_ is not None or not next_.startswith('/'):
                next_ = url_for('main.index')
            return redirect(next_)
        flash('Invalid username or password.')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout_user():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
