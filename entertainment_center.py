# includes Movie and TV classes with methods for rendering in fresh tomatoes
import media
# This append movies in a list and calls an external rendering function to make movie webpage
import fresh_tomatoes

toy_story = media.Movie(title="Toy Story",
	storyline="A story of a boy and his toys that come to life.",
	poster_image_url="http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	trailer="https://www.youtube.com/watch?v=vwyZH85NQC4",
	actors=[
		("Tom Hanks", "Woody (voice)"),
		("Tim Allen", "Buzz Lightyear (voice)"),
		("Don Rickles", "Mr. Potato Head (voice)"),
		("Jim Varney", "Slinky Dog (voice)"),
		("Wallace Shawn", "Rex (voice)"),
		("John Ratzenberger", "Hamm (voice)"),
		("Annie Potts", "Bo Peep (voice)"),
		("John Morris", "Andy (voice)"),
		("Erik von Detten", "Sid (voice)"),
		("Laurie Metcalf", "Mrs. Davis (voice)"),
		("R. Lee Ermey", "Sergeant (voice)"),
		("Sarah Freeman", "Hannah (voice)"),
		("Penn Jillette", "TV Announcer (voice)"),
		("Jack Angel", "Shark / Rocky Gibraltar (voice)"),
	],
	release_date="November 19, 1995",
	)

avatar = media.Movie(title="Avatar",
	storyline="A marine on an alien planet.",
	poster_image_url="http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	trailer="https://www.youtube.com/watch?v=5PSNL1qE6VY",
	actors=[
		("Sam Worthington", "Jake Sully"),
		("Zoe Saldana", "Neytiri (as Zoe Saldana)"),
		("Sigourney Weaver", "Dr. Grace Augustine"),
		("Stephen Lang", "Colonel Miles Quaritch"),
		("Michelle Rodriguez", "Trudy Chacon"),
		("Giovanni Ribisi", "Parker Selfridge"),
		("Joel David Moore", "Norm Spellman"),
		("CCH Pounder", "Moat"),
		("Wes Studi", "Eytukan"),
		("Dileep Rao", "Dr. Max Patel"),
		("Matt Gerald", "Corporal Lyle Wainfleet"),
		("Sean Anthony Moran", "Private Fike"),
		("Jason Whyte", "Cryo Vault Med Tech"),
		("Scott Lawrence", "Venture Star Crew Chief"),
	],
	release_date="December 18, 2009",

	)

starwars_iv = media.Movie(title="Star Wars IV: A New Hope",
	storyline="A farmboy fights to save his way of life from the evil empire.",
	poster_image_url="https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
	trailer="https://www.youtube.com/watch?v=vZ734NWnAHA",
	actors=[
		("Mark Hamill", "Luke Skywalker"),
		("Harrison Ford", "Han Solo"),
		("Carrie Fisher", "Princess Leia Organa"),
		("Peter Cushing", "Grand Moff Tarkin"),
		("Alec Guinness", "Ben Obi-Wan Kenobi"),
		("Anthony Daniels", "C-3PO"),
		("Kenny Baker", "R2-D2"),
		("Peter Mayhew", "Chewbacca"),
		("David Prowse", "Darth Vader"),
		],
	release_date="May 25, 1977",
	)

movies = [starwars_iv, toy_story, avatar]
# print media.Movie.VALID_RATINGS
# print avatar.title
# print starwars_iv.get_cast()
# print avatar.get_cast()
# print toy_story.get_cast()
fresh_tomatoes.open_movies_page(movies)
