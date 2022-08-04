import sys
sys.path.append("..")
sys.path.append("../models/")
import time
import matplotlib.image as mpimg
import os
from os.path import exists
from app.generator import generate_random_image_from_FEN
from app.inference import  make_prediction

import streamlit as st


### Styling the App
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css?family=Open+Sans&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Open Sans'
			}
            # body ,[class*="css"] {
            # background-image: url("https://ih1.redbubble.net/image.387186162.8319/flat,750x,075,f-pad,750x1000,f8f8f8.u9.jpg");
            # background-size: cover;
            # }
			</style>
			"""
   
st.markdown(streamlit_style, unsafe_allow_html=True)



    
def main():
    new_title = '<p style="font-size: 42px; font-weight:bolder;">AI Chess Master &#x265f;'+\
    '<br/></p><p style="font-size: 32px;">Welcome to my App!</p>'
    read_me_0 = st.markdown(new_title, unsafe_allow_html=True)
    input=st.text_input('Enter your FEN - To generate an image: ( it should be in this format shown)', value='8/8/8/8/8/8/8/8')
    generate = st.button('Generate Image')
    dummy_path = 'random/dummy.jpeg'
    if generate:
        FEN=str(input.strip()).replace(' ','')
        path = generate_random_image_from_FEN(FEN,'random/')
        os.rename(path, dummy_path)
        img  = mpimg.imread(dummy_path)
        rand= st.image(img)
        line_0=st.markdown("<hr style= size='6', color=black> ", unsafe_allow_html=True)
        st.header('the model can only see the image, the label is randomized')
    
    prediction = st.button('Predict Image')
    if prediction:
        if exists(dummy_path):
            result = make_prediction(dummy_path)
            st.success(result)
            predicted_image  = generate_random_image_from_FEN(result.replace('-','/'),optional_path='random/results/')
            st.subheader('Generated Image - ' +dummy_path)
            img  = mpimg.imread(dummy_path)
            st.image(img)
            st.subheader('Predicted Image - ' + result)
            st.image(predicted_image)
            
        else:
            st.error('Please generate an image first')
            
    line_0=st.markdown("<hr style= size='6', color=black> ", unsafe_allow_html=True)
    read_repo = st.markdown("""My Github repository can be found 
    [here](https://github.com/ibrahim-Sobh/AI-Chess-Position)""")
    

if __name__ == '__main__':
		main()	