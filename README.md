# tweet_streamer
analysing tweets with textblob in realtime with logstash(using tweeter input) and flask endpoint to enrich data

##USAGE
  1. pip3 install -r requirements.txt
  2. python3 -m textblob.download_corpora
  3. python3 enrich.py
  4. add twitter logstash config to your pipeline
  4. start logstash service(pre-installed)
  
  That is it.
