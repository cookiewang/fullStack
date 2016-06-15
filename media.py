import webbrowser


class Movie():
        """this is a constructor which takes the movie info as the parameters"""    # noqa
        def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):   # noqa
            self.title = title
            self.storyline = storyline
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url

        def show_trailer(self):
            """ this function displays the movie trailer web page """
            webbrowser.open(self.trailer_youtube_url)
