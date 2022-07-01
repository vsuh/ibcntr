from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('root.tpl')

@main.route('/profile')
@login_required
def profile():
    redirect_url = url_for("bats.index")
    return render_template('profile.tpl', name=current_user.name, redirect_url=redirect_url)
