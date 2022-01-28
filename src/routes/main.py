from flask import Blueprint, request, render_template
from src import db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # TODO get pages with db

    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register_new_user():
    if request.method == 'POST':
       username = request.form
       

    return render_template('register.html')