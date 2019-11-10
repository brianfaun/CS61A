"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    newlist = [x for x in paragraphs if select(x)]
    if k >= len(newlist):
        return ''
    else:
        return newlist[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def searcher(str):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        for x in str:
            if x in punctuations:
                str = str.replace(x, "")
        str = str.lower()
        newlist = str.split(" ")

        for x in topic:
            for elem in newlist:
                if x == elem:
                    return True
        return False
    return searcher
    # END PROBLEM 2

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    """
    typed_list = typed.split(" ")
    reference_list = reference.split(" ")
    i, correct = 0, 0
    while i < len(typed_list):
        if typed_list[i] == reference_list[i]:
            correct += 1
        i += 1
    return correct / len()
    """
    total = 0
    typed_words = split(typed)
    reference_words = split(reference)

    if len(typed_words) == 0:
        return 0.0
    for i in range(0, len(typed_words)):
        if len(reference_words) <= i:
            break
        if typed_words[i] == reference_words[i]:
            total += 1
    return total / len(typed_words) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed) / 5) / (elapsed / 60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    lowest_diff, closest = limit + 1, valid_words[0]
    for elem in valid_words:
        if elem == user_word:
            return elem
        else:
            if diff_function(user_word, elem, limit) < lowest_diff:
                lowest_diff, closest = diff_function(user_word, elem, limit), elem
    if lowest_diff > limit:
        return user_word
    return closest
    # END PROBLEM 5

def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if limit < 0:
        return limit + 1
    elif len(start) > len(goal):
        return swap_diff(start[:len(start)-1] , goal, limit-1) + 1
    elif len(goal) > len(start):
        return swap_diff(start, goal[:len(goal)-1], limit-1) + 1
    elif len(start) == 0 or len(goal) == 0:
        return 0
    elif start[0] != goal[0]:
        return swap_diff(start[1:], goal[1:], limit-1) + 1
    else:
        return swap_diff(start[1:], goal[1:], limit)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    #BEGIN PROBLEM 7
    """
    if limit < -2:                                           #LIMIT
        return 100000000
    elif len(start) == 0:                                   # Length Check
        return len(goal)
    elif len(goal) == 0:
        return len(start)
    elif start in goal:
        return len(goal) - len(start)
    elif start[0] != goal[0]:                               # Don't Match
        if len(start) == 1 and len(goal) == 1:              # Length = 1
            return 1
        elif len(start) == 1 and len(goal) > len(start):
            #print ("am i ever called )
            return len(goal)
        elif len(goal) == 1 and len(start) > len(goal):
            #print ("am i ever called iether?")
            return len(start) - len(goal)
        elif start[0] == goal[1]:                           #ADD
            return edit_diff(start, goal[1:], limit-1) + 1
        elif start[1] == goal[0]:                           #DELETE
            return edit_diff(start[1:], goal, limit-1) + 1
        else:                                               #SUBSTITUTE
            return edit_diff(start[1:], goal[1:], limit-1) + 1
    else:                                                   #MATCHES
        return edit_diff(start[1:], goal[1:], limit-1)
    """

    if start == "" :
        return len(goal)
    elif goal == "":
        return len(start)
    elif limit < 0:
        return 100000000
    elif start[0] == goal[0]:
        return edit_diff(start[1:], goal[1:], limit)
    else:
        sub_counter = True
        if start[0] == goal[0]:
            sub_counter = False
        add_diff = edit_diff(start, goal[1:], limit-1) + 1
        remove_diff = edit_diff(start[1:], goal, limit-1) + 1
        substitute_diff = edit_diff(start[1:], goal[1:], limit-1) + sub_counter
        return min(add_diff, remove_diff, substitute_diff)

    #END PROBLEM 7

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    correct, i = 0, 0
    while i < len(typed):
        if typed[i] == prompt[i]:
            correct += 1
        else:
            break
        i += 1
    ratio = correct / len(prompt)
    send({'id': id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    final_list = []                             #Creates empty list inside final_list per player
    for _ in range(n_players):
        final_list.append([])

    for words in range(1, n_words+1):                #  for x amount of WORDS
        fastest_time, fastest_player = elapsed_time(word_times[0][words]) - elapsed_time(word_times[0][words-1]), [0]
        for players in range(1, n_players):       #  for x amount of PLAYERS
            time_diff = elapsed_time(word_times[players][words]) - elapsed_time(word_times[players][words-1])
            if time_diff <= fastest_time + margin:
                if time_diff <= fastest_time - margin:
                    fastest_player = []
                fastest_player.append(players)
            if time_diff < fastest_time:
                fastest_time = time_diff
        for element in fastest_player:
            final_list[element].append(word(word_times[element][words]))
    return final_list
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = True  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
