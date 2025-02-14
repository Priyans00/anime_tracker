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
        gender
        image {
          large
        }
        description
        gender
        favourites
        bloodType
        name {
          alternative
          full
        }
        } 
      }
    }
    """
    variables = {"search": character_name}
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.json()

#for fetching anime news details 
def fetch_anime_news(anime_year):
    url = "https://graphql.anilist.co"
    query = """
    query ($seasonYear: Int, $sort: [MediaSort]) {
      Page( page:1,perPage: 40) {
        media( seasonYear: $seasonYear, type: ANIME,sort:$sort) {
          id
          title {
            romaji
            english
          }
          startDate {
            year
            month
            day
          }
          coverImage {
            large
          }
          genres
          endDate {
            year
            month
            day
          }
        }
      }
    }"""
    variables = {"seasonYear": anime_year,"sort": ["POPULARITY_DESC"]}
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.json()

#for fetching trending animes
def fetch_pics():
    url = "https://graphql.anilist.co"
    query = """
    query jjh{
      Page(page:1, perPage: 40) {
        media( , type: ANIME, sort: [POPULARITY_DESC], ) {
          title {
            romaji
            english
          }
          coverImage {
            large
          }
        }
      }
    }"""
    response = requests.post(url, json={"query": query})
    return response.json()