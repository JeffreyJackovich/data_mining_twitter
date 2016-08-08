from nltk.corpus import stopwords
import string
from nltk import bigrams


#remove stopwords
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt','via', 'RT']


fname = 'processed_hash_tag_data.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)  # parsing JSON to a python dict
        #create a list with all the terms INCLUDES stop words
        terms_all = [term for term in preprocess(tweet['text'])]
        # WITHOUT STOPWORDS
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # count terms only once
        terms_single = set(terms_all)
        #count hashtags only
        #terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
        #count terms only (no hashtags, no mentions)
        terms_only = [term for term in preprocess(tweet['text']) if term not in stop and not term.startswith(('#', '@'))]
        # update the counter
        #count_all.update(terms_stop)
        #count_all.update(terms_hash)
        #count_all.update(terms_only)
        #
        #terms_bigram = bigrams(terms_stop)
        #
        #count_all.update(terms_bigram)
    #print 5 most frequent words
    print(count_all.most_common(25))