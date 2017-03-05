

# the genre data set will contain values in the form of binary
# The list will follow the same pattern

# Action,Adventure,Animation,Biography,Comedy,Children 6
# crime,documentry,Drama, Family, Fantasy, 10
# Film-Noir, History, Horror, Music, Musical ,15
# Mystery,Romance, Sci-Fi, Sport, Thriller,20
# War, Western

import math

# euclidian distance  = sqrt(pow(x1 - y1,2) + pow(x2 - y2,2))

# samp data set : (8.8,6.4) (9.8,5.4)

def sim_dist(dataset,person1,person2):
    si = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_of_squares = sum([pow(dataset[person1][item] - dataset[person2][item],2)for item in dataset[person1] if item in dataset[person2]])
    return 1/(1+math.sqrt(sum_of_squares))


def genre_tagger(movieData = None):
    '''
        This function tags the movie with true or false as genre.
        If a movie has comedy as its genre then it tags it as 1, if its
        not comedy then it tags it 0. So, it makes a list of binary sequence by checking
        if the genre exists in the movie data.

    '''
    genre_tag = []
    # momentary movie data list
    movieData = [
                    ['152081', 'Zootopia (2016)', ['Action','Adventure','Animation','Children','Comedy']]
    ]
    # all typpes of genres
    movie_genres_list = ["Action","Adventure","Animation","Biography","Comedy","Children",\
                    "Crime","Documentry","Drama","Family", "Fantasy",\
                    "Film-Noir", "History","Horror","Music","Musical",\
                    "Mystery","Romance","Sci-Fi","Sport","Thriller",\
                    "War","Western"]
    for genre in movie_genres_list:
        if genre in movieData[0][2]:
            genre_tag.append(1)
        else:
            genre_tag.append(0)

    if genre_tag is None or  genre_tag is []:
        return None
    return genre_tag


print(genre_tagger())
