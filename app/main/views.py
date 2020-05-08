from flask import render_template,request,redirect,url_for, abort

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Movie of the day'
    return render_template('index.html' , title = title)