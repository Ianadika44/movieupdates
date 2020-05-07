from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_movies,get_movie,get_trailer,get_recommended_movies,search_movie

@main.route('/')
def index():

    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    top_movies = get_movies('top_rated')

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('.search',movie_name=search_movie))
    else:
        return render_template('index.html', popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie,top_movies=top_movies)

@main.route('/movie/<int:id>')
def movie(id):

    movie = get_movie(id)
    trailer = get_trailer(id)
    recomended_movies = get_recommended_movies(id)

    return render_template('movie.html',movie=movie,trailer=trailer,movies=recomended_movies)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',title = title,movies = searched_movies)