from tmdb_client import get_single_movie
from unittest.mock import Mock

def test_get_single_movie_correct_response(monkeypatch):
    mock_movie = 'Movie1'

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie

    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)
    movie = get_single_movie(movie_id = 1)
    assert movie == mock_movie

def test_get_single_movie_api_not_available(monkeypatch):
    mock_movie = None

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie

    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)
    movie = get_single_movie(movie_id = 1)
    assert movie == None

def test_get_single_movie_invalid_response(monkeypatch):
    mock_movie = ['Movie1', 'Movie2']

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie

    monkeypatch.setattr('tmdb_client.requests.get', requests_mock)
    movie = get_single_movie(movie_id = 1)
    assert not (movie == mock_movie)
