from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')  # Changed from page1.html to index.html

@main.route('/page2')
def page2():
    return render_template('page2.html')  # This one is correct

@main.route('/page3')
def page3():
    return render_template('page3.html')  # This one is correct