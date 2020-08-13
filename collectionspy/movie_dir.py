import pandas as pd
import csv
from collections import defaultdict, namedtuple, deque
import statistics
from operator import attrgetter

Movie = namedtuple('Movie', 'title year score')
Director = namedtuple('Director', 'name average movies')
class DirectorRating:
    def __init__(self, path='https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv', 
                num_top_directors=20, min_movies=4, min_year=1960):
        self.MOVIE_DATA = pd.read_csv(path)
        self.NUM_TOP_DIRECTORS = num_top_directors
        self.MIN_MOVIES = min_movies
        self.MIN_YEAR = min_year
    def get_movies_by_director(self):
        '''Extracts all movies from csv and stores them in a dictionary
        where keys are directors, and values is a list of movies (named tuples)'''
        directors_dic = defaultdict(list)
        for index, row in self.MOVIE_DATA.iterrows():
            directors_dic[row.director_name].append((Movie(title=row.movie_title.strip(), year=row.title_year, score=row.imdb_score)))
        return directors_dic

    def get_average_scores(self, directors):
        '''Filter directors with < MIN_MOVIES and calculate averge score'''
        directors_to_remove = []
        for key, values in directors.items():
            valid_by_year = [m for m in values if m.year >= 1960]
            if len(valid_by_year) < self.MIN_MOVIES:
                directors_to_remove.append(key)
            directors[key] = valid_by_year
        # remove directors with less then four or old movies    
        for dir_ in directors_to_remove:
            directors.pop(dir_, None)
        return directors

    def _calc_mean(self, movies):
        '''Helper method to calculate mean of list of Movie namedtuples'''
        ratings = [score for title, year, score in movies]
        return statistics.mean(ratings)


    def filter_directors(self, directors):
        '''Filter and sort directors ordered by highest average rating. For each director
        print his/her movies also ordered by highest rated movie.'''
        filtered_directors = list()
        for d in directors.keys():
            average = self._calc_mean(directors[d])    
            filtered_directors.append(Director(name=d, average=average, movies=sorted(directors[d], key=attrgetter('score'), reverse=True)))
        filtered_directors = sorted(filtered_directors, key=attrgetter('average'), reverse=True)[:self.NUM_TOP_DIRECTORS + 1]
        return filtered_directors

    def print_results(self, directors):
        counter = 1
        for director, avg, movies in directors:
            fmt_director_entry = f'{counter}. {director:<52} {avg}'
            sep_line = '-' * 60
            print(fmt_director_entry)
            print(sep_line)

            for year, title, score in movies:
                fmt_movie_entry = f'{year} {title:<50} {score}'
                print(fmt_movie_entry)
            counter += 1
            print()


    def show(self):
        '''This is a template, feel free to structure your code differently.
        We wrote some tests based on our solution: test_directors.py'''
        aggregated_directors = self.get_movies_by_director()
        average_scored_directors = self.get_average_scores(aggregated_directors)
        filtered_directors = self.filter_directors(average_scored_directors)
        self.print_results(filtered_directors)

if __name__ == '__main__':
    director_rating = DirectorRating()
    director_rating.show()