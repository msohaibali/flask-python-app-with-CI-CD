from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
    return render_template('index.html')

@main.route('/profile')
@login_required
def get_profile():
    return render_template('profile.html', username=current_user.username)
