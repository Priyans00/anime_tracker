from flask import Flask, render_template, request
import requests
from queries import*

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/tracker', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        anime_name = request.form['userInput']
        data = fetch_anime_details(anime_name)
    return render_template('index.html', data=data)

@app.route('/character',methods=['GET','POST'])
def character():
    data = None 
    if request.method == 'POST':
        character_name = request.form['userInput']
        data = fetch_character_details(character_name)
    return render_template('character.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)
