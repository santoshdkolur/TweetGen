import streamlit as st
import tweetGenerator as TG
from PIL import Image
import os

def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


st.title("Thulp Fiction")
st.text(os.getcwd())
st.caption("Template Tweet")
st.image("Template.png")

name = st.text_input("Name")
st.text("")
username = st.text_input("Username")
st.text("")
tweet = st.text_input("Enter your tweet")
st.text("")
retweet = st.text_input("Enter your re-tweet")
st.text("")

#uploaded_file = st.file_uploader("Upload an image to the tweet if required",type=['jpg'])
#if uploaded_file:
#    tweetImg = 1
#    with open("uploadedTweetImg.jpg","wb") as file:
#        file.write(uploaded_file.getbuffer())
#else:
#    tweetImg = None
tweetImg=1
generate = st.button("Generate")

if generate:
    img = TG.generate(name,username,tweet,tweetImg)
    if img:
        try:
            with open("finalImageStreamlit.png","wb") as file:
                file.write(img)
            make_square(Image.open("finalImageStreamlit.png")).save("finalImageStreamlit2.png")
            st.image("finalImageStreamlit2.png")
        except:
            st.text("Error in Tweet generation!")

    st.text("_____________________________________________________________________________________________")
    st.text("---------------------------------------------------------------------------------------------")

    img= TG.generate(name,username,retweet,tweetImg)
    if img:
        try:
            with open("RefinalImageStreamlit.png","wb") as file:
                file.write(img)
            make_square(Image.open("RefinalImageStreamlit.png")).save("RefinalImageStreamlit2.png")
            st.image("RefinalImageStreamlit2.png")

        except:
            st.text("Error!")
        


