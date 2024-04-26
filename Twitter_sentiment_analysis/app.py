import re
from textblob import TextBlob
from flask import Flask, render_template, request


def clean_sentence(sentence):

    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", sentence).split())

def get_sentence_sentiment(sentence):
    analysis = TextBlob(clean_sentence(sentence))

    if analysis.sentiment.polarity > 0:
        return "positive"
    
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    
    else:
        return "negative"

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')

def home():
    return render_template("index.html")

# *******Sentence level sentiment analysis

@app.route("/predict1", methods=['POST', 'GET'])

def pred1():

    if request.method == 'POST':
        sentence = request.form['txt']
        sentiment = get_sentence_sentiment(sentence)
        return render_template('result1.html', msg=sentence, result=sentiment)


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')