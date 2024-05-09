import streamlit as st
import pandas as pd 

st.subheader("Loading the csv file.")
df =st.file_uploader("Upload the csv file :" ,type =['csv','xlsx'])

#if df is not None:
    #st.dataframe(df)

df =pd.read_csv('Products.csv')
st.table(df.head())

st.subheader('Dealing with images while uploading.')
st.image('img.png')
img_file =st.file_uploader("Upload the Image file : ",type =['png','jpeg'])

if img_file is not None:
    st.image(img_file)

st.subheader('Working with videos.')

video_file =st.file_uploader("Upload the videofile : ",type =['mkv','mp4','mp3'])
if video_file is not None:
    st.video(video_file,start_time =0)

st.subheader('Working with audio.')
audio_file =st.file_uploader("Upload the videofile : ",type =['wav','mp3'])
if audio_file is not None:
    st.audio(audio_file.read())
