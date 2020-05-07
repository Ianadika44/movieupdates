class Movie:

    def __init__(self,id,title,overview,poster,genre):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.genre = genre