import webbrowser

class Movie():
    '''This class provides a way to store movie related information'''
    def __init__(self, title, plot, poster, trailer):
        '''Initialization'''
        self.title = title
        self.plot = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
    def showTrailer(self):
        '''This method opens a youtube trailer via a webbrowser'''
        webbrowser.open(self.trailer_youtube_url)
