import streamlit as st
import os
from pytube import YouTube  
import glob

st.set_page_config(page_title="The Name Bringer", page_icon=":tada:", layout="wide")
st.subheader("Hi, I am Michael :wave:")
st.title("A Data Engineer From Nigeria")

path = "./our_videos"

if not os.path.exists(path):
    os.makedirs(path)

for i in os.listdir(path):
    os.remove(path +'/' + i)

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_lowest_resolution()
        # Download the video to the specified output path
        video_stream.download(path)

        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")

video = st.text_input('please drop your youtube link:')
download_youtube_video(str(video))

print(os.listdir(path))
st.write('The current video title is', os.listdir(path))


 