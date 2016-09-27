import urllib
import json
from array import array
import displayMovies

def get_movie_content():
	
	data = {
				'id':{

				},
				'name':{

				},
				'youtube_url':{

				},
				'poster_url':{

				}
			}

	connection = urllib.urlopen("https://api.themoviedb.org/3/movie/popular?api_key=dc2c5f4a99f94c7e22a32a35bf23e7f7&language=en-US")
	index = 0;
	output = connection.read()
	
	output = json.loads(output)
	output = output['results']
	
	k=0

	print(len(output))
	for item in output:
		
		data['name'][k] = output[k]['original_title']
		print(data['name'][k] + " " + output[k]['original_title'])
		k=k+1

	movid_ids = array('L') #holds all the movie ids
	k=0
	
	for item in output:
		movid_ids.append(item['id'])

	for id in movid_ids:
		data['id'][k]= id
		k = k+1;
	
	connection.close()


	k=0
	for id in movid_ids:
		url = "https://api.themoviedb.org/3/movie/"+str(id)+"/videos?api_key=dc2c5f4a99f94c7e22a32a35bf23e7f7&language=en-US"
		connection = urllib.urlopen(url)
		output = connection.read()
		output = json.loads(output)
		output = output['results']
		
		if len(output) >0 :
			data['youtube_url'][k] = "https://www.youtube.com/watch?v=" +  str(output[0]['key'])
		else:
			data['youtube_url'][k] = 'NULL'
		k = k+1

		connection.close()

	k=0
	for id in movid_ids:
		url = "https://api.themoviedb.org/3/movie/"+str(id)+"/images?api_key=dc2c5f4a99f94c7e22a32a35bf23e7f7"
		connection = urllib.urlopen(url)
		output = connection.read()
		output = json.loads(output)
		output = output['posters']

		if len(output) >0 :
			data['poster_url'][k] = "http://image.tmdb.org/t/p/original/" +  str(output[0]['file_path'])
		else:
			data['poster_url'][k] = 'NULL'
		#print(data['poster_url'][k])
		k = k+1

	connection.close()

	print(data['name'])
	print(data['youtube_url'])
	displayMovies.display_movies(data)


get_movie_content()

#crm77085d9592