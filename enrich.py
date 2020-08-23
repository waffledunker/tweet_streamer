#!/usr/bin/python3
from flask import Flask,jsonify, render_template, redirect, url_for, request
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.corpus import movie_reviews
import re


app = Flask(__name__)

##reroute to predict enpoint
@app.route('/',methods=['POST'])
def hello():
    return redirect(url_for('predict_a_tweet'), code=302)

##prediction endpoint
@app.route('/predict', methods=['POST'])
def predict_a_tweet():
    tweet_content = request.get_json()
    cleaned_tweet = clean_text(tweet_content)
    positive_likelyhood = text_blob(cleaned_tweet).sentiment.p_pos
    if 0.45 <= positive_likelyhood <= 0.55:
        return jsonify(sentiment="neutral", score=positive_likelyhood)
    if positive_likelyhood > 0.60:
        return jsonify(sentiment="positive", score=positive_likelyhood)
    else:
        return jsonify(sentiment="negative", score=positive_likelyhood)

###replace any impurities in text then split the data for textblob
def clean_text(tweet_to_clean):
    print(tweet_to_clean['text'])
    tmp = tweet_to_clean['text']
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tmp).split())

### "http://0.0.0.0:9555/predict"
if __name__ == '__main__':
    text_blob = Blobber(analyzer=NaiveBayesAnalyzer())
    app.run(host='0.0.0.0',port=9555, debug=True)
