# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# -----------------------------------------------------------------------------

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network information
# and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
#
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Note that each sentence will be separated from the next by only a period. There will
# not be whitespace or new lines between sentences.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below.
#
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using print statements and the
# Test Run button.
# -----------------------------------------------------------------------------

# Example string input. Use it to test your code.
example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# -----------------------------------------------------------------------------
# create_data_structure(string_input):
# Parses a block of text (such as the one above) and stores relevant
# information into a data structure. You are free to choose and design any
# data structure you would like to use to manage the information.
#
# Arguments:
# string_input: block of text containing the network information
#
# You may assume that for all the test cases we will use, you will be given the
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not
#   list B's connections or liked games.
#
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
#
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    network = {}
    for e in string_input.split('.'):
        if e != '':
            name = e.split()[0]
            if name not in network:
                network[name] = [[], []]
        if 'is connected to' in e:
            network[e.split()[0]][0] = e[e.find('is connected to') + 16:].split(', ')
        if 'likes to play' in e:
            network[e.split()[0]][1] = e[e.find('likes to play') + 14:].split(', ')
    return network


# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user in network:
        return network[user][0]


# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network, user):
    if user in network:
        return network[user][1]


# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    if user_B not in network[user_A][0]:
        network[user_A][0].append(user_B)
    return network


# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network[user] = [[], games]
    return network


# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
#
# NOTE:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    secondary = None
    if user in network:
        secondary = []
        for first in network[user][0]:
            for second in network[first][0]:
                if second not in secondary:
                    secondary.append(second)
    return secondary


# -----------------------------------------------------------------------------
# connections_in_common(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    n = 0
    for connection in network[user_A][0]:
        if connection in network[user_B][0]:
            n += 1
    return n


# -----------------------------------------------------------------------------
# path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# NOTE:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.
def path_to_friend(network, user_A, user_B, visited=None):
    # your RECURSIVE solution here!
    if visited is None:
        visited = []

    if user_A in network and user_B in network:
        visited.append(user_A)
        if user_B in network[user_A][0]:
            return [user_A, user_B]
        for e in network[user_A][0]:
            if e not in visited:
                path_left = path_to_friend(network, e, user_B, visited)
                if path_left:
                    return [user_A] + path_left


# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------
# Your MYOP should either perform some manipulation of your network data
# structure (like add_new_user) or it should perform some valuable analysis of
# your network (like path_to_friend). Don't forget to comment your MYOP. You
# may give this procedure any name you want.

# -----------------------------------------------------------------------------
# compute_user_popularity(network):
#   Roughly computes popularity of each user in gamer network based on two main
#   factors:
#       1)  The number of users that are connected to him/her is positively
#           correlated to his/her popularity.
#       2)  The popularity of the users who are connected to him/her is positively
#           correlated to his/her popularity.
#
# Arguments:
#   network: the gamer network data structure.
#
# Return:
#   A dictionary showing popularity of each user in the gamer network.
def compute_user_popularity(network):
    #no damping factor needed
    nloops = 10
    popularity = {}
    nusers = len(network)
    for user in network:
        popularity[user] = 1.0 / nusers
    for i in range(0, nloops):
        new_popularity = {}
        for user in network:
            popu = 0
            for user2 in network:
                if user in network[user2][0]:
                    popu += popularity[user2] / len(network[user2][0])
            new_popularity[user] = popu
        popularity = new_popularity
    return popularity


# -----------------------------------------------------------------------------
# find_most_popular_user(network):
#   Finds the most popular user of the given gamer network.
#
# Arguments:
#   network: the gamer network data structure.
#
# Return:
#   The name of the most popular user.
#   -   If two or more users are equally popular and are the most popular ones,
#       return all their names separated by comma and space.
def find_most_popular_user(network):
    popularity = compute_user_popularity(network)
    most = -1
    puser = None
    for user in popularity:
        if popularity[user] == most:
            puser = puser + ', ' + user
        if popularity[user] > most:
            most = popularity[user]
            puser = user
    return puser


# -----------------------------------------------------------------------------
# games_in_common(network, user_A, user_B):
#   Finds the games that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The games in common (as a string, games are separated by comma and space).
#   - If user_A or user_B is not in network, return False.
#   - If user_A or user_B do not have games in common, return None.
def games_in_common(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    games = None
    for g in network[user_A][1]:
        if g in network[user_B][1]:
            if games:
                games = games + ', ' + g
            else:
                games = g
    return games


# -----------------------------------------------------------------------------
# add_new_game(network, user, game):
#   Adds new game to an existed user profile.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a string containing the user's NEW favorite game, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with new games added in a user's profile.
#   -   Print a string "Added successfully!"
#   -   If the user does not exist in network, print a string "You do not have a
#       profile. Please create one first!" and return network unchanged.
#   -   If the game already exists in user's profile, print a string "The game ***
#       already existed in your profile."
def add_new_game(network, user, game):
    if user not in network:
        print 'You do not have a profile. Please create one first!'
    else:
        if game in network[user][1]:
            print 'The game ' + game + ' already existed in your profile!'
        else:
            network[user][1].append(game)
            print 'Added successfully!'
    return network


# -----------------------------------------------------------------------------
# find_gamers(network, game):
#   Finds all the users who play the given game.
#
# Arguments:
#   network: the gamer network data structure
#   game:  a string containing the name of a game
#
# Return:
#   A list of users who play the game.
#   If no user play the game, return empty list.
def find_gamers(network, game):
    gamers = []
    for user in network:
        if game in network[user][1]:
            gamers.append(user)
    return gamers


# -----------------------------------------------------------------------------
# sort_games(network):
#   Sorts all the games played by the users in the network based on the number
#   of users who play each game.
#
# Arguments:
#   network: the gamer network data structure
#
# Return:
#   A sorted list of lists which contain the name of each game and the number
#   of users who play the game.
#   - The game with most number of users should be placed first.
def sort_games(network):
    games = {}
    for user in network:
        for game in network[user][1]:
            if game not in games:
                games[game] = 1
            else:
                games[game] += 1
    s = sorted(games, key=games.__getitem__, reverse=True)
    chart = []
    for e in s:
        chart.append([e, games[e]])
    return chart


#net = create_data_structure(example_input)
#print net
#print path_to_friend(net, "John", "Ollie")
#print path_to_friend({'a': [['b'], []], 'b': [['a', 'd'], []], 'c': [[], []], 'd': [['c'], []]}, 'a', 'c')
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", [])
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print get_connections(net, 'John')
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")
#print compute_user_popularity(net)
#print find_most_popular_user(net)
#print find_most_popular_user({'a':[[],[]], 'b':[[],[]]})
#print games_in_common(net, 'John', 'Ollie')
#print games_in_common(net, 'Walter', 'Freda')
#print find_gamers(net, 'The Movie: The Game')
#print find_gamers(net, 'Lord of Rings')
#print sort_games(net)
#print create_data_structure('')
#print add_new_game(net, 'John', 'Lord of Rings')
#print add_new_game(net, 'Lisa', 'Ninja Hamsters')
#print add_new_game(net, 'Freda', 'Ninja Hamsters')