from distutils.log import debug
import trafilatura
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from flask import Flask, request, jsonify, Response, render_template
from ratelimit import limits
import nltk

nltk.download('punkt')

app = Flask(__name__)
#index_html = ""
#homepage_html = ""    
#with open('index.html', 'r') as f:
#    index_html = f.read()
# print(index_html) 

#with open('homepage.html', 'r') as f:  #for loop variable jaise
#    homepage_html = f.read()

@app.route('/', methods=['GET', 'POST']) 

def homepage():
    return render_template('homepage.html' )
#    return Response(homepage_html, mimetype="text/html")

@app.route('/summarize/', methods=['GET', 'POST']) 
@limits(calls=1, period=1)
def respond():
    data = request.form.get("text", None)
    length = request.form.get("length", None)
    print(length)
    LANGUAGE = "english"
    print(data)
    parser = PlaintextParser.from_string(data, Tokenizer(LANGUAGE))
    # parser = Tokenizer(LANGUAGE)
    # print(parser.to_sentences(data))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    # downloaded = trafilatura.fetch_url('https://hi.wikipedia.org/wiki/%E0%A4%A4%E0%A4%BE%E0%A4%9C%E0%A4%AE%E0%A4%B9%E0%A4%B2')
    # print(downloaded)
    # y = trafilatura.process_record(downloaded, include_comments=False, include_tables=False, target_language="en")
    # print(y)
    y = data
    response = []
    if(y == None):
        firstParagraph = ""
        l = len(parser.document.sentences)
        SENTENCES_COUNT = int(l*float(length))
    else:
        firstParagraph = ""
        l = len(y.split("\n"))
        SENTENCES_COUNT = int(l*float(length))
        for p in y.split("\n"):
            if len(p) > 150:
                firstParagraph = p
                break

    if firstParagraph!="":
        response.append(firstParagraph+"\n\n")
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        if str(sentence) not in firstParagraph:
            response.append(str(sentence) + "  ")

    res = ""

    for s in response:
        res += s
    #summary = index_html.format(summary=res)
    return render_template('index.html', summary = res)
    #return Response(summary, mimetype="text/html")


@app.route('/text/', methods=['POST'])
@limits(calls=1, period=1)
def respond_text():

    y = request.form.get("text", None)
    length = request.form.get("length", None)

    LANGUAGE = "english"
    parser = PlaintextParser.from_string(y,Tokenizer("english"))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    response = []
    l = len(y.split(". "))
    SENTENCES_COUNT = int(l*float(length))*2

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        response.append(str(sentence) + "  ")

    res = ""

    for s in response:
        res += s

    return Response(res, mimetype="text/plain")



if __name__ == '__main__':

    app.run(threaded=True, port=5000, debug = True)