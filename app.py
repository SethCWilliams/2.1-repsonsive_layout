from flask import Flask
from flask import request
import requests


app = Flask(__name__)



@app.route("/")
def index():
    post_file = open('index.html', 'r')
    post_html = post_file.read()
    post_file.close()










#This gets the html and renders it to the screen.
index_file = open('index.html', 'r')
    index_html = index_file.read()
    index_html = index_html.replace('{{planet_list}}', planet_html)
    index_file.close()

    return index_html