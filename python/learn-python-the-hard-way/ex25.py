def sentence_split(sentence):
    """ split sentence """
    words = sentence.split()
    return words

def words_sort(words):
    """ sorted the words """
    return sorted(words)

def words_first(words):
    """ pop the first word and return """
    word = words.pop(0)
    print word

def words_last(words):
    """ pop the last word and return """
    word = words.pop(-1)
    print word

def sentence_split_sort(sentence):
    """ split the sentence and return the sorted """
    words = sentence.split()
    return words_sort(words)

def print_first_and_last(sentence):
    """ print the first and the last word of the sentence """
    words = sentence_split(sentence);
    words_first(words);
    words_last(words);

def print_first_and_last_sorted(sentence):
    """ print the first and the last word of the sorted sentence """
    words = sentence_split_sort(sentence);
    words_first(words);
    words_last(words);
"""
pydoc string.split
Help on function split in string:

string.split = split(s, sep=None, maxsplit=-1)
    split(s [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is given, splits at no more than
    maxsplit places (resulting in at most maxsplit+1 words).  If sep
    is not specified or is None, any whitespace string is a separator.
    
    (split and splitfields are synonymous)

pydoc sorted
Help on built-in function sorted in module __builtin__:

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list


"""

#str="my name is yang ming ming, I'm 20, how are you!"
#print str
#print "%s" %str
#print_first_and_last(str)
#print_first_and_last_sorted(str)
