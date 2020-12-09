from tmdb_client import get_movie_lists
from unittest.mock import Mock

def test_get_movie_list(monkeypatch):
    mock_movies_list = {'results':['Movie1', 'Movie2', 'Movie3']}
    requests_mock = Mock()

    response = requests_mock.return_value

    response.json.return_value = mock_movies_list
    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)

    movies_list = get_movie_lists(limit=2, list_name="popular")
    assert movies_list == mock_movies_list['results']




#dependency injection
