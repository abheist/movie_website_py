# This file contains the instances of the movies and creating them as much as one want

# Importing media and fresh_tomatoes file
import media
import fresh_tomatoes



# Making the instance of toy_story movie
toy_story = media.Movie("Toy Story",
						"A story of a boy and his toy came to life",
						"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", # noqa
						"https://www.youtube.com/watch?v=Bj4gS1JQzjk")

# print (toy_story.storyline)

# Making the instance of avatar movie
avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", #noqa
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# print avatar.storyline
# avatar.show_trailer()


#Make the list of all instance variable to pass to fresh_tomatoes class and generate .html page of these movies.
movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)