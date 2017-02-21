#Brett's Favorite Movies

Generated from python scripts, "Brett's Favorite Movies" is a website that shows a few of my favorite movies. This website and scripts are part of a project within [Udacity's Full Stack Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004) program. 

##Pre-requisites

For the scripts to properly generate the intended website, [Python](https://www.python.org/downloads/) version 2.7 or greater must be installed. 

##Populating the template
In order to function properly, both *fresh_tomatoes.py* and *entertainment_center.py* must be contained within the same folder. 

###fresh_tomatoes.py
This file takes a list of movies and creates an html page that displays those movies in an attractive and orderly layout, using information provided in ```entertainment_center.py```. 

###entertainment_center.py
This file contains the information that will be used to populate the page when we run the program. 

For each instance of the object ```movie_name = media.Movie```, the code looks for four inputs, in order, separated by commas. They are:
1. "Movie Title"
2. "A description of the movie's plot"
3. "The url of the movie's poster art"
4. "The url of the movie's trailer on YouTube". 

Enter this information for each movie that you would like to appear on the website.

The list of movies ```movies = [movie_name_1, movie_name_2, ...]```  will need to be filled in to correspond with the ```movie_name```s from the instances above.  

The program command ```fresh_tomatoes.open_movies_page(movies)``` will run the code and generate an html page with the content you provided. The html file created by the program will be stored in the same folder as the two Python files. Cool! 






