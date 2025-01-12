import requests

#for fetching anime details --- string search
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

#for fetching character details --- string search
def fetch_character_details(character_name):
    url = "https://graphql.anilist.co"
    query = """
    query Character($search: String) {
    Character(search:$search) {
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
    """
    variables = {"search": character_name}
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.json()