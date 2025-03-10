import streamlit as st
import pickle
import pandas as pd


movies_dict= pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
# Title of the App
st.title("🎬 Movie Recommendation System")
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distancec = similarity[movie_index]
    movies_list = sorted(list(enumerate(distancec)), reverse=True, key=lambda x: x[1])[1:6]
    recommended=[]
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended
# User Input
selected_movies= st.selectbox(
    "please enter the movies."
    , movies['title'].values
)
if st.button("Recommend"):
    recommendations = recommend(selected_movies)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)
#
