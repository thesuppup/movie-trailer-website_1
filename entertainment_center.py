
# Imports the media.py file which includes the Movie Class. Also imports fresh_tomatoes, which generates the webpage.
import fresh_tomatoes
import media

# Each movie is put into an object of the Class Movie, with arguments such as Movie Title, Storyline, Posterboard, and Youtube link to the movie trailer.

# Toy Story 3
toy_story = media.Movie("Toy Story",
                        "Going on a trip with toys.",
                        "http://img2.wikia.nocookie.net/__cb20140317213412/disney/images/1/14/Toy-Story-3-Movie-Poster.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

# Avatar
avatar = media.Movie("Avatar",
                     "Marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Divergent
divergent = media.Movie("Divergent",
                        "Divergent from the factions",
                        "http://www.impawards.com/2014/posters/divergent_ver11_xxlg.jpg",
                        "https://www.youtube.com/watch?v=sutgWjz10sM")

# Puts the objects into an array which is stored in movies.
movies = [toy_story, avatar, divergent]

# Calls upon the open_movies_page function in fresh_tomatoes.py, giving it the list of movies as an argument, and therefore generating the website.
fresh_tomatoes.open_movies_page(movies)
