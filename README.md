# Movie Trailer List 
This project uses python files to create a list of movies with information about each movie. Clicking the image will show a movie and clicking "show cast" wil show a list of all actors and their roles below the movie tile.

To run this file open "entertainment_center.py" with python IDE and click run. Or type in the command line "python entertainment_center.py" to create the the movie webpage. Each time entertainment_center runs, it will generate a new file "fresh_tomatoes.html" and open it in your default browser.

To add more movies, edit the entertainment_center.py file and create a new media.Movie instance and add it to the list at the bottom of the code titled "movies". Example: batman = media.Movie(title="Batman" ... )
...
movies += [batman]

The Movie class in media takes parameters including "title","storyline","actors" (a list of actors in tuple (actor, role) format), "trailer"(url for the youtube trailer) , "poster_image_url" (url for the main poster image),"release_date" (date movie was released).

Note:
This file was compiled using python classes in media.py and python entertainment center to create movies with certain attributes including cast, release date, youtube trailer, title and other information.

Possible Updates:
Add more movies, have it dynamically pull more content information from IMBD.