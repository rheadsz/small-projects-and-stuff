
'''

Script to write movie ratings and the movies in the same file.
MovieLensDB gives different datasets for movies which are good.
But the problem here is, the movies.csv file contains movieId,name and genre,
but not the movie rating. The ratings are kept in a separate file (ratings.csv).

'''

import csv

def open_moviesDB():
    movie_list = []
    with open("movies.csv","r") as movies:
        movielist = csv.reader(movies)
        for m in movielist:
            movie_list.append(m)
    return movie_list

def open_ratingsDB():
    rating_list = []
    with open("ratings.csv","r") as ratings:
        ratinglist = csv.reader(ratings)
        for r in ratinglist:
            rating_list.append(r)
    return rating_list

def getTheMovieID(rated_list):
    # extract the movie ID from ratings.csv
    # since the ID's are not sorted
    rated_movieID = []
    for ids in rated_list:
        rated_movieID.append(ids[1])
    ids = list(set(rated_movieID))
    ids.sort()
    return ids

def WriteToFile(database,filename):
    sorted_ids_file = open("{0}.txt".format(filename),"a")
    sorted_ids_file.write("#sorted movieIds of the ratings.csv")
    for mId in database:
        sorted_ids_file.write(mId+"\n")
    sorted_ids_file.close()
    return 

rates_movieId = open_ratingsDB()
movieIds = getTheMovieID(rates_movieId)
WriteToFile(movieIds,"sorted-movieIds")


