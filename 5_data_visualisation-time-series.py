import pandas
import json

fname = 'nyse_friday_tweet.json'
f = open(fname, 'r') 

dates_nyse = []

# f is the file pointer to the JSON data set
for line in f:
    tweet = json.loads(line)
    # let's focus on hashtags only at the moment
    terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
    # track when the hashtag is mentioned
    if '#nyse' in terms_hash:
        dates_nyse.append(tweet['created_at'])
  

# a list of "1" to count the hashtags
ones = [1]*len(dates_nyse)
# the index of the series
idx = pandas.DatetimeIndex(dates_nyse)
# the actual series (at series of 1s for the moment)
nyse = pandas.Series(ones, index=idx)
 
# Resampling / bucketing
#per_minute = nyse.resample('1Min', how='sum').fillna(0)
per_hour = nyse.resample('H', how='sum').fillna(0) 


time_chart = vincent.Line(per_hour)
time_chart.axis_titles(x='Time', y='Freq')
time_chart.to_json('time_chart.json')

