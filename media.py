# Import webbrowser to be used when opening a link in a web browser.
import webbrowser

# Declares Movie as a class
class Movie():
# Function defines where the title, storyline, post_image_url, and traielr_youtube_url will be stored.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
# Function opens the movie trailer when called upon.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
