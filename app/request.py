import urllib.request,json
from .models import Movie

api_key = None
base_url = None
trailers_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    trailers_url = app.config['TRAILERS_URL']

def get_movies(category):

    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

        return movie_results

def process_results(movie_list):

    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')

        if poster:
            movie_object = Movie(id,title,overview,poster)
            movie_results.append(movie_object)

    return movie_results

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')

            movie_object = Movie(id,title,overview,poster)

    return movie_object

def get_trailer(id):
    get_trailers_url = trailers_url.format(id,api_key)

    with urllib.request.urlopen(get_trailers_url) as url:
        trailers_data = url.read()
        trailers_response = json.loads(trailers_data)

    trailers_object = None

    if trailers_response['results']:
        id = trailers_response.get('id')
        key = trailers_response.get('key')

        trailers_object = (id,key)