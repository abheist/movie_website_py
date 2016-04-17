import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toy came to life",
						"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
						"https://www.youtube.com/watch?v=Bj4gS1JQzjk")

# print (toy_story.storyline)


avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# print avatar.storyline
# avatar.show_trailer()

movies = [toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)