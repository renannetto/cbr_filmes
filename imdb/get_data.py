import urllib2
import json

json_filename = "json"

def get_movie_data(title):
	html_request = "http://www.omdbapi.com/?i=&t=" + title
	response = urllib2.urlopen(html_request)
	json_text = response.read()

	json_file = open(json_filename, "w")
	json_file.write(json_text)
	json_file.close()

	json_file = open(json_filename, "r")
	movie_data = json.load(json_file) 
	json_file.close()

	print "Title: " + movie_data["Title"]
	print "Genre: " + movie_data["Genre"]
	print "Year: " + movie_data["Year"]
	print "Language: " + movie_data["Language"]
	print "Rating: " + movie_data["imdbRating"]

get_movie_data("Frozen")
