 
<h2><strong>Goal</strong></h2> 
<ul>Access tweets via Twitter's public API options and perform a Sentiment Analysis on stock market related tweets.</ul>


<h2><strong>Why Twitter?</strong></h2> 
<ul>Twitter's REST API provides access to ~500 million daily tweets with numerous options via a 
<a href="https://dev.twitter.com/rest/public/search">Search API</a> and <a href="https://dev.twitter.com/streaming/overview">Streaming API</a>.
Accessing the data is streamlined with python's <a href="http://www.tweepy.org/">Tweepy</a>.</ul>
 
 
<h2><strong>Project Outline:</strong></h2> 
<ul>1. Tweet collection via <a href="https://github.com/JeffreyJackovich/data_mining_twitter/blob/master/1_tweet_streaming_collection.py">Streaming API</a> and<a href="https://github.com/JeffreyJackovich/data_mining_twitter/blob/master/1_tweet_collection.py"> Search API</a>.</ul>
<ul>2. <a href="https://github.com/JeffreyJackovich/data_mining_twitter/blob/master/2_text_pre-processing.py">Tweet Pre-processing</a></ul>
<ul>3. <a href="https://github.com/JeffreyJackovich/data_mining_twitter/blob/master/3_term_frequencies.py">Term Frequencies</a></ul>
<ul>4. <a href="https://github.com/JeffreyJackovich/data_mining_twitter/blob/master/4_term_co-occurrences.py">Term Co-Occurrences</a></ul>
<ul>5. <a href="https://github.com/JeffreyJackovich/data_mining_twitter/blob/master/5_data_visualisation-term-frequency.py">Data Visualisation</a></ul>

<h2><strong>Why is this interesting?</strong></h2>
<ul>Provides a basic framework to develop more complex data pipelines.</ul>


<h2><strong>Next Steps?</strong></h2>
<ul>1. Geolocation with Leaflet.js</ul>
<ul>2. Build a real-time sentiment dashboard</ul>


<h2><strong>Dependencies</strong></h2>
<ul>Data collection: <a href="http://www.tweepy.org/">Tweepy</a></ul>
<ul><a href="http://www.nltk.org/">NLTK</a></ul>
<ul>Data Visualisiation:<a href="https://github.com/wrobstory/vincent">Vincent</a> to utilize <href="https://d3js.org/">D3.js</a></ul>
<ul>Time Series Data Visualisiation:<a href="http://pandas.pydata.org/">Pandas</a> and <a href="https://github.com/wrobstory/vincent">Vincent</a></ul>


<h2><strong>Project Source</strong></h2>
<ul>I followed Marco Bonzanini's,<a href="https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/"> Mining twitter data with python</a>.
