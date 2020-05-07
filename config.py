import os

class Config:
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = 'e699c48f914c566cf9dccd32eac5fe7c'
    TRAILERS_URL = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}&language=en-US'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}