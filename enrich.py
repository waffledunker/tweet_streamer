#!/usr/bin/python3
from flask import Flask,jsonify, render_template, redirect, url_for, request
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.corpus import movie_reviews
import re
import logging as log

#logging configurations
log.basicConfig(filename='enrich_access.log',filemode='a',level=log.DEBUG)

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello():
    return redirect(url_for('predict_a_tweet'), code=302)

@app.route('/predict', methods=['POST'])
def predict_a_tweet():
    tweet_content = request.get_json()
    cleaned_tweet = clean_text(tweet_content)
    if cleaned_tweet is not 'neutral':
        positive_likelyhood = text_blob(cleaned_tweet).sentiment.p_pos
        if 0.45 <= positive_likelyhood <= 0.55:
            return jsonify(sentiment="neutral", score=positive_likelyhood)
        if positive_likelyhood > 0.60:
            return jsonify(sentiment="positive", score=positive_likelyhood)
        else:
            return jsonify(sentiment="negative", score=positive_likelyhood)
    else:
        return jsonify(sentiment="TypeError", score= 0.0000)

def clean_text(tweet_to_clean):
    ## only string data
    if type(tweet_to_clean) is str:
        log.info("requested to predict : {}".format(tweet_to_clean['text']))
        return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tweet_to_clean['text']).split())
    else:
        log.info("request is not string type : {}".format(tweet_to_clean['text']))
        return 'neutral'


if __name__ == '__main__':
    log.info("Starting the server!")
    text_blob = Blobber(analyzer=NaiveBayesAnalyzer())
    app.run(host='0.0.0.0',port=9555, debug=True)
