import urllib.request,json
from .models import Movie,Trailer

api_key = None
base_url = None
trailers_url = None
recommended_url = None
search_url = None

def configure_request(app):
    global api_key,base_url,trailers_url,recommended_url,search_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    trailers_url = app.config['TRAILERS_URL']
    recommended_url = app.config['RECOMMENDED_MOVIES_URL']
    search_url = app.config['SEARCH_URL']

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

    trailers_results = None

    if trailers_response['results']:
        trailers_list = trailers_response['results']
        trailers_results = process_trailers(trailers_list)

    return trailers_results

def process_trailers(list_trailers):
    trailers_results =[]
    for trailer in list_trailers:
        id = trailer.get('id')
        key = trailer.get('key')

        trailer_object = Trailer(id,key)

    return trailer_object

def get_recommended_movies(id):
    get_recommended_movies_url = recommended_url.format(id,api_key)

    with urllib.request.urlopen(get_recommended_movies_url) as url:
        recommended_movies_data = url.read()
        recommended_movies_response = json.loads(recommended_movies_data)

        recommended_movies_results = None

        if recommended_movies_response['results']:
            recommended_movies_results_list = recommended_movies_response['results']
            recommended_movies_results = process_recommended_movies(recommended_movies_results_list)

    return recommended_movies_results

def process_recommended_movies(recommended_movies_list):

    recommended_movies_results = []
    for recommended_movie in recommended_movies_list:
        id = recommended_movie.get('id')
        title = recommended_movie.get('original_title')
        overview = recommended_movie.get('overview')
        poster = recommended_movie.get('poster_path')

        if poster:
            recommended_movie_object = Movie(id,title,overview,poster)
            recommended_movies_results.append(recommended_movie_object)

    return recommended_movies_results

def search_movie(movie_name):
    search_movie_url = search_url.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results