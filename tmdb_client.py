import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NDI0ZTdhMTBhZDBiMmQ4ZDFlYzg5ZjMwZDFmNWQ4NiIsInN1YiI6IjVmYTE4ZDlmNjkxY2Q1MDAzNmNlMzYwZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.jQq0KYdq0F6vc9XZXu9_pDocr2A_4uCZsR2lVmozQMQ"

def get_popular_movies(limit):
    ENDPOINT = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(ENDPOINT, headers=headers)
    randomised_response = random.sample(response.json()['results'], k=limit)
    return randomised_response
    # return response.json()['results'][:limit]

def get_movie_lists(limit, list_name):
    ENDPOINT = f"https://api.themoviedb.org/3/movie/{list_name}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(ENDPOINT, headers=headers)
    original_status_code = response.status_code
    # response.raise_for_status()
    if response.status_code == 404:
        ENDPOINT = f"https://api.themoviedb.org/3/movie/popular"
        response = requests.get(ENDPOINT, headers=headers)
    randomised_response = random.sample(response.json()['results'], k=limit)
    return randomised_response, original_status_code
    # return response.json()['results'][:limit]

def get_single_movie(movie_id):
    ENDPOINT = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    return requests.get(ENDPOINT, headers=headers).json()


def get_single_movie_cast(movie_id):
    ENDPOINT = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    return requests.get(ENDPOINT, headers=headers).json()['cast']

def get_poster_url(poster_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_path}"

def get_random_backdrop(movie_id):
    ENDPOINT = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(ENDPOINT, headers=headers)
    randomised_response = random.choice(response.json()['backdrops'])
    return randomised_response['file_path']


# print(get_popular_movies(1))
