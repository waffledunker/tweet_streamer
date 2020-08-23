#!/usr/bin/python3
from flask import Flask,jsonify, render_template, redirect, url_for, request
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
#we need this to use naive bayes. it uses movie_revies corpus to predict
from nltk.corpus import movie_reviews
import re


app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello():
    return redirect(url_for('predict_a_tweet'), code=302)

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


def clean_text(tweet_to_clean):
    print(tweet_to_clean['text'])
    tmp = tweet_to_clean['text']
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",tmp).split())

if __name__ == '__main__':
    text_blob = Blobber(analyzer=NaiveBayesAnalyzer())
    app.run(host='0.0.0.0',port=9555, debug=True)
