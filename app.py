from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def fetch_anime_details(anime_name):
    url = "https://graphql.anilist.co"
    query = """
    query ($search: String) {
        Media(search: $search, type: ANIME) {
            id
            title {
                romaji
                english
                native
            }
            description
            episodes
            genres
            averageScore
            coverImage {
                large
            }
        }
    }
    """
    variables = {"search": anime_name}
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.json()

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

if __name__ == '__main__':
    app.run(debug=True)
