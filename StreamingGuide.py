# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 3/2/2022
#
# As with all classes you define in this
# course, all data members must be private, meaning that their names begin with a single leading underscore and that
# they are not accessed directly from outside of the class (methods belonging to the class are free to access its
# private data members directly).
#
# First, write a class named Movie that has four data members: title, genre, director, and year. It should have:
#
# an init method that takes as arguments the title, genre, director, and year (in that order) and assigns them to the
# data members. The year is an integer and the others are strings. get methods for each of the data members (
# get_title, get_genre, get_director, and get_year). Next write a class named StreamingService that has two data
# members: name and catalog. the catalog is a dictionary of Movies, with the titles as the keys and the Movie objects
# as the corresponding values (you can assume there aren't any Movies with the same title). The StreamingService
# class should have:
#
# an init method that takes the name as an argument, and assigns it to the name data member. The catalog data member
# should be initialized to an empty dictionary. get methods for each of the data members (get_name and get_catalog).
# a method named add_movie that takes a Movie object as an argument and adds it to the catalog. a method named
# delete_movie that takes a movie title as an argument and if that Movie is in the catalog, removes it. Lastly,
# write a class named StreamingGuide that has one data member, a list of StreamingServices. It should have:
#
# an init method that takes no arguments and initializes the data member to an empty list. a method called
# add_streaming_service that takes a StreamingService object as an argument and adds it to the list. a method named
# delete_streaming_service that takes the name of a streaming service as an argument and if it's in the list,
# removes it. a method named where_to_watch that takes a movie title as an argument and returns a list. Element 0 of
# the list is a string that is the concatenation of the name and year of the movie (with the year in parentheses),
# with the rest of the list being the names of streaming services showing that movie. For example, the list that is
# returned might look like this: ['King Kong (1933)', 'HBO Max', 'epix', 'Kanopy']. If the movie is not available on
# any of the StreamingServices, the method should return None. So a StreamingGuide will have a list of
# StreamingServices, and a Streaming Service will have a dictionary of Movies. The where_to_watch method needs to use
# this nested information to determine which StreamingServices, if any, have the desired movie available.

class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        return self._title

    def get_genre(self):
        return self.genre

    def get_director(self):
        return self.director

    def get_year(self):
        return self.year


class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_movie(self, movie_object):
        movie_object.get_title()

    def delete_movie(self, movie_title):
        self._catalog.pop(movie_title)


class StreamingGuide:
    def __init__(self):
        self.streaming_service = []

    def add_streaming_service(self, streaming_service_object):
        self.add_streaming_service(streaming_service_object)

    def delete_streaming_service(self, streaming_service):
        self.delete_streaming_service(streaming_service)

    def where_to_watch(self, movie_title):
        return [self.get_title, self.get_year, self.get_name, self.get_genre]


# testing
movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical document', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch('Little Women')
