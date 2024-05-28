from ast import literal_eval
from pandas import read_csv, Series
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_tools import clean_data, create_soup, get_director, get_list
from joblib import dump
from os import makedirs

df_credits = read_csv('../input/tmdb-movie-metadata/tmdb_5000_credits.csv')
df_movies = read_csv('../input/tmdb-movie-metadata/tmdb_5000_movies.csv')

df_credits.columns = ['id', 'tittle', 'cast', 'crew']
df_movies = df_movies.merge(df_credits, on='id')
df_movies['overview'] = df_movies['overview'].fillna('')

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    df_movies[feature] = df_movies[feature].apply(literal_eval)

df_movies['director'] = df_movies['crew'].apply(get_director)

features = ['cast', 'keywords', 'genres']
for feature in features:
    df_movies[feature] = df_movies[feature].apply(get_list)

features = ['cast', 'keywords', 'director', 'genres']

for feature in features:
    df_movies[feature] = df_movies[feature].apply(clean_data)

df_movies['soup'] = df_movies.apply(create_soup, axis=1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df_movies['soup'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

df_movies = df_movies.reset_index()
indices = Series(df_movies.index, index=df_movies['title'])

makedirs('components', exist_ok=True)
dump(df_movies, 'components/df_movies.pkl')
dump(cosine_sim, 'components/cosine_sim.pkl')
dump(indices, 'components/indices.pkl')
print("Model components created")
