
class Movie:

    def __init__(self,id,title,overview,poster):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster

class Trailer:

    def __init__(self,id,key):
        self.id = id
        self.key = key