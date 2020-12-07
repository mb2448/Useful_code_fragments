"""
Searches for egregious repeated words.
Note: sometimes it is good to repeat words.
Edit the parameters for search in the program itself
Usage: python repeated_words.py (myfile.tex)
"""
import sys
from collections import Counter
from difflib import get_close_matches

#common words to ignore
ignore = "the\
|of|and|to|a|in|that|is|was|he|for|it\
|with|as|his|on|be|at|by|I|this|had\
|not|are|but|from|or|have|an|they\
|which|one|you|were|all|her|she|there\
|would|their|we|him|been|has|when|who\
|will|no|more|if|out|so|up|said|what\
|its|about|than|into|them|can|only\
|other|time|new|some|could|these\
|two|may|first|then|do|any|like\
|my|now|over|such|our|man|me|even\
|most|made|after|also|did|many|off\
|before|must|well|back|through|years\
|much|where|your|way".split('|')
ignore = ignore+[x.capitalize() for x in ignore]

#minimum times a word must occur  in a paragraph
#to be flagged as potentially "problematic"
minimum_occurrence = 3 
#minimum characters in a word to be considered 
#potentially "problematic"
min_length = 7

def flatten_list(l):
    flat_list = [] 
    for sublist in l: 
        for item in sublist: 
            flat_list.append(item)
    return flat_list

def get_bad_duplicates(line, words_to_ignore=ignore,
                       minimum_occurrences=minimum_occurrence, 
                       min_length=min_length):
    """Finds similar words in a string \
    that occur more than 'minimum_occurrence' times
    and are longer than 'min_length'"""
    words = [w for w in line.split() if w not in words_to_ignore]
    words = [w for w in words if len(w)>min_length]
    enough_occurrences= []
    for word in words: 
        close = get_close_matches(word, words, cutoff=0.8) 
        if len(close)>=minimum_occurrence: 
           enough_occurrences.append(close) 
    flattened = flatten_list(enough_occurrences)
    duplicates = list(set(flattened))
    return duplicates

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please execute by specifying a file name as \
              python repeated_words.py (myfile.tex)")
        sys.exit(0)
    
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        possible_violations = 0
        for idx, line in enumerate(content):
            duplicate_words = get_bad_duplicates(line)
            if len(duplicate_words)>0:
                possible_violations = possible_violations+1
                for d in duplicate_words:
                    line = line.replace(d, '***'+d.upper()+'***')
                print('Line: '+str(idx+2))
                print( line)
                print('\n')
    print(str(possible_violations) + " possible violations found.")
