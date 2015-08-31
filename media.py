# for loading a webpage
import webbrowser

class Video():
	"""Video related class to inherit from"""
	def __init__(self, **kwargs):
		self.title = kwargs.get("title", "")
		self.duration = kwargs.get("duration", "")
		self.imdb_link = kwargs.get("imdb_link", "")
		self.actors = kwargs.get("actors", [])

	# returns cast as a list of actors and their roles
	def get_cast(self):
		htmlList = '<ul id="displayCast">'
		for (actor,role) in self.actors:
			htmlList += '<li>' + actor + ' as <strong>' + role + '</strong></li>'
		return htmlList + '</ul>'

class Movie(Video):
	"""This class provides way to store information for movies"""
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, **kwargs):
		Video.__init__(self, **kwargs)
		self.storyline = kwargs.get("storyline", "")
		self.poster_image_url = kwargs.get("poster_image_url", "")
		self.trailer_youtube_url = kwargs.get("trailer", "")
		self.release_date = kwargs.get("release_date", "")

	# show movie trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def set_actors(self, actors):
		# two tests to make sure cast is set correctly
		assert len(actors) > 0, "actors must be an array"
		assert len(actors[1]) > 1, "actors must be in tuple"
		self.actors = actors or []