from flask import Flask, jsonify, request
from newspaper import Article
import nltk
nltk.download('punkt')
import requests
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='092d1aeb4ca74c9fbb5541d00ed79140')
import json
app = Flask(__name__)
class SummaryArticle:
    def __init__(self, title, summary):
        self.title = title
        self.summary = summary

@app.route('/fetchArticles', methods=['GET'])
def index():
    searchQuery = request.args['searchText']
    url1 = ('http://newsapi.org//v2/everything?'
            'q='+searchQuery+'&'    
            'apiKey=092d1aeb4ca74c9fbb5541d00ed79140')
    response = requests.get(url1)
    data=response.json()
    l=data['articles']
    n=len(l)
    articleResp = []
    if(n<=3):
        for i in range(0,n):
            article = Article(l[i]['url'], language="en")
            article.download() 
            article.parse() 
            article.nlp()
            art = {
                "title": article.title,
                "summary": article.summary
            }
            articleResp.append(art)
    else :
        for i in range(0,5):
            article = Article(l[i]['url'], language="en")
            article.download() 
            article.parse() 
            article.nlp()
            art = {
                "title": article.title,
                "summary": article.summary
            }
            articleResp.append(art)
    return jsonify(articleResp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
