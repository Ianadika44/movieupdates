from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_movies,get_movie,get_trailer

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    top_movies = get_movies('top_rated')

    return render_template('index.html', popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie,top_movies=top_movies)

@main.route('/movie/<int:id>')
def movie(id):

    movie = get_movie(id)
    trailer = get_trailer(id)

    return render_template('movie.html',movie=movie,trailer=trailer)