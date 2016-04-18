# This file "media.py" helps in making instances of the movies.
# the movie's instance variables are defined in "entertainment_center.py"

import webbrowser
class Movie():
	"""
		This class provides a way to store movie related information
	"""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube


	# This method is build for show_casing the trailor
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)