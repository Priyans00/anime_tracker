import requests

#for fetching anime details --- string search
def fetch_anime_details(anime_name):
    url = "https://graphql.anilist.co"
    query = """
    query ($search: String) {
      Page(perPage: 50) {
        media(search: $search, type: ANIME) {
        id
        title {
          romaji
          english
        }
        genres
        averageScore
        description
        season
        episodes
      
        seasonYear
        format
        coverImage{
          large
        }
        }
      }
    }"""

    variables = {"search": anime_name}
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.json()

#for fetching character details --- string search
def fetch_character_details(character_name):
    url = "https://graphql.anilist.co"
    query = """
    query Character($search: String) {
      Page(perPage:10){
        characters(search:$search) {
        age
        dateOfBirth {
          day
          year
          month
        }
        image {
          large
        }
        description
        gender
        favourites
        bloodType
        name {
          alternative
          alternativeSpoiler
          full
        }
        } 
      }
    }
    """
    variables = {"search": character_name}
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.json()