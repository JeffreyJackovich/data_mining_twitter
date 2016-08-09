import re
import json 
import sys
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
from collections import defaultdict


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 

def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=True):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


#remove stopwords
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt','via', 'RT']


#co-occurrences
com = defaultdict(lambda : defaultdict(int))
fname = './twitter_data/data.json'
with open(fname, 'r') as f:
    count_all = Counter()
    # f is the file pointer to the JSON data set
    for line in f: 
        tweet = json.loads(line)
        terms_only = [term for term in preprocess(tweet['text']) 
                      if term not in stop 
                      and not term.startswith(('#', '@'))]
     
        # Build co-occurrence matrix
        for i in range(len(terms_only)-1):            
            for j in range(i+1, len(terms_only)):
                w1, w2 = sorted([terms_only[i], terms_only[j]])                
                if w1 != w2:
                    com[w1][w2] += 1


com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])


# co-occurrences for specific term passed in as command-line argument
# fname = './twitter_data/data.json'
# with open(fname, 'r') as f:
#     search_word = sys.argv[1] # pass a term as a command-line argument
#     count_search = Counter()
#     for line in f:
#         tweet = json.loads(line)
#         terms_only = [term for term in preprocess(tweet['text']) 
#                       if term not in stop 
#                       and not term.startswith(('#', '@'))]
#         if search_word in terms_only:
#             count_search.update(terms_only)
#     print("\nCo-occurrence for %s:" % search_word)
#     print(count_search.most_common(20))
