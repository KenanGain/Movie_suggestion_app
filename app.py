import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
movies_titles = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommendation site')

selected_moviename = st.selectbox('Tell me your movie?', movies_titles)

if st.button('Recommend'):
    recomandations = recommend(selected_moviename)
    for i in recomandations:
        st.write(i)