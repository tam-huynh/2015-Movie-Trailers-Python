import webbrowser

class Movie():
    def __init__(self, title, plot, poster, trailer):
        self.title = title
        self.plot = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
