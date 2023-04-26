class Movie:
    def __init__(self, name, genre=None):
        self.name = name
        if genre != None:
            self.genre = genre

    def set_genre(self, genre):
        self.genre = genre

    def get_name(self):
        return self.name

    def __str__(self):
        return "{}".format(self.get_name())

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented

        return self.get_name() == other.get_name()


class Movie_Store:
    def __init__(self):
        self.movie_list = []

    def add_movie(self, movie):
        # for m in self.movie_list:
        #     if movie == m:
        #         print("Movie already exists")
        #         return
        # self.movie_list.append(movie)

        # if movie in self.movie_list:
        #     print("Movie already exists")
        # else:
        #     self.movie_list.append(movie)

        self.movie_list.append(movie)

    def remove(self, title):
        for movie in self.movie_list:
            if movie.get_name() == title:
                self.movie_list.remove(movie)




m1 = Movie("Star Wars")
m2 = Movie("Star Wars")
print(m1 == m2)

ms1 = Movie_Store()
ms1.add_movie(m1)
ms1.add_movie(m2)
ms1.remove("Star Wars")
print(ms1.movie_list)
