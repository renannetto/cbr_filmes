import urllib2
import json

json_filename = "json"
instances_file = open("instances", "w")

def get_movie_data(title):
	html_request = "http://www.omdbapi.com/?i=&t=" + title.replace(" ", "+")
	print "Request: " + html_request
	response = urllib2.urlopen(html_request)
	json_text = response.read()

	json_file = open(json_filename, "w")
	json_file.write(json_text)
	json_file.close()

	json_file = open(json_filename, "r")
	movie_data = json.load(json_file) 
	json_file.close()

	title = movie_data["Title"]
	year = movie_data["Year"]
	language = movie_data["Language"]
	language = language.replace(", ", ";") + ";"
	rating = movie_data["imdbRating"]
	genre = movie_data["Genre"]
	genre = genre.replace(", ", ";") + ";"

	instances_file.write('\t<instance id="' + title + '" >\n')
	instances_file.write('\t\t<att name="Titulo" value="' + title + '" />\n')	
	instances_file.write('\t\t<att name="Ano" value="' + year + '" />\n')	
	instances_file.write('\t\t<att name="Idioma" value="' + language + '" />\n')	
	instances_file.write('\t\t<att name="Nota" value="' + rating + '" />\n')	
	instances_file.write('\t\t<att name="Genero" value="' + genre + '" />\n')	
	instances_file.write("\t</instance>\n")


movies_file = open("movie_list", "r")
movies = movies_file.read()
movie_list = movies.split("\n")

for movie in movie_list:
	get_movie_data(movie)

