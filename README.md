# tweet_streamer
analysing tweets with kibana in realtime with;
- logstash(using twiter input)
- flask rest api to analyse tweet sentiments 
  - textblob and nltk

##USAGE
  1. pip3 install -r requirements.txt
  2. python3 -m textblob.download_corpora
  3. python3 enrich.py
  4. add twitter logstash config to your pipeline
  4. start logstash service(pre-installed)
  ![alt text](https://github.com/waffledunker/tweet_streamer/blob/master/dashboard_simple.PNG?raw=true)
  ![alt text](https://github.com/waffledunker/tweet_streamer/blob/master/proof.PNG?raw=true)
  ![alt text](https://github.com/waffledunker/tweet_streamer/blob/master/logs.PNG?raw=true)
  
  That is it.
