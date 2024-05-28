from env import TMDB_API_KEY
from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
from joblib import load
import requests

df_movies = load('../model/components/df_movies.pkl')
cosine_sim = load('../model/components/cosine_sim.pkl')
indices = load('../model/components/indices.pkl')

app = Flask(__name__)
CORS(app)

last_call = ''
call_counter = 1


@app.route('/')
def index():
    return render_template('frontend.html')


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    title = request.args.get('title')
    if title is None:
        return jsonify({'error': 'Please provide a movie title as "title" parameter'}), 400

    idx = indices.get(title)
    if idx is None:
        return jsonify({'error': f'Movie with title "{title}" not found'}), 404

    global last_call, call_counter

    if last_call == title:
        call_counter += 1
    else:
        call_counter = 1
        last_call = title

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1 + (call_counter - 1) * 5:6 + (call_counter - 1) * 5]
    movie_indices = [i[0] for i in sim_scores]
    recommended_movies = df_movies.iloc[movie_indices]['title'].tolist()
    posters = get_posters(recommended_movies)
    return {'titles': posters, 'repetitive': call_counter}, 200


def get_posters(titles):
    posters = {}
    for title in titles:
        response = requests.get('https://api.themoviedb.org/3/search/movie', params={'api_key': TMDB_API_KEY, 'query': title})
        if response.status_code == 200:
            results = response.json().get('results', [])
            if results:
                movie_info = results[0]
                poster_path = movie_info.get('poster_path')
                movie_id = movie_info.get('id')
                if poster_path and movie_id:
                    poster_url = f'https://image.tmdb.org/t/p/w500/{poster_path}'
                    movie_link = f'https://www.themoviedb.org/movie/{movie_id}'
                    posters[title] = {'poster_url': poster_url, 'movie_link': movie_link}
    return posters


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
