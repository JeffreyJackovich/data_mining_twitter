
import vincent


fname = 'nyse_friday_tweet.json'
      
wordfreq = count_all.most_common(10)
labels, freq = zip(*wordfreq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.axis_titles(x='#hashtags', y='Frequency')
bar.to_json('wordfreq.json')
