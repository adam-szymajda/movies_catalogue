from flask import Flask, render_template, request, url_for
import tmdb_client
import time


app = Flask(__name__)

@app.route("/")
def homepage():
    count = 8
    list_types = ["incorrect", "now_playing", "popular", "top_rated", "upcoming"]
    selected_list = request.args.get('list_name', "popular")
    movies, status_code = tmdb_client.get_movie_lists(count, list_name=selected_list)
    if status_code == 200:
        return render_template("homepage.html", movies=movies, list_types=list_types, selected_list=selected_list)
    else:
        return render_template("homepage.html", movies=movies, list_types=list_types, selected_list='popular')


@app.route("/movie/<movie_id>/")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    movie['backdrop_path'] = tmdb_client.get_random_backdrop(movie_id)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id)
    return render_template("movie_details.html", movie=movie, movie_cast=movie_cast)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {'tmdb_image_url': tmdb_image_url}

@app.context_processor
def utility_processor():
    def age_category(movie):
        if movie.get('adult'):
            return "bg-danger"
        return "bg-success"
    return {'age_category': age_category}

@app.context_processor
def utility_processor():
    def url_for_list_type(list_type):
        return url_for('homepage', list_name=list_type)
    return {'url_for_list_type': url_for_list_type}


if __name__ == "__main__":
    app.run(debug=True)
