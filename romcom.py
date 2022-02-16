# romcom.py 2/15/22 11:13 PM
""" Provides a menu screen where user can select various IMDB movie functions"""

# Import os module for system calls to cls and clear (screen)
import os  # for system calls to clear screen
import csv  # to import TSV files for movie and actor lists
import unittest 
import re
import pandas as pd #needs install
import pickle
import json
import sqlite3
import matplotlib.pyplot as plt #needs install
import networkx as nx #needs install
from tabulate import tabulate

# Define main function to print menu and get user choice
def main():
    """ Command-line menu of functions Hallmark original movies """
    
    # Clear the screen
    clrscr()

    # Load the data structures
    load_data()

    # Implement a “master loop” console application where the user can repeatedly enter commands,
    # perform actions, including choosing to exit the program. Code Louisville requirement.

    while(True):

        # Print instructions and menu
        print('\nPlease enter a number between 1 and 6.\n')
        print_menu()

        # Get user's menu choice and verify entry data type
        option = ''
        try:
            option = int(input('\nEnter your choice (1-6) and ENTER/RETURN: '))
        except:
            print('\nNumbers only, please...')

        # Launch whichever function the user selected from the main menu
        if option == 0:  # for debug only, to be removed later
            clrscr()
            option0(option)
        elif option == 1:
            clrscr()
            option1(option)
        elif option == 2:
            clrscr()
            option2(option)
        elif option == 3:
            clrscr()
            option3(option)
        elif option == 4:
            clrscr()
            option4(option)
        elif option == 5:
            clrscr()
            option5(option)
        elif option == 6:
            #clrscr()
            print('\n\'Option 6\' selected, our work is done here.')
            print("\nDon\'t have a good day... Have a great day!\n")
            exit()
        else:
            pass

def clrscr():  # clears screen in Mac, Linux, or Windows
    # Check if Operating System is Mac and Linux or Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
          # Else Operating System is Windows (os.name = nt)
        _ = os.system('cls')
    return None

def notImplementedYet(option):  # stub for drivers and testing
    separator = '\n******************************************************\n'
    print(separator)
    print("'Option", str(option) + "' selected. Section not implemented yet.")
    print(separator)
    return None

def print_menu():  # basic menu screen for user to select program feature sets
    menu_options = {  # dictionary of menu options
        1: 'Filmography - See what movies a select person starred in',
        2: 'Cast - See who starred in a select movie',
        3: 'Costars - See any movie(s) two select people starred in',
        4: 'Leaderboard - ("Hallmark" TV RomComDram Hall of Fame)',
        5: 'About - See more about this project',
        6: 'Exit',
    }
    # Loop for main menu until user selects to exit program
    for key in menu_options.keys():
        print (str(key) + '. ', menu_options[key] )
    return None

# Define functions launched when chosen from main menu by user

def option1(option):  # filmography for a person
    option = option
    actor = input()
    nm = name_nm[actor]
    # Create and call at least 3 functions or methods, at least one of which must return a value
    # that is used somewhere else in your code. Code Louisville requirement.
    actor_name = actor_lookup(nm)
    filmography_headers = actor_name + ' Movies'
    actor_movies = nm_tt[nm]
    actor_titles = []
    for k, v in enumerate(actor_movies):
        actor_titles.append(tt_title[v])
    df = pd.DataFrame(actor_titles)
    total_titles = len(actor_titles)
    print(actor_name, ': ', total_titles, 'Hallmark movies')
    tab_print(df, '')
    return None

def actor_lookup(nm):
    name = nm_name[nm]
    return name

def option2(option):  # a movie's top actors and actresses
    option = option
    #movie_info_headers=["IMDB #","Category ","Title  ","Year","Runtime","Genres   ","Rating","Votes"]  # note: bug in tab api
    #tab_print(movie_info.head(10), movie_info_headers)  # "pretty" print result
    movie='tt13831504'
    movie_cast_codes = tt_nm[movie]  # create a list of movies from the dictionary lookup
    movie_cast_names = []
    for person in movie_cast_codes:
        movie_cast_names.append(nm_name[person])
    df = pd.DataFrame(movie_cast_names)
    total_actors = len(movie_cast_names)
    print(tt_title[movie], 'had', total_actors, 'main actors and actresses in it:')
    #cast_headers = ""
    tab_print(df, '')
    return None

def option3(option):  # movies where two specific people acted in
    option = option
    actor1 = 'Lacey Chabert'
    actor2 = 'Luke Macfarlane'
    separation = (sp[actor1][actor2])
    df = pd.DataFrame(separation)
    distance = int(len(separation)/2)
    header_string = (str(distance) + " Degrees Separation - " + str(actor1) + " and " + str(actor2))
    separation_headers = [header_string]
    tab_print(df, separation_headers)
    return None

def option4(option):  # leaderboard
    option = option
    leader_board_headers=['"Hall of Fame"', "Fame-O-Meter\u2081"]
    tab_print(leader_board[:10], leader_board_headers)
    print('\nNote 1. Calculated using graph analysis and centrality.')
    return None

def option5(option):  # about section
    option = option
    about_header = 'SIX DEGREES OF LACEY CHABERT\n' + '--------------------------------------------------------------------------------'
    about = ['This initiative includes a GitHub repository, which includes more information',
            'as well as a Wiki page and Kanban project schedule.',
            '\nLacey Chabert is widely regarded as the "queen" of Hallmark movies, having', 
            'starred in over 30 Hallmark original romantic comedies, dramas, and mysteries.', 
            'Six Degrees of Kevin Bacon is a meme that cast him as "center of the universe"',
            'in Hollywood. Based on how many movies he\'s starred and costarred in with top',
            'actors and actresses in Hollywood, analysts joked that nobody in Hollywood was',
            'more than six degrees of separation from Kevin. And they backed it up with',
            'research and analyis. Other studies have proven several people are more likely',
            'candidates as the center of the Hollywood metaverse.',
            '\nThis neophyte Python program performs similar analysis on Lacey Chabert within',
            'Hallmark movies. This initiative is associated with a Code Louisville bootcamp',
            'on Python programming and data analysis. It uses a public dataset provided by',
            'IMDB, and provides a command-line program that provides the capability to query',
            'the database to learn more about an actor or actress or the movies they\'ve',
            'costarred in. Any external analysis from Jupyter Notebook will also be displayed.']
    print(about_header)
    for lines in about:
        print(lines)
    return None

def option6(option):  # exit the program
    option = option
    notImplementedYet(option)  # driver, eventually replaced by feature

def option0(option):  # for debug only, to be replaced later with 'easter egg'
    option = option  # space holder
    notImplementedYet()
    return None

def load_data():  # read data from tab-delimited files to data structures
    global tt_title, title_tt, tt_nm, nm_name, name_nm, nm_tt
    global cast_crew_info, movie_info, movie_cast_crew, leader_board, sp 
    # Read data from an external file, such as text, JSON, CSV, etc, and use that data in your
    # application. Code Louisville requirement.
    print('Loading data, please wait (15-20 seconds)...')
    movie_info = pd.read_csv('movie_info.csv', sep='\t', index_col=None, \
                  dtype={'startYear': str, 'runtimeMinutes': str}, \
                  converters={'movieGenres': lambda x: re.split(',+', x)})  
    df = movie_info
    tt_title = dict(zip(df.tconst, df.primaryTitle))  # match title by movie ID
    title_tt = dict(zip(df.primaryTitle, df.tconst))  # match ID by movie title

    cast_crew_info = pd.read_csv('cast_crew_info.csv', sep='\t', index_col=None)
    df = cast_crew_info 
    nm_name = dict(zip(df.nconst, df.primaryName))  # lookup name by cast ID
    name_nm = dict(zip(df.primaryName, df.nconst))  # lookup ID by cast name

    movie_cast_crew = pd.read_csv('movie_cast_crew.csv', sep='\t', \
      index_col=None)
    df = movie_cast_crew.groupby('nconst')['tconst'].apply(list).reset_index(name="movieList")
    nm_tt = dict(zip(df.nconst, df.movieList))  # lookup movie IDs by actor ID
    df = movie_cast_crew.groupby('tconst')['nconst'].apply(list).reset_index(name="actorList")
    tt_nm = dict(zip(df.tconst, df.actorList))  # lookup actor IDs by movie ID 

    leader_board = pd.read_csv('leader_board.csv', sep='\t', index_col=None)
    sp = pickle.load(open("shortest_path.pkl", "rb"))  # shortest path data, pickle 1/4 size of json
    return None

def tab_print(df, header_name):  # "pretty" print for a dataframe slice
    print(tabulate(df, headers=header_name, showindex=False, numalign='center'))
    return None

# Allow file to be used as function or program
if __name__=='__main__':
    main()